#!/usr/bin/env python
"""API connector base class definition."""


class Connector(object):

  @property
  def page_size(self):
    raise NotImplementedError()

  def SendRequest(self, handler_name, args):
    raise NotImplementedError()

  def SendStreamingRequest(self, handler_name, args):
    raise NotImplementedError()
