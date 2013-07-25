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
require 'uri'
require 'net/http'
require 'net/https'

# set variables
rowid = 'INSERT_ROW_ID_HERE'
filename = "screenshot-of-smartsheet.png"
# determine file size, in Kb
filesize = File.size(filename)

# upload file
puts "Uploading file #{filename}, size #{filesize} to row #{rowid}..."

data = File.read(filename)
url = URI.parse("https://api.smartsheet.com/1.1/row/#{rowid}/attachments")
req = Net::HTTP.new(url.host, url.port)
req.use_ssl = true
headers = {
  "Authorization" => "Bearer INSERT_YOUR_TOKEN_HERE",
  "Content-Type" => "image/png",
  "Content-Length" => "#{filesize}",
  "Content-Disposition" => "attachment; filename=\"#{filename}\""
}

response, body = req.post(url.path, data, headers)
puts
puts "Response: #{response.code} #{response.message}"
puts
puts "Response body: #{response.body}"

puts "File #{filename} uploaded to row #{rowid}."
puts
