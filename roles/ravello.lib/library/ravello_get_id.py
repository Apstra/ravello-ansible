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
      resource_type = dict(required=True, default = None,
                           choices=['applications',
                                    'blueprint',
                                    'images',
                                    'vms',
                                    'keypair']),
      resource_name = dict(required = True, default = None),
      application_id = dict(required = False, default = None),
      failed_if_not_found = dict(required=False, type='bool', default = False),
    ),
    supports_check_mode = False
  )

  args = module.params
  url = ""

  if args['resource_type'] == 'vms' and args['application_id']:
    url = "https://cloud.ravellosystems.com/api/v1/{0}/vms/{1}".format(args['application_id'], args['resource_type'])
  else:
    url = "https://cloud.ravellosystems.com/api/v1/{0}".format(args['resource_type'])

  headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
  r = requests.get(url,
    auth = (args['user'], args['password']),
    headers = headers,
  )

  resp = dict(found=False)

  if r.status_code != 404:
      resources = r.json()

      for resource in resources:
          if 'name' in resource.keys():
              if resource['name'] == args['resource_name']:
                 resp['found'] = True
                 resp['json'] = resource
                 module.exit_json(**resp)

      if args['failed_if_not_found']:
        module.fail_json(msg = "Unable to find the {0} named '{1}' in Ravello, please check if the App exist".format(args['application_type'], args['application_name']))

  module.exit_json(**resp)

if __name__ == "__main__":
    main()
