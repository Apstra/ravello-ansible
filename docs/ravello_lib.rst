Library of modules (ravello.lib)
================================

This role is a library of small Ansible modules to help interact with the Ravello API

ravello_addvm
-------------

Add a new VM to an existing application and return the newly created VM

.. code-block:: yaml

    ravello_addvm:
      appId: "{{ app.json.id }}"
      baseVmId: "{{ image.json.baseVmId }}"
      user: "{{ login.username }}"
      password: "{{ login.password }}"

ravello_get_id
---------------

Retrieve the ID of several resources based on its name

.. code-block:: yaml

    # Get Application Id
    ravello_get_id:
      resource_name: "my-application"
      resource_type: applications
      user: "{{ login.username }}"
      password: "{{ login.password }}"

    # Get Image Id
    ravello_get_id:
      resource_name: "my-image"
      resource_type: image
      user: "{{ login.username }}"
      password: "{{ login.password }}"

    # Get Blueprint Id
    ravello_get_id:
      resource_name: "my-blueprint"
      resource_type: blueprints
      user: "{{ login.username }}"
      password: "{{ login.password }}"

    # Get VM Id
    ravello_get_id:
      resource_type: vms
      application_id: "{{ application_id }}"
      resource_name: "vm_name"
      user: "{{ ravello_login_username }}"
      password: "{{ ravello_login_password }}"

    # Get keypair Id
    ravello_get_id:
      resource_name: "my-keypair"
      resource_type: keypairs
      user: "{{ login.username }}"
      password: "{{ login.password }}"
