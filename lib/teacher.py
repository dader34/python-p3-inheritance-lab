#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self,first_name="",last_name=""):
        super().__init__(first_name,last_name)
        self._knowledge =[1]

    def teach(self):
        return 1