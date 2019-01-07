from setuptools import setup, find_packages

setup (
  name 			= "calcbackend",
  version		= "0.1.0",
  description		= "my calc backend",
  packages		= find_packages(),
  include_package_data  = True,
  scripts		= ['calculator.py','mywsgi.py'],
  install_requires 	= ['Flask==1.0.2',
			   'flask-httpauth==3.2.4', 
			   'Jinja2==2.10',
			   'sqlalchemy',
			   'requests==2.21.0',
			   'nose==1.3.7',
			   'coverage==4.5.2',
			   'rednose==1.3.0',
			   'mysqlclient',
                           'uwsgi']
)
