#!/usr/bin/python3
''' Models package initializer module '''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
