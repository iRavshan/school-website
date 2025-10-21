from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = RichTextField(null=False)
    published_date = models.DateTimeField(auto_now_add=True, auto_created=True)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)