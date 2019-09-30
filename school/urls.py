from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('admin/', views.admin_view, name='admin'),
    path('admission/', views.admission_view, name='admission'),
    path('registration/', views.registration, name='registration'),
    # path('teacher/', views.Teacher_view, name='teacher'),
    path('teacherlist/', views.Teacherlist, name='teacherlist'),
    path('editteacher/<int:id>/',views.editteacher,name='editteacher')
]
