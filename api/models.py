from uuid import uuid4

from django.db import models

# Create your models here.


class TinyUrl(models.Model):
    url = models.CharField(max_length=255)
    code = models.CharField(max_length=6, null=True, blank=True, unique=True)

    def _get_unique_id(self):
        uuid_code = self.generate_id()
        while TinyUrl.objects.filter(code=uuid_code).exists():
            uuid_code = self.generate_id()

        return uuid_code

    @staticmethod
    def generate_id():
        return str(uuid4())[:5]

    def save(self, *args, **kwargs):
        self.code = self._get_unique_id()
        super(TinyUrl, self).save(*args, **kwargs)
