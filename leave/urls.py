from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    path('apply_leave',views.apply_leave,name='apply_leave'),
    path('view_my_leave',views.view_my_leave,name='view_my_leave'),
    path('view_all_leave',views.view_all_leave,name='view_all_leave'),
    path('update_leave/<int:leave_id>',views.update_leave,name='update_leave'),
    path('my_leave_count',views.my_leave_count,name='my_leave_count'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)