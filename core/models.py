from django.core.urlresolvers import reverse

from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title
  def get_absolute_url(self):
    return reverse("question_detail", args=[self.id])

