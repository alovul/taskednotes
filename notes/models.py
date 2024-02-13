from django.db import models


class Notelist(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        """Returns a string representation of a message."""
        return f"'{self.name}' logged on"
    