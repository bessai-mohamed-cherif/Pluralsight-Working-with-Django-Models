from django.urls import path

<<<<<<< HEAD
=======
from .views import category_view
>>>>>>> fa9bec0 (fifth commit)

app_name = "store"

urlpatterns = [
<<<<<<< HEAD
=======
    path('category/<str:name>', category_view, name="category"),
>>>>>>> fa9bec0 (fifth commit)
]
