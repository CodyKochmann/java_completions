# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-08-01 12:35:54
# @Last Modified 2016-08-01
# @Last Modified time: 2016-08-01 13:06:44

import os
import json

if __file__.split('/')[-1] not in os.listdir('./'):
    print 'wrong directory'
    exit()

for i in os.listdir('./'):
    if i.endswith('.java.sublime-snippet'):
        os.remove(i)

data = {}

with open('keywords.json','r') as f:
    data = json.loads(f.read())

def write_file(file_path,txt):
    with open(file_path, 'w') as f:
        f.write(txt)

class KeywordSnippet():
    def __init__(self, keyword, type_description):
        self.keyword = keyword
        self.type_description = type_description
        self.snippet_text = '''<snippet>
    <content>{}</content>
    <!-- Optional: Tab trigger to activate the snippet -->
    <tabTrigger>{}</tabTrigger>
    <!-- Optional: Scope the tab trigger will be active in -->
    <scope>source.java</scope>
    <!-- Optional: Description to show in the menu -->
    <description>{}</description>
</snippet>'''.format(
            self.keyword,
            self.keyword,
            self.type_description
        )
        self.file_path = '{}.java.sublime-snippet'.format(self.keyword)

for t in data:
    for keyword in data[t].split(' '):
        s = KeywordSnippet(keyword, t)
        print '========================================================'
        print s.file_path
        print s.snippet_text
        write_file(s.file_path, s.snippet_text)
