"""
USAGE: 
   o install in develop mode: navigate to the folder containing this file,
                              and type 'python setup.py develop --user'.
                              (ommit '--user' if you want to install for 
                               all users)                           
"""


from setuptools import setup

setup(name='akount',
      version='0.0.1',
      description='Manage accounts, bills and payments between a group of people.',
      url='',
      author='Ilyas Kuhlemann',
      author_email='ilyasp.ku@gmail.com',
      license='GNU GPLv3',
      packages=['akount',
                'akount.CLI'],
      entry_points={
          "console_scripts": [
              'akount-calculate-balance=akount.CLI.calculate_balance:main',
              'akount-create-invoice-files=akount.CLI.create_invoice_files:main'
          ],
          "gui_scripts": [
          ]
      },
      install_requires=['pandas',
                        'click'],
      zip_safe=False)
