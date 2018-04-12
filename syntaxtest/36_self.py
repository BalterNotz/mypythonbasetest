#!/usr/bin/env python
# Python3

class Demo(Iterable):

    def setValue(self, key, value):
        if key not in self:
            self[key] = value
        return self[key]


demo = Demo()
print(demo)
print(demo.setValue("abc", "def"))
