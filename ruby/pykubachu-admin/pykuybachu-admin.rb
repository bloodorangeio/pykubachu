#!/usr/bin/env ruby

require 'kubeclient'

tag = ARGV[0]

config = Kubeclient::Config.read(ENV['KUBECONFIG'])
context = config.context
ssl_options = context.ssl_options
auth_options = context.auth_options

client = Kubeclient::Client.new(
    context.api_endpoint, 'v1',
    ssl_options: ssl_options, auth_options: auth_options
)

for pod in client.get_pods do
    c1 = pod.spec.containers[0]
    if c1.name == "pykubachu"
        c1.image = "bloodorangeio/pykubachu:#{tag}"
        client.update_pod(pod)
    end
end
