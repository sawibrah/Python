# Python

This repositories is all about python

## Virtual environment in python

### Using venv
The command below lists the modules install in your global python environment
`$ pip list`

`$ mkdir my_project`
`$ cd my_project`

This install the virtual environment call `project_env`, note that the second `venv` is the environment name one can use another name like `project_env` for instancte.
`$ python3 -m venv venv`

This activate your environment
`$ soure venv/bin/activate`

This to check which python your virtual environment is using
`$ which python`

This will list the modules in you virtual environment
`$ pip list`

How to install a package in your virtual environment
`$ pip install package_name`

List the modules with the version (almost like `pip list`) but her the ouput can be used to creat a requirements files
`$ pip freeze`

How to create a `requirements.txt` files
`$ pip freeze > requirements.txt`

How to deactivate the virtual environment
`$ deactivate`

How to delete the virtual environment
`$ rm -rf project_env`

### Using `virtualenv`

`virtualenv env_name -p pythons`


### Using `pipenv`

Installing `pipenv`
`$ pip install pipenv pip --upgrade`

Install env
`$ pip install -python python3`

Activate env
`$ pip shell`
