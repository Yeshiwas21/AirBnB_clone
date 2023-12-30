#!/usr/bin/python3
"""Empty module to initialize package."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
