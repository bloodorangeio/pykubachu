#!/usr/bin/env python3

import os
import sys
from kubernetes import client, config

NAME = os.environ.get('NAME', 'pykubachu')
NAMESPACE = os.environ.get('NAMESPACE', 'chipy')

def update_pykubachu(color):
    config.load_kube_config()
    extensions_v1beta1 = client.ExtensionsV1beta1Api()

    deployment = extensions_v1beta1.read_namespaced_deployment(
        name=NAME,
        namespace=NAMESPACE)

    deployment.spec.template.spec.containers[0].env[0].value = color
    api_response = extensions_v1beta1.patch_namespaced_deployment(
        name=NAME,
        namespace=NAMESPACE,
        body=deployment)

    print("Deployment updated. status='%s'" % str(api_response.status))

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Usage: ./pykuybachu-admin.py <color>')
        sys.exit(1)

    color = args[1]
    update_pykubachu(color)
