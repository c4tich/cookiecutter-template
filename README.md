Cookiecutter template
---------------------

This is a cookiecutter template created from https://github.com/claws/cookiecutter-python-project and adapted to meet the individual needs of this project. 

To use it, clone the project with either SSH (preferred) or HTTPS 

```bash
# ssh
git clone git@git.hermes3x-cidelcampeador.duckdns.org:cfortichj/cookiecutter-template.git

# https
git clone https://git.hermes3x-cidelcampeador.duckdns.org/cfortichj/cookiecutter-template.git
```

create and activate a [conda virtualenv](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) for ``cookiecutter`` (note that this environment is only used for cookiecutter, the projects based on this template should use a different conda virtual env)


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
cookiecutter cookiecutter-template/
```

and follow the instructions asked by the script. 

Check that everything went ok
-----------------------------
After finishing, check the folder called `package_name` as specified in the second answer of the creation script. The following steps, in which we will check that the creation of the new project was successful, it is assumed that package name is `my_package`. Replace the name by the one you specified.

- Go to the folder with `cd my_package`
- Run `pip install -r requirements` to install template dependencies 
- Execute the test command `python -m my_package.my_package cli-test`. If the output is `Click CLI is working!`, then everything is set.
