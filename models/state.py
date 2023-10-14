#!/usr/bin/python3
""" Class state that inherits from base model"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Class Stae that inherits from base model """
    name = ""

    # def __init__(self, *args **kwargs):
    #     """ Constructor """
    #     Super().__init__(self, *args, **kwargs)
