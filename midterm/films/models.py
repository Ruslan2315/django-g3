from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    duration = models.IntegerField()

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)
