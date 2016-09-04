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
      application_name = dict(required = True, default = None),
    ),
    supports_check_mode = False
  )

  args = module.params
  url = "https://cloud.ravellosystems.com/api/v1/applications"
  headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
  r = requests.get(url,
    auth = (args['user'], args['password']),
    headers = headers,
  )

  apps = r.json()

  for app in apps:
      if 'name' in app.keys():
          if app['name'] == args['application_name']:
             module.exit_json(json = app)

  module.fail_json(msg = "Unable to find the Application named '{0}' in Ravello, please check if the App exist".format(args['application_name']))

if __name__ == "__main__":
    main()
