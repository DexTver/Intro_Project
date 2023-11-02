from django.db import models


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
