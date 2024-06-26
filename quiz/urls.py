from django.urls import path
from .views.register import register
from .views.login import login_view
from .views.logout import logout_view
from .views.landing_page import landing_page
from .views.try_now import try_now_page
from .views.home import home_page
from .views.about_contact import about_view, contact_view
from quiz.views.campaignViews.views import participate
from quiz.views.termsCondition import privacy_policy, terms_of_service
from quiz.views.settingsProfile import profile_page, settings_page

app_name = 'quiz'

urlpatterns = [
    path('', landing_page, name='landing'),  # Landing page as the default home page for unauthenticated users
    path('try-BrainFlex/', try_now_page, name='try-brainflex'),  # Landing page as the default home page for unauthenticated users
    path('home/', home_page, name='home'),  # Home page for authenticated users
    
    path('profile/', profile_page, name='profile'),
    path('settings/', settings_page, name='settings'),
    
    
    path('about/', about_view, name='about'),  # URL pattern for the "About" page
    path('contact/', contact_view, name='contact'),  # URL pattern for the "Contact" page
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
    

    
    path('campaign/<int:campaign_id>/', participate, name='campaign_detail'),

    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]


