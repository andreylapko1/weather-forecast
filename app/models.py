from django.db import models


class Visitor(models.Model):
    session_key = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class VisitorSearch(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    search_city = models.CharField(max_length=255)



# Create your models here.
