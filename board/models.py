from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=10)
    content = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now=True)
    read_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Board[id={self.id}, title={self.title}]"

    def add_count(self):
        self.read_count +=1
        self.save()
        