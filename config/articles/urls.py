from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticlesList.as_view(), name='home'),
    path('article/<slug:slug>/', ArticleShow.as_view(), name="post"),
    path('add/', ArticleAdd.as_view(), name="add"),
    path('destroy/<int:id>/', destroy, name="destroy"),
    path('category/<slug:slug>/', CategoryList.as_view(), name="cat"),
    path('tag/<int:id>/', TagList.as_view(), name="tag"),

    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name='register'),

]
