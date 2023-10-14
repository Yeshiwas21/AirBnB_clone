from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            self.load_from_dict(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.today()
            models.storage.new(self)

    def load_from_dict(self, data):
        """Load attributes from a dictionary."""
        for key, value in data.items():
            if key in ["created_at", "updated_at"]:
                setattr(self, key, datetime.strptime(value, self.DATE_FORMAT))
            else:
                setattr(self, key, value)

    def save(self):
        """Update updated_at with the current datetime and save the object."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        return {
            "id": self.id,
            "created_at": self.created_at.strftime(self.DATE_FORMAT),
            "updated_at": self.updated_at.strftime(self.DATE_FORMAT),
            "__class__": self.__class__.__name__,
            **self.__dict__
        }

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        class_name = self.__class__.__name
        return f"[{class_name}] ({self.id}) {self.__dict__}"