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
      blueprint_name = dict(required = True, default = None),
    ),
    supports_check_mode = False
  )

  args = module.params
  url = "https://cloud.ravellosystems.com/api/v1/blueprints"
  headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
  r = requests.get(url,
    auth = (args['user'], args['password']),
    headers = headers,
  )

  blueprints = r.json()

  for bp in blueprints:
      if 'name' in bp.keys():
          if bp['name'] == args['blueprint_name']:
             module.exit_json(json = bp)

  module.fail_json(msg = "Unable to find the Blueprint named {0} in Ravello, please check if the Blueprint exist".format(args['blueprint_name']))

if __name__ == "__main__":
    main()
