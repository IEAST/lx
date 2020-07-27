from django.urls import path
import blog.views

urlpatterns = [
    path('index', blog.views.get_index_page),
    path('detail', blog.views.get_detail_page),

]
