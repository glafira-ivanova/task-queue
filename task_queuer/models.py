from django.db import models


class Task(models.Model):
    create_time = models.DateTimeField(verbose_name='create time', blank=True, null=True)
    finish_time = models.DateTimeField(verbose_name='finish time', blank=True, null=True)
    start_time = models.DateTimeField(verbose_name='start time', blank=True, null=True)

    class Meta:
        ordering = ('-create_time',)

    def get_status(self):
        return 'finished' if self.finish_time else 'in porgress' if self.start_time else 'in queue'
