#!/usr/bin/env ruby
=begin
  Smartsheet Platform sample code
  attachments.rb (Ruby)

   Copyright 2013 Smartsheet, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
=end

# load third-party libraries and extensions
require 'httparty'
require 'active_support/core_ext/hash/deep_merge'
require 'json'

# as is, httparty does not allow file uploads - enable file uploads via httparty
module HTTParty
  class Request
    private

    def setup_raw_request
      @raw_request = http_method.new(request_uri(uri))
      if body
        if body.respond_to?(:read)
          @raw_request.body_stream = body
        else
          @raw_request.body = body
        end
      end
      @raw_request.initialize_http_header(options[:headers])
      @raw_request.basic_auth(username, password) if options[:basic_auth]
      setup_digest_auth if options[:digest_auth]
    end

  end
end

# define httparty class
class Smartsheet
  include HTTParty
  #debug_output $stderr
  base_uri 'https://api.smartsheet.com/1.1'
 
  # initialize httparty object
  def initialize(token)
    @auth_options = {headers: {"Authorization" => 'Bearer ' + token}}
  end

  def request(method, uri, options={})
    # merge headers
    options.deep_merge!(@auth_options)

    # process response
    puts "* requesting #{method.upcase} #{uri}"
    response = self.class.send(method, uri, options)
    json = JSON.parse(response.body)

    # if response is anything other than HTTP 200, print error and quit
    if response.code.to_s !~ /^2/
      puts "* fatal error: #{json['errorCode']}: #{json['message']}"
      exit 
    end

    return json
  end
end

# Smartsheet API access token
ss_token = 'INSERT_YOUR_TOKEN_HERE'

# initializing Smartsheet connection object
ss_connection = Smartsheet.new(ss_token)

puts
puts "Starting attachments.rb..."
puts

# create sheet
sheet_name = "Attachments"
puts "Creating sheet #{sheet_name}..."
options = {
  headers: { 'Content-Type' => 'application/json' },
  body: {
    name: sheet_name,
    columns: [
      { title: "Attachment name", type: "TEXT_NUMBER", primary: true },
      { title: "Type", type: "PICKLIST", options: ["File", "URL"] },
      { title: "Uploaded?", type: "CHECKBOX", symbol: "FLAG" }
    ] 
  }.to_json
}
body = ss_connection.request('post', '/sheets', options)
sheet_id = body['result']['id']
puts "Sheet #{sheet_name} created, id: #{sheet_id}."
puts


# insert rows
puts "Inserting rows into #{sheet_name}..."

# fetch sheet columns
puts "Fetching #{sheet_name} sheet columns..."
sheet_columns = ss_connection.request('get', "/sheet/#{sheet_id}/columns")
puts "Fetched."
puts

options = {
  headers: { 
    'Content-Type' => 'application/json'
  },
  body: {
    toBottom: true,
    rows: [
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Smartsheet attachments 1" },
        { columnId: sheet_columns[1]['id'], value: "File" },
        { columnId: sheet_columns[2]['id'], value: false }
      ]},
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Smartsheet attachments 2" },
        { columnId: sheet_columns[1]['id'], value: "URL" },
        { columnId: sheet_columns[2]['id'], value: false }
      ]}
    ]
  }.to_json
}
rows1 = ss_connection.request('post', "/sheet/#{sheet_id}/rows", options) 
puts "Added #{rows1['result'].length} rows to #{sheet_name}."
puts


# attach file
filename = "screenshot-of-smartsheet.png"
# determine file size, in Kb
filesize = File.size(filename)
puts "Attaching file #{filename}, size #{filesize} to top row ..."

options = {
  headers: {
    'Content-Disposition' => "attachment; filename=\"#{filename}\"",
    'Content-Type' => 'image/png',
    'Content-Length' => "#{filesize}"
  },
  body: File.open(filename, 'r')
}
attached_file = ss_connection.request('post', "/row/#{rows1['result'][0]['id']}/attachments", options) 
puts "File #{filename} attached to top row."
puts


# attach URL
link = "http://smartsheet.com"
puts "Attaching URL #{link} to bottom row ..."

options = {
  headers: { 
    'Content-Type' => 'application/json'
  },
  body: {
    name: "Smartsheet",
    description: "Smartsheet website",
    attachmentType: "LINK",
    url: link 
  }.to_json
}
attached_url = ss_connection.request('post', "/row/#{rows1['result'][1]['id']}/attachments", options) 
puts "URL #{link} attached to top row."
puts


# download file
attached_file_id = attached_file['result']['id']
attached_file_name = attached_file['result']['name']
puts "Getting attachment object for #{attached_file_name} ..."
attached_file_object = ss_connection.request('get', "/attachment/#{attached_file_id}")
puts "Downloading attachment #{attached_file_name} ..."
File.open("attached_file_contents", "w") do |stream|
  stream << HTTParty.get(attached_file_object['url'])
end
puts "Downloaded attachment to local file attached_file_contents."
puts


# delete file
puts "Deleting attached file #{filename} from top row ..."
ss_connection.request('delete', "/attachment/#{attached_file_id}") 
puts "Deleted attached file #{filename} from top row."
puts


puts "Completed attachments.rb."
puts
