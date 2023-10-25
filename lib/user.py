#!/usr/bin/env python

class User:
    def __init__(self,first_name,last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._knowledge = []

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def knowledge(self):
        return self._knowledge