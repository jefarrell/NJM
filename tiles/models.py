from django.db import models
from django.utils import timezone
import datetime
from stdimage.models import StdImageField
from django.template.defaultfilters import slugify


class ProfileImage(models.Model):
    image = StdImageField(upload_to='%Y/%m/%d', blank=True)
    date = models.DateTimeField(auto_now=True, blank=True, default=datetime.date.today())
    description = models.TextField(max_length=20000, blank=True)
    title = models.TextField(max_length=200, blank=True)
    weblink = models.TextField(max_length=200, blank=True)


    slug = models.SlugField()

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.description[:20])

        super(ProfileImage, self).save(*args, **kwargs)
