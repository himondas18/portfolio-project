from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='blogimages/')
    
    def summary(self):
        return self.body[:100]
    
    def __str__(self):
        return self.title