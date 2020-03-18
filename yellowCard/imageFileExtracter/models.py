from django.db import models

class ImageFile(models.Model):
    image = models.ImageField(blank=False, null=False)
    text=models.TextField()
    def __str__(self):
        return self.file.name