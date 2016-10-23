Installation
==============

There roles are not yet available in Ansible Galaxy.
For now, you need to install them manually

Install an ansible role manually
--------------------------------

Download the project locally

.. code-block:: text

    git clone https://github.com/Juniper/ravello-ansible.git

Add path to the directory to the variable ``roles_path`` into your Ansible configuration.
Ansible can have multiple configuration file [add link to ansible doc]

.. code-block:: text

    [defaults]
    roles_path = /etc/ansible/roles/:../ravello-ansible/roles

.. IMPORTANT::
  When you define the variable roles_path you need to redefine the default location as well

Install python dependancies
---------------------------

.. code-block:: text

    pip install requests httplib2

Define Ravello credentials
--------------------------

It's mandatory to provide your ravello credentials.
It's recommanded to create a variable file dedicated for that under the ``group_vars/all`` directory

.. code-block:: yaml

    # group_vars/all/credentials.yaml
    ravello_login_username: user@email.com
    ravello_login_password: xxxyyy
