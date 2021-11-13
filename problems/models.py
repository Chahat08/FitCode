from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model

# Create your models here.
class Problem(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )

    title=models.CharField(max_length=200);
    subject=models.CharField(max_length=200);
    topic=models.CharField(max_length=200);
    details=models.TextField(blank=True);

    header=models.ImageField(upload_to='headers/', blank=True)

    # link for youtube vid to be embedded
    youtube=models.URLField(blank=True)

    #done_by=models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('problem_detail', args=[str(self.id)])


class Comment(models.Model):

    problem=models.ForeignKey(
            Problem,
            on_delete=models.CASCADE,
            related_name='comments'
        )
    comment=models.TextField()
    author=models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE
        )
    created = models.DateField(auto_now_add=True)
    # active=models.BooleanField(default=False)

    def __str__(self):
        return self.comment

    class Meta:
        ordering=['created']

class ProblemURL(models.Model):

    problem=models.ForeignKey(
            Problem,
            on_delete=models.CASCADE,
            related_name='urls'
        )

    url=models.URLField()

    def __str__(self):
        return self.url