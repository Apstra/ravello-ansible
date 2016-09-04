#!/usr/bin/env python

# Copyright (c) 1999-2016, Juniper Networks Inc.
#
# All rights reserved.
#
# License: Apache 2.0
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# * Neither the name of the Juniper Networks nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Juniper Networks, Inc. ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Juniper Networks, Inc. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

DOCUMENTATION = '''
---

'''

EXAMPLES = '''
   dest: "{{ inventory_hostname }}.xml"
   format: xml
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
            appId = dict(required = True, default = None),
            baseVmId = dict(required = True, default = None),
            user = dict(required = True, default = None),
            password = dict(required = True, default = None),
        ),
        supports_check_mode = True
    )

    results = dict(changed=False)

    args = module.params
    url = "https://cloud.ravellosystems.com/api/v1/applications/" + str(args['appId']) + "/vms"
    headers = {"Accept" : "application/json", "Content-Type" : "application/json"}
    data = {"baseVmId" : args['baseVmId'] }
    r = requests.post(url,
        auth = (args['user'], args['password']),
        headers = headers,
        json = data
    )

    ## TODO Add check for return code from server

    json = r.json()
    vms = json['design']['vms']
    creationTime = 0
    returnVm = None
    for vm in vms:
        if creationTime < vm['creationTime']:
            creationTime = vm['creationTime']
            returnVm = vm

    if returnVm == None:
        module.fail_json(msg = "Unable to identify the newly added VMs")

    results['changed'] = True
    results['msg'] = returnVm
    module.exit_json(**results)

if __name__ == "__main__":
    main()
