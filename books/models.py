from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=17)


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} "

    class Meta:
        ordering = ['email']


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),
        ('ROMANCE', 'romance')
    ]
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=8, choices=GENRE_CHOICES, default='Finance')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateField(blank=True, null=True)
    total_copies_brought = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.isbn}"


class Address(models.Model):
    street_number = models.CharField(max_length=30, blank=False)
    street_name = models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100, default="Nigeria")


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Review(models.Model):
    name = models.CharField(max_length=40, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
