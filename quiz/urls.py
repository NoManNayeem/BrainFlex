from django.urls import path
from .views.register import register
from .views.login import login_view
from .views.logout import logout_view
from .views.landing_page import landing_page
from .views.home import home_page

app_name = 'quiz'

urlpatterns = [
    path('', landing_page, name='landing'),  # Landing page as the default home page for unauthenticated users
    path('home/', home_page, name='home'),  # Home page for authenticated users
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
