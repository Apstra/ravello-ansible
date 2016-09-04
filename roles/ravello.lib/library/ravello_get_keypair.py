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
      keypair_name = dict(required = True, default = None),
    ),
    supports_check_mode = False
  )

  args = module.params
  url = "https://cloud.ravellosystems.com/api/v1/keypairs"
  headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
  r = requests.get(url,
    auth = (args['user'], args['password']),
    headers = headers,
  )

  keypairs = r.json()

  for key in keypairs:
      if 'name' in key.keys():
          if key['name'] == args['keypair_name']:
             module.exit_json(json = key)

  module.fail_json(msg = "Unable to find the Key Pair named {0} in Ravello, please check if the Key Pair exist".format(args['keypair_name']))

if __name__ == "__main__":
    main()
