#!/usr/bin/env ruby

require 'sinatra'

color = ENV['PIKA_COLOR'] || '#00a3ff'

set :bind, '0.0.0.0'
set :port, 8080

get '/' do
  body = '<html><head><title>PyKubachu</title></head>'
  body += '<body style="background:'+color+';margin: 0px;">'
  body += '<img src="/images/pykubachu.png"/>'
  body += '</body></html>'
  body
end

get '/images/:filename' do
  send_file File.expand_path("images/#{params['filename']}", __dir__)
end
