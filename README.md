![status experimental](https://img.shields.io/badge/status-experimental-yellow.svg)

# Ravello Ansible

Collection of Ansible roles to programmatically interact with Ravello

With these roles, it's possible to:
- Create an application dynamically
- Start VM
- Delete an application
- Collect all public IP addresses

# How to use these roles

You can reference to this project for an example: [https://github.com/dgarros/rav-ipfabric-demo](https://github.com/dgarros/rav-ipfabric-demo)

# Docker container

A docker container `juniper/ravello-ansible` is provided to easily use this project.   
By default working directory for the container is `/project`, if you mount it you can use the container directly on your local project

```
docker run -t -i -v $(pwd):/project juniper/ravello-ansible ansible-playbook -i <inventory> <playbook>
```

# Documentation

Please, visit the [main documentation](http://ravello-ansible.readthedocs.io)
