import markdown
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    image = models.ImageField(upload_to='news/')
    content = models.TextField(help_text="Write content in Markdown format")
    content_html = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.content_html = markdown.markdown(self.content, extensions=['extra'])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
