Contributing Guide
==================

Contributions are welcome and greatly appreciated!


.. _contributing-workflow-label:

Workflow
--------

A bug-fix or enhancement is delivered using a pull request. A good pull request
should cover one bug-fix or enhancement feature. This strategy ensures the
change set is easier to review and less likely to need major re-work or even be
rejected.

The workflow that developers typically use to fix a bug or add enhancements
is as follows.

* Fork the ``{{cookiecutter.gitlab_repo_name}}`` repo into your account.

* Obtain the source by cloning it onto your development machine.

  .. code-block:: console

      $ git clone git@gitlab.com:opendatascientists/{{cookiecutter.gitlab_repo_name}}.git
      $ cd {{cookiecutter.package_name}}

* Create a branch for local development:

  .. code-block:: console

      $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally.

* Create and activate a Conda virtual environment for local development. This
  rule also specifies a project specific prompt label to use once the virtual
  environment is activated.

  .. code-block:: console

      $ conda create --name {{cookiecutter.gitlab_repo_name}} --python=3.10
      $ conda activate {{cookiecutter.gitlab_repo_name}}

* Develop fix or enhancement:

  * Make a fix or enhancement (e.g. modify a class, method, function, module,
    etc).

  * Update an existing unit test or create a new unit test module to verify
    the change works as expected.

  * Run the test suite.

    .. code-block:: console

        ({{cookiecutter.package_name}}) $ pytest 

    See the :ref:`testing-label` section for more information on testing.

  * Commit and push changes to your fork.

  .. code-block:: console

      $ git add .
      $ git commit -m "A detailed description of the changes."
      $ git push origin name-of-your-bugfix-or-feature

  A pull request should preferably only have one commit upon the current
  master HEAD, (via rebases and squash).

* Submit a pull request through the service website (e.g. Github, Gitlab).

* Check automated continuous integration steps all pass. Fix any problems
  if necessary and update the pull request.
