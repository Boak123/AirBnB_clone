#!/usr/bin/python3
""" Class cty that inherits from base model"""

import models
from models.base_model import BaseModel


class City(BaseModel):
    """ Class state that inherits from base model """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
super().__init__(self, *args, **kwargs)
