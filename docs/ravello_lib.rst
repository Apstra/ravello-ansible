Library of modules (ravello.lib)
================================

This role is a library of small Ansible modules to help interact with the Ravello API

ravello_addvm
--------------

Add a new VM to an existing application and return the newly created VM

.. code-block:: yaml

    ravello_addvm:
      appId: "{{ app.json.id }}"
      baseVmId: "{{ image.json.baseVmId }}"
      user: "{{ login.username }}"
      password: "{{ login.password }}"

ravello_get_app
---------------

Retrieve the ID of an application based on its name

.. code-block:: yaml

    ravello_get_app:
      application_name: "{{ ravello.app_name }}"
      user: "{{ login.username }}"
      password: "{{ login.password }}"

ravello_get_image
-----------------

Retrieve the ID of an image based on its name

.. code-block:: yaml

    ravello_get_image:
      image_name: "{{ ravello_image }}"
      user: "{{ login.username }}"
      password: "{{ login.password }}"


ravello_get_keypair
-------------------

Retrieve the ID of a key pair based on its name

.. code-block:: yaml

    ravello_get_keypair:
      keypair_name: "{{ ravello_key_pair }}"
      user: "{{ login.username }}"
      password: "{{ login.password }}"

ravello_get_vm
--------------

Retrieve the ID of a VM based on its name

.. code-block:: yaml

    ravello_get_vm:
      application_id: "{{ app.json.id }}"
      vm_name: "{{ inventory_hostname }}"
      user: "{{ login.username }}"
      password: "{{ login.password }}"
