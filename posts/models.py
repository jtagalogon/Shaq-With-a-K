from django.db import models
from datetime import datetime

class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_body = models.TextField()
    likes = models.IntegerField(blank=True)
    dislikes = models.IntegerField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey(Users, on_delete=models.CASCADE)
# Does it matter where this 'poster' foreign key goes?

    def __str__(self):
    	return self.post_title

    class Meta:
        managed = False
        db_table = 'post'
# Create your models here.
