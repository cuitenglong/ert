from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """图书类"""
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    """英雄类"""
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    # book作为外键关联到表
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
