from django.db import models
from django.utils import timezone

# Create your models here.
class content_list(models.Model):
    user= models.ForeignKey('auth.User',on_delete= models.CASCADE)
    content= models.TextField()
    is_finished= models.BooleanField(default= 0)
    create_date= models.DateTimeField()
    update_date= models.DateTimeField()

    def create_todo(self):
        self.create_date= timezone.now()
        self.update_date= timezone.now()
        self.save()

    def update_todo(self):
        self.update_date= timezone.now()
        self.save()

    def __str__(self):
        return self.content