from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('change_password',views.change_password,name='change_password'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('add_bank_details',views.add_bank_details,name='add_bank_details'),
    path('view_my_account_details',views.view_my_account_details,name='view_my_account_details'),
    path('add_experience',views.add_experience,name='add_experience'),
    path('add_salary',views.add_salary,name='add_salary'),
    path('view_all_salary',views.view_all_salary,name='view_all_salary'),
    path('view_my_salary',views.view_my_salary,name='view_my_salary'),
    path('view_all_experience',views.view_all_experience,name='view_all_experience'),
    path('view_my_experience',views.view_my_experience,name='view_my_experience'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)