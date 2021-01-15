from django.db import models


# Create A BLOG Model :
# title
# publication_date
# body
# image

# Create a model for the BLOG app, and then we will connect it with the DB
class Blog(models.Model):
    #  https://docs.djangoproject.com/en/3.1/ref/models/fields/ - details about what Field Types are available, e.g. :
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')  # located in the "media" folder

# Add the BLOG app to the settings
# 'blog.apps.BlogConfig',

# Create a MIGRATION

# MIGRATE

# Add the app to the ADMIN
