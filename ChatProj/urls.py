from django.contrib import admin
from django.urls import path, include
from chatback import views as chatback_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', chatback_views.register, name='signup.html'),
    path('account/', chatback_views.profile, name='account.html'),
    path('login/', auth_views.LoginView.as_view(
        template_name='chatback/registration/login.html'), name='login'),
    path('', include('chatback.urls')),  # Все остальные маршруты `chatback`
]
