#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def learn(self,new_skill):
        self._knowledge.append(new_skill)