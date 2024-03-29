urllib.request is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. These are provided by objects called handlers and openers.
The simplest way to use urllib.request is as follows:

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

This is just an introduction, more is coming
