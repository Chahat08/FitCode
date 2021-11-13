from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class TaskList(models.Model):

    title = models.CharField(max_length=250)
    problems = models.ManyToManyField(get_user_model())
    creator=models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
            related_name='creator'
        )

    def __str__(self):
        return self.title
