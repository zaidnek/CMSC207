from django.contrib import admin
from django.urls import path, include
from survey.views import questionnaire, confirmation
from users.views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', questionnaire.as_view(), name='questionnaire'),
    path('confirmation/', confirmation, name='confirmation'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]