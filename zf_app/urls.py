from django.urls import path

from zf_app import views, student_views

urlpatterns = [
    # path("",views.home,name="home"),
    # path("", views.index, name="index"),
    path("", views.login_view, name="log"),
    path("base", views.base, name="base"),
    path("reg", views.admin_reg, name="reg"),
    path("studreg",views.student_reg,name="studreg"),
    path("admindash", views.admindash, name="admindash"),
    path("studentview",views.studentview,name="studentview"),
    path('mark_update/<int:id>/',views.mark_update,name='mark_update'),

    path('delete/<int:id>', views.delete_student_view, name='delete'),
    path("addmark",views.addmark,name='addmark'),
    path("markview",views.markview,name='markview'),
    path("student_update/<int:id>/",views.student_update,name='student_update'),
    path("table",views.table,name="table"),

###student##

    path("studentdash", student_views.studentdash, name="studentdash"),
    path("profile_update/<int:id>/",student_views.profile_update,name='profile_update'),
    path("profile",student_views.profile,name='profile'),
    path('logout_view', views.logout_view, name='logout_view'),

]