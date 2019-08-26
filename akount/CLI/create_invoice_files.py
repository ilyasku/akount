import os
from shutil import copyfile
import pandas as pd
import click

from ..template_loader import (path_to_invoices_template, path_to_invoices_people_template)

@click.command()
@click.argument('name')
def main(name):
    required_files = ['people.csv', 'deposits.csv']
    file_missing_msg = "File '{}' missing! Not a valid akount folder. "
    file_missing_msg += "See README on https://github.com/ilyasku/akount."
    for f in required_files:
        if not os.path.exists(f):        
            raise RuntimeError(file_missing_msg.format(f))
    if not os.path.exists('invoices'):
        os.mkdir('invoices')

    people = pd.read_csv('people.csv', index_col=0)
    invoices_people = pd.read_csv(path_to_invoices_people_template)

    for p in people.iterrows():
        print(p)
        
    copyfile(path_to_invoices_template, os.path.join('invoices', '{}.csv'.format(name)))

   

if __name__ == "__main__":
    main()
