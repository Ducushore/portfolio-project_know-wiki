from django.db import models


# Create a model for the JOB app, and then we will connect it with the DB

class Job(models.Model):
    #  https://docs.djangoproject.com/en/3.1/ref/models/fields/ - details about what Field Types are available, e.g. :
    image = models.ImageField(upload_to='images/')  # located in an "media" folder
    summary = models.CharField(max_length=200)  # summary Field Type is kind of an description
