from django.db import models

class Articles(models.Model):
    article_name = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    document = models.FileField(upload_to='uploads/')
    status = models.BooleanField(default=False)