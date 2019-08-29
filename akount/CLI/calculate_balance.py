import os
import pandas as pd

fname_people_template = os.path.join('invoices', '{}_people.csv')
fname_invoices_template = os.path.join('invoices', '{}.csv')

def get_people_df(deposits: pd.DataFrame) -> pd.DataFrame:
    people = pd.read_csv('people.csv', index_col=0)
    people['Balance'] = 0.0
    people.index = people.index.str.lower().str.strip()    
    for row in deposits.iterrows():
        name, amount, date = row[1]
        people.loc[name, 'Balance'] += amount
    return people

def main():

    deposits = pd.read_csv('deposits.csv')
    deposits['Name'] = deposits['Name'].str.lower().str.strip()
    people = get_people_df(deposits)
    
    invoices_list = pd.read_csv('invoice_list.csv', header=None)[0]
    for inv in invoices_list:
        invoices = pd.read_csv(fname_invoices_template.format(inv))
        invoices['Name'] = invoices['Name'].str.lower().str.strip()
        people_dc = pd.read_csv(fname_people_template.format(inv))
        people_dc['Name'] = people_dc['Name'].str.lower().str.strip()
        people_dc.index = people_dc['Name']
        weight_total = people_dc['Weight'].sum()
        people_dc['Weight-fraction'] = people_dc['Weight']/weight_total
        total_price = 0.0
        for row in invoices.iterrows():
            name, amount = row[1][:2]
            if name.strip() not in people_dc['Name'].values:
                raise RuntimeError(
                    'Name "{}" of invoice not in list of people for date {}!'.format(
                        name, inv))
            total_price += amount
            people.loc[name, 'Balance'] += amount
        for name in people_dc['Name']:
            people.loc[name, 'Balance'] -= total_price * people_dc.loc[name, 'Weight-fraction']

    assert abs(deposits['Amount'].sum()-people['Balance'].sum()) < 1e-6
    print("There is {:.2f} Euro in the cash register!".format(deposits['Amount'].sum()))

    people.to_csv('balance_calculated.csv')
    people.to_csv('people.csv')

    
if __name__ == "__main__":
    main()
