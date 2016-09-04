#!/usr/bin/env python

DOCUMENTATION = '''
---

'''

EXAMPLES = '''

'''
from distutils.version import LooseVersion
from ansible.module_utils.basic import *
import logging
import json
import requests
import httplib2

def main():

  module = AnsibleModule(
    argument_spec = dict(
      user = dict(required = True, default = None),
      password = dict(required = True, default = None),
      vm_name = dict(required = True, default = None),
      application_id = dict(required = True, default = None),
    ),
    supports_check_mode = False
  )

  args = module.params
  url = "https://cloud.ravellosystems.com/api/v1/applications/{0}/vms".format(args['application_id'])
  headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
  r = requests.get(url,
    auth = (args['user'], args['password']),
    headers = headers,
  )

  vms = r.json()

  for vm in vms:
      if 'name' in vm.keys():
          if vm['name'] == args['vm_name']:
             module.exit_json(json = vm)

  module.fail_json(msg = "Unable to find the VM named '{0}' in the Application {1} Ravello, Please check if the App exist".format(args['vm_name'], args['application_id']))

if __name__ == "__main__":
    main()
