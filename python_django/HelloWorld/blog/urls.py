from django.urls import path
import blog.views

urlpatterns = [
    path('index', blog.views.get_index_page),
    path('detail/<int:article_id>', blog.views.get_detail_page),

]
