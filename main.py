#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apherache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import webapp2

from sys import argv, exit
from helpers import alphabet_position, rotate_character
from caesar2 import encrypt

form = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Caesar Cipher</title>

        <style type="text/css">
            #lay {margin-top: 20px; margin-left: 20px; background-color: #F0FFFF;}
            input {border: none; background-color: #f2f2f2; margin-left: 10px; margin-bottom: 30px; padding-right: 50px;}
            label{
            display:inline-block;
            width:50px;
            }
        </style>

    </head>

    <body>
        <div id="lay">
        <h2>Caesar Cipher</h2>

        <form method = "post">

        <label>
            <h3>Rotation:</h3>
            <input type= "number" name="roty" size="10" value="%(rot)s">
        </label>
        <br>
        <br>

        <label>
            <h3>Text:</h3>
                <textarea name="old_text"  cols="75" rows="7">%(scram)s</textarea>
        </label>
        <br>
        <br>
        <input type = "submit">
        </form>
        </div>
    </body>
</html>
"""



class MainHandler(webapp2.RequestHandler):
#    def write_form(self, rot="", scram=""):
#        self.response.write()

    def get(self):
        self.response.write(form % {'scram': "" ,'rot': ""})

    def post(self):
        old_text = self.request.get("old_text")
        roty = self.request.get("roty")
        rot = int(roty)
        scram = encrypt(old_text, rot)
        self.response.write(form % {"rot": rot, "scram": scram})


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
