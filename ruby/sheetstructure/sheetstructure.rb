#!/usr/bin/env ruby
=begin
  Smartsheet Platform sample code
  sheetstructure.rb (Ruby)

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

# define httparty class
class Smartsheet
  include HTTParty
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
puts "Starting sheetstructure.rb: Betty's Bake Sale..."
puts

# create sheet
sheet_name = "Betty's Bake Sale"
puts "Creating sheet #{sheet_name}..."
options = {
  headers: { 'Content-Type' => 'application/json' },
  body: {
    name: sheet_name,
    columns: [
      { title: "Baked Good", type: "TEXT_NUMBER", primary: true },
      { title: "Baker", type: "CONTACT_LIST" },
      { title: "Price Per Item", type: "TEXT_NUMBER" },
      { title: "Gluten Free?", type: "CHECKBOX", symbol: "FLAG" },
      { title: "Status", type: "PICKLIST", options: ["Started", "Finished", "Delivered"] }
    ] 
  }.to_json
}
body = ss_connection.request('post', '/sheets', options)
sheet_id = body['result']['id']
puts "Sheet #{sheet_name} created, id: #{sheet_id}."
puts

# add column
column_name = "Delivery Date"
puts 'Adding a column #{column_name} to #{sheet_name} sheet...'
options = {
  headers: { 'Content-Type' => 'application/json' },
  body: {
    index: 5, title: column_name, type: "DATE"
  }.to_json
}
body = ss_connection.request('post', "/sheet/#{sheet_id}/columns", options)
puts "Column #{column_name} added, id: #{body['result']['id']}."
puts

# add rows
# fetch sheet columns
puts "Fetching #{sheet_name} sheet columns..."
sheet_columns = ss_connection.request('get', "/sheet/#{sheet_id}/columns")
puts "Fetched."
puts

# insert rows
puts "Inserting rows into #{sheet_name}..."
options = {
  headers: { 
    'Content-Type' => 'application/json'
  },
  body: {
    toBottom: true,
    rows: [
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Brownies" },
        { columnId: sheet_columns[1]['id'], value: "julieanne@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$1", strict: false },
        { columnId: sheet_columns[3]['id'], value: true },
        { columnId: sheet_columns[4]['id'], value: "Finished" }
      ]},
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Snickerdoodles" },
        { columnId: sheet_columns[1]['id'], value: "stevenelson@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$1", strict: false },
        { columnId: sheet_columns[3]['id'], value: false },
        { columnId: sheet_columns[4]['id'], value: "Delivered" },
        { columnId: sheet_columns[5]['id'], value: "2013-09-04" }
      ]},
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Rice Krispy Treats" },
        { columnId: sheet_columns[1]['id'], value: "rickthames@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$.50", strict: false },
        { columnId: sheet_columns[3]['id'], value: false },
        { columnId: sheet_columns[4]['id'], value: "Started" }
      ]},
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Muffins" },
        { columnId: sheet_columns[1]['id'], value: "sandrassmart@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$1.50", strict: false },
        { columnId: sheet_columns[3]['id'], value: false },
        { columnId: sheet_columns[4]['id'], value: "Finished" }
      ]},
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Chocolate Chip Cookies" },
        { columnId: sheet_columns[1]['id'], value: "janedaniels@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$1", strict: false },
        { columnId: sheet_columns[3]['id'], value: false },
        { columnId: sheet_columns[4]['id'], value: "Delivered" },
        { columnId: sheet_columns[5]['id'], value: "2013-09-05" }
      ]},
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Ginger Snaps" },
        { columnId: sheet_columns[1]['id'], value: "nedbarnes@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$.50", strict: false },
        { columnId: sheet_columns[3]['id'], value: true },
        { columnId: sheet_columns[4]['id'], value: "Unknown", strict: false }
      ]}
    ]
  }.to_json
}
rows1 = ss_connection.request('post', "/sheet/#{sheet_id}/rows", options) 
puts "Added #{rows1['result'].length} rows to #{sheet_name}."
puts

# move row
puts "Moving row 6 to top..."
options = {
  headers: { 'Content-Type' => 'application/json' },
  body: {
      toTop: true
  }.to_json
}
body = ss_connection.request('put', "/row/#{rows1['result'][5]['id']}", options) 
puts "Row 6 moved to top."
puts

# insert empty separator row + Delivered section header
puts "Inserting separator + Delivered section header rows..."
options = {
  headers: { 
    'Content-Type' => 'application/json'
  },
  body: {
    toBottom: true,
    rows: [
      { cells: [ { columnId: sheet_columns[0]['id'], value: "" } ]},
      { cells: [ { columnId: sheet_columns[0]['id'], value: "Delivered:" } ]}
    ]
  }.to_json
}
rows2 = ss_connection.request('post', "/sheet/#{sheet_id}/rows", options) 
puts "Added #{rows2['result'].length} rows to #{sheet_name}."
puts

# move delivered items to delivered section
delivered_header_id = rows2['result'][1]['id']
delivered_row_ids = [ rows1['result'][1]['id'], rows1['result'][4]['id'] ]
delivered_row_ids.each {|id|
  puts "Moving row id #{id} to Delivered..."
  options = {
    headers: { 'Content-Type' => 'application/json' },
    body: { parentId: delivered_header_id }.to_json
  }
  body = ss_connection.request('put', "/row/#{id}", options) 
  puts "Row id #{id} moved."
  puts
}

# append more items as siblings of muffins
puts "Appending additional rows to items in progress..."
sibling_id = rows1['result'][3]['id']
options = {
  headers: { 
    'Content-Type' => 'application/json'
  },
  body: {
    siblingId: sibling_id,
    rows: [
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Scones" },
        { columnId: sheet_columns[1]['id'], value: "tomlively@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$1.50", strict: false },
        { columnId: sheet_columns[3]['id'], value: true },
        { columnId: sheet_columns[4]['id'], value: "Finished" }
      ]},
      { cells: [
        { columnId: sheet_columns[0]['id'], value: "Lemon Bars" },
        { columnId: sheet_columns[1]['id'], value: "rickthames@example.com", strict: false },
        { columnId: sheet_columns[2]['id'], value: "$1", strict: false },
        { columnId: sheet_columns[3]['id'], value: false },
        { columnId: sheet_columns[4]['id'], value: "Started" }
      ]}
    ]
  }.to_json
}
body = ss_connection.request('post', "/sheet/#{sheet_id}/rows", options) 
puts "Added #{body['result'].length} rows to #{sheet_name}."
puts

# move Status column to index 1
puts "Moving Status column to index 1..."
status_column = sheet_columns.detect{|c| c['title'] == 'Status'}
options = {
  headers: { 'Content-Type' => 'application/json' },
  body: { 
    sheetId: sheet_id,
    index: 1,
    title: status_column['title']
  }.to_json
}
body = ss_connection.request('put', "/column/#{status_column['id']}", options) 
puts "Column id #{status_column['id']} moved to index 1."
puts

puts "Completed sheetstructure.rb: Betty's Bake Sale."
puts
