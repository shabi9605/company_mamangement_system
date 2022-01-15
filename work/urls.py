from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    path('assign_work',views.assign_work,name='assign_work'),
    path('view_all_assigned_work',views.view_all_assigned_work,name='view_all_assigned_work'),
    path('view_my_work',views.view_my_work,name='view_my_work'),
    path('update_percentage/<int:work_id>',views.update_percentage,name='update_percentage'),
    path('update_work_additiondays/<int:work_id>',views.update_work_additiondays,name='update_work_additiondays'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)