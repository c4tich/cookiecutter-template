from setuptools import setup, find_packages

with open("README.md") as fd_readme:
    readme = fd_readme.read()

with open("CHANGELOG.md") as fd_changelog:
    changelog = fd_changelog.read()

with open("requirements.txt") as fd_requirements:
    requirements = [req.strip() for req in fd_requirements.readlines() if not req.startswith("#")]

with open("VERSION.txt") as fd_version:
    version = fd_version.read().strip()

setup(
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="""{{cookiecutter.package_short_description}}""",
    entry_points={
        "console_scripts": [
            "{{cookiecutter.package_name}}={{cookiecutter.package_name}}.{{cookiecutter.package_name}}:main"
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    name="{{cookiecutter.package_name}}",
    packages=find_packages(
        include=[
            "{{cookiecutter.package_name}}",
            "{{cookiecutter.package_name}}.*"
        ]
    ),
    test_suite="tests",
    url="https://{{cookiecutter.git_server_host}}/{{cookiecutter.git_server_username}}/{{cookiecutter.package_name}}.git",
    version=version,
    zip_safe=False
)
