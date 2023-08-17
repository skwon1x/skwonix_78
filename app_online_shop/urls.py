from django.urls import path
from .views import index, top_sellers, advertisment_post, advertisment, login, profile, register

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisment_post, name='advertisement-post'),
    path('advertisement/', advertisment, name='advertisement'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
]