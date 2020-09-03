# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:36:46 2020

@author: Ronin
"""

class Item:
    def __init__(self,name,description,value=0):
        self.name = name
        self.description = description
        self.value = int(value)