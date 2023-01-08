from django.db import models


class School(models.Model):
    name = models.CharField(max_length=120)

    # What I get when I call the class object
    def __str__(self):
        return self.name
