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
      image_name = dict(required = True, default = None),
    ),
    supports_check_mode = False
  )

  args = module.params
  url = "https://cloud.ravellosystems.com/api/v1/images"
  headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
  r = requests.get(url,
    auth = (args['user'], args['password']),
    headers = headers,
  )

  ## TODO Add check for return code from server

  images = r.json()

  for image in images:
      if 'name' in image.keys():
          if image['name'] == args['image_name']:
             module.exit_json(json = image)

  module.fail_json(msg = "Unable to find the VM named {0} in Ravello, please check if the VM exist".format(args['image_name']))

if __name__ == "__main__":
    main()
