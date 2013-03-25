#!/usr/bin/env python

"""
Wavedrom markdown filter
========================

- Copyright (c) 2013 Chris Higgs
    - Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

## Format

![[waveform.json]]

Where waveform.json is a file containing the JSON formatted waveform

"""


import markdown
from markdown.util import etree

class WavedromExtension(markdown.Extension):
  """ Wavedrom Extension for Python-Markdown. """

  def add_inline(self, md, name, pattern_class, pattern):
    """
    Add new functionality to the Markdown instance.

    Keyword arguments:
    * md: The Markdown instance.
    * md_globals: markdown's global variables.
    """
    objPattern = pattern_class(pattern, self.config)
    objPattern.md = md
    objPattern.ext = self
    md.inlinePatterns.add(name, objPattern, "<reference")

  def extendMarkdown(self, md, md_globals):
    self.add_inline( md, "wavedrom", WavedromPattern, r'\!\[\[(.*)\]\]')

class WavedromPattern(markdown.inlinepatterns.Pattern):
  def __init__(self, pattern, config):
    self.pattern = pattern
    self.config = config
    markdown.inlinepatterns.Pattern.__init__(self, pattern)

  def getCompiledRegExp(self):
    import re
    return re.compile(self.pattern)

  def handleMatch(self, match):

    if match :

      wavedromURL = str(match.group(1))

      with open(wavedromURL, 'r') as f:
          waveform = f.read()


      div = etree.Element("p")
      
      script = etree.SubElement(div, 'script')
      script.set("src", "http://wavedrom.googlecode.com/svn/trunk/skins/default.js")
      script.set("type","text/javascript")

      script2 = etree.SubElement(div, 'script')
      script2.set("src", "http://wavedrom.googlecode.com/svn/trunk/WaveDrom.js")
      script2.set("type","text/javascript")
      
      script3 = etree.SubElement(div, 'script')
      script3.set("type","WaveDrom")
      script3.text = markdown.util.AtomicString(waveform)     
      

      return div
    else :
      return ""

def makeExtension(configs=None):
  return WavedromExtension(configs=configs)

if __name__ == "__main__":
    import doctest
    print doctest.testmod()
    print "-" * 8
    md = markdown.Markdown(extensions=['wavedrom'])
    print md.convert( __doc__ )

