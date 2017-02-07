#!/usr/bin/python
# encoding: utf-8

import json
import urllib2

class Workflow:

  def __init__(self):
    self.items = json.loads('{"items":[]}')
    self.length = 0

  def get_result_from_url(self, url, encoding='utf-8'):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    response = urllib2.urlopen(request)
    result = response.read().decode(encoding)
    return result

  def add_item(self, title, subtitle='', arg='', autocomplete='', valid='yes', icon=''):
    self.items['items'].insert(self.length, {
          "uid" : self.length,
          "title" : title,
          "subtitle" : subtitle,
          "arg" : arg,
          "autocomplete" : autocomplete,
          "valid" : valid,
          "icon" : {
              "type" : "png",
              "path" : icon
            }
        })
    self.length += 1

  def __str__(self):
    return json.dumps(self.items)
