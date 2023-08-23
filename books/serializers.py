from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import Book, Author, Review, BookInstance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'author']
    #
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name="author-detail"
    # )
    # # author = AuthorSerializer()
    # author = serializers.StringRelatedField()


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre', 'author']


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['first_name', 'last_name', 'book']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Review.objects.create(book_id=self.context['book_id'], **validated_data)


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'book']


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['book', 'user', 'date_returned', 'price']


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'phone_number']


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'username']
