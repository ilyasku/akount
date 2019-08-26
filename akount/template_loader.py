import os

_HERE = os.path.abspath(os.path.split(__file__)[0])
_template_folder = os.path.join(_HERE, '..', 'templates')

path_to_people_template = os.path.join(_template_folder, 'people.csv')
path_to_deposits_template = os.path.join(_template_folder, 'deposits.csv')
path_to_invoices_template = os.path.join(_template_folder, 'invoices.csv')
path_to_invoices_people_template = os.path.join(_template_folder, 'invoices_people.csv')
