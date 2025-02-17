from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import BookListApiView, book_list_view, BookDetailApiView, \
    BookDeleteApiView, BookUpdateApiView, BookCreateApiView, \
        BookListCreateApiView, BookUpdateDeleteView, BookViewset

from .views import BookListApiView


router = SimpleRouter()
router.register('books', BookViewset, basename='books')



urlpatterns = [
    # path("books/", BookListApiView.as_view()),
    # path("book/", BookListCreateApiView.as_view(), name=""),
    # path("bookud/<int:pk>/", BookUpdateDeleteView.as_view(), name=""),
    # path("books/create", BookCreateApiView.as_view(), name=""),
    # path("books/<int:pk>/", BookDetailApiView.as_view(), name=""),
    # path("books/<int:pk>/update/", BookUpdateApiView.as_view(),),
    # path("books/<int:pk>/delete/", BookDeleteApiView.as_view(),),
    # path("books/", book_list_view),
]


urlpatterns = urlpatterns + router.urls