from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.filters import CustomFilter
from books.models import Book, Author, Review, BookInstance
from books.pagination import CustomPagination
from books.serializers import BookSerializer, AuthorSerializer, ReviewSerializer, BookInstanceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# def post(request):
#     serializer = CreateBookSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class = PageNumberPagination
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CustomFilter
    search_fields = ['isbn']

    # filterset_fields = ['author_id', 'title']

    def get_serializer_context(self):
        return {'request': self.request}

    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     author_id = self.request.query_params.get('author_id')
    #     if author_id is not None:
    #         queryset = queryset.filter(author_id=author_id)
    #         return queryset


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_id': self.kwargs['book_pk']}


class BookInstanceViewSet(ListCreateAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    permission_classes = [IsAuthenticated]

# def author_list(request):
#     if request.method == 'GET':
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#
# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# def get_serializer_class(self):
#     return {'request': self.request}


# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_class(self):
#         return {'request': self.request}

#
# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# def get_queryset(self):
#     return Book.objects.all()
#
# def get_serializer_class(self):
#     return BookSerializer
#
# def get_serializer_context(self):
#     return {'request': self.request}


# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True, context={'request', request})
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class BookDetail(APIView):
#     # def get(self, request, pk):
#     #     book = get_object_or_404(Book, pk=pk)
#     #     serializer = BookSerializer(book, context={'request': request})
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#     #
#     # def put(self, request, pk):
#     #     book = get_object_or_404(Book, pk=pk)
#     #     serializer = BookSerializer(book, data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#     #
#     # def delete(self, request, pk):
#     #     book = get_object_or_404(Book, pk=pk)
#     #     book.delete()
#     #     return Response(status=status.HTTP_200_OK)

#
# class AuthorList(APIView):
#     def get(self, request):
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request):
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class AuthorDetail(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = BookSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Book, pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_200_OK)


# class ReviewList(APIView):
#     def get(self, request):
#         queryset = Review.objects.all()
#         serializer = ReviewSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request):
#         serializer = CreateReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class ReviewDetail(APIView):
#     def get(self, request, pk):
#         review = get_object_or_404(Review, pk=pk)
#         serializer = BookSerializer(review)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# @action(detail=True, methods=['post'])
# def comment(self, request, pk=None):
#     tweet = self.get_object()
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user, tweet=tweet)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def put(self, request, pk):
#         review = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(review, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         review = get_object_or_404(Book, pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_200_OK)

# @api_view(['GET', 'POST', 'DELETE'])
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.select_related('author').all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateBookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book,context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_200_OK)


# @api_view(['GET', 'POST', 'DELETE'])
# def author_list(request):
#     if request.method == 'GET':
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def author_detail(request, pk):
#     # author = Book.objects.get(Author, pk=pk)
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_200_OK)

#
# @api_view(['GET', 'POST'])
# def reviewers_list(request):
#     if request.method == 'GET':
#         queryset = Review.objects.all()
#         serializer = ReviewSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def review_detail(request, pk):
#     review = Review.objects.get(Review, pk=pk)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_200_OK)

# Create your views here.
# users = [
#     {"name": "Couthio"},
#     {"name": "olu"},
#     {"name": "mer"}
# ]
#
#
# def welcome(request):
#     query_set = Author.objects.get(pk=1)
#     return render(request, "books/welcome.html", {"authors": list(query_set)})
#
#
# def wayoo(request):
#     return HttpResponse("Wayooooooooooo")
