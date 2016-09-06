Role - Create application (ravello.application_create)
======================================================

This role will create automatically an application on Ravella based on your ansible project.
By default, each host in the Ansible inventory will be converted into a VM on ravello.

.. NOTE::
  Most of the execution is done **Per host/VM** as per Ansible principle. As a results,
  it's possible to control which VM will be created by limiting the execution using ``--limit``

Define your VM
---------------

For each, VM you want to define the name of the base image to use.
This operation is done by using the variable ``ravello_image``
The value of this variable but match exactly the name of a VM in your inventory.

Below an example where the variable is defined in the inventory file directly

.. code-block:: text

    [spine]
    spine1     mgmt_ip=10.0.0.11   id=11
    spine2     mgmt_ip=10.0.0.21   id=21

    [spine:vars]
    ravello_image=vqfx10k-re-15.1X53-D60

Define your physical layout
----------------------------

To define your physical topology,
you need to provide the mapping for each interface of each VM in the variable ``ravello_topology``.

For each VM:
- The name need to match the name defined in the inventory
- The interface mapping needs to be define in order as a list starting from the first interface.

For each interface, you need to provide a dict to indicate where the interface should be connected.
A L1 link is defined by an ``ID``, if you want to connect 2 interfaces together, you need to assign them the same ``ID``

.. code-block:: yaml

    link: "link_id" or "dhcp-public"
    type: (optional) [virtio, default etc ..]

.. NOTE::
  it's possible to connect more than 2 interfaces together by assigning the same ID to more than 2 interfaces


Example:

.. code-block:: yaml

    ravello_topology:
      leaf1:
        - link: dhcp-public
        - link: 91
        - null
        - link: 11

      leaf2:
        - link: dhcp-public
        - link: 92
        - null
        - link: 11
        - link: 12
        - link: 13



Create the playbook
-------------------

Execution
---------

The Ravello API doesn't allow multiple concurrents that are doing modification for the same application.
So to avoid any issue due to Ansible paralelle execution, you need to reduce the number of fork to 1 using ``--forks=1``

.. code-block:: text

    ansible-playbook pb.rav.create.yaml --forks=1

It's possible to limit the execution of the playbook to a subset of VMs

.. code-block:: text

    ansible-playbook pb.rav.create.yaml --forks=1 --limit=leaf
