#!/usr/bin/python3
"""__init__ file containing storage variable"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
