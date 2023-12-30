# models/base_model.py
from datetime import datetime
import uuid
from models import storage  # Import storage locally within methods

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

    def save(self):
        storage.new(self)  # Use storage.new() instead of storage.new(self)
        storage.save()

