from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # Author Name

    def __str__(self):
        return self.name  # For admin display

class Book(models.Model):
    title = models.CharField(max_length=255)  # Book Title
    publication_year = models.IntegerField()   # Year Published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Connect to Author
