Cookiecutter template
---------------------

This is a cookiecutter template created from https://github.com/claws/cookiecutter-python-project and adapted to meet the individual needs of this project. 

To use it, clone the project 

```bash
git clone git@gitlab.com:opendatascientists/madrid-cookiecutter-template.git
```

create and activate a conda virtualenv for ``cookiecutter``


```bash
conda create --name cookiecutter --python=3.10
conda activate cookiecutter
```

install `cookiecutter`

```bash
pip install cookiecutter==1.7.3
```


run `cookiecutter`

```bash
cookiecutter madrid-cookiecutter-template/
```

and follow the instructions asked by the script. 

Create a conda environment
--------------------------

Go to the [environment configuration](https://team-1634581945508.atlassian.net/wiki/spaces/OPENDATASC/pages/2916354/Configuraci+n+inicial+del+entorno#Crear-entorno-virtual) page in Confluence to learn how to create and configure a conda environment

Check that everything went ok
-----------------------------
After finishing, check the folder called `package_name` as specified in the second answer of the creation script. The following steps, in which we will check that the creation of the new project was successful, it is assumed that package name is `my_package`. Replace the name by the one you specified.

- Go to the folder with `cd my_package`
- Run `pip install -r requirements` to install template dependencies 
- Execute the test command `python -m my_package.my_package cli-test`. If the output is `Click CLI is working!`, then everything is set.
