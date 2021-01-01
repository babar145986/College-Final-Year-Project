from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('add_semister_year/', views.add_semister_year, name="add_semister_year"),
    path('semister_year_remove/<str:pk_test>/', views.semister_year_remove, name='semister_year_remove'),
    path('course_semister/<str:pk_test>/', views.course_semister, name='course_semister'),
    path('semister_detail/<str:pk_test>/', views.semister_detail, name='semister_detail'),
    path('front_home/', views.front_home, name="front_home"),


    path('subject/', views.subject, name='subject'),
    path('subject_remove/<str:pk_test>', views.subject_remove, name='subject_remove'),
    path('subject_update/<str:pk_test>/', views.subject_update, name='subject_update'),


    path('teacher/', views.teacher, name='teacher'),
    path('teacher_update/<str:pk_test>/', views.teacher_update, name='teacher_update'),
    path('teacher_remove/<str:pk_test>/', views.teacher_remove, name='teacher_remove'),
    path('teacher_profile/<str:pk_test>/', views.teacher_profile, name='teacher_profile'),


    path('time_table/', views.time_table, name='time_table'),
    path('time_table_update/<str:pk_test>/', views.time_table_update, name="time_table_update"),
    path('time_table_remove/<str:pk_test>/', views.time_table_remove, name="time_table_remove"),


    path('result/', views.result, name='result'),
    path('result_update/<str:pk_test>/', views.result_update, name='result_update'),
    path('result_delete/<pk_test>/', views.result_delete, name='result_delete'),


    path('register_user/', views.register_user, name='register_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('user_update/<str:pk_test>/', views.user_update, name='user_update'),
    path('user_remove/<str:pk_test>/', views.user_remove, name='user_remove'),


    path('student_fine/', views.student_fine, name='student_fine'),
    path('fine_update/<str:pk_test>/', views.fine_update, name='fine_update'),
    path('fine_remove/<str:pk_test>/', views.fine_remove, name='fine_remove'),


    path('project_report/', views.project_report, name='project_report'),
    path('project_update/<str:pk_test>/', views.project_update, name='project_update'),
    path('project_remove/<str:pk_test>/', views.project_remove, name='project_remove'),


    path('syllabus/', views.syllabus, name='syllabus'),
    path('syllabus_update/<str:pk_test>/', views.syllabus_update, name='syllabus_update'),
    path('syllabus_remove/<str:pk_test>/', views.syllabus_remove, name='syllabus_remove'),


    path('select_course/<str:pk_test>/', views.select_course, name='select_course'),




    path('assignment/', views.assignment, name='assignment'),
    path('assignment_update/<str:pk_test>/', views.assignment_update, name='assignment_update'),
    path('assignment_remove/<str:pk_test>/', views.assignment_remove, name='assignment_remove'),



    path('course_save/', views.course_save, name='course_save'),
    path('course_remove/<str:pk_test>/', views.course_remove, name='course_remove'),
    path('course_update/<str:pk_test>/',
         views.course_update, name='course_update'),


    path('teacher_save/', views.teacher_save, name='teacher_save'),
    path('course/<str:pk_test>/', views.course, name='course'),


    path('assign_subject/', views.assign_subject, name='assign_subject'),
    path('assing_subject_update/<str:pk_test>/', views.assing_subject_update, name='assing_subject_update'),
    path('assign_subject_delete/<str:pk_test>/', views.assign_subject_delete, name='assign_subject_delete'),


    path('enter_marks/', views.enter_marks, name='enter_marks'),
    path('search_student/', views.search_student, name='search_student'),

    #=================================================== start student urls ========================================

    path('student_form/', views.student_form, name='student_form'),
    path('<int:id>/', views.student_form, name='student_update'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_profile/<str:pk_test>/', views.student_profile, name='student_profile'),
    path('search_student_real/', views.search_student_real, name='search_student_real'),

    path('my_filter/', views.my_filter, name='my_filter'),
    path('load-semister/', views.load_semister, name='load-semister'),
    path('load_student/', views.load_student, name="load_student"),
    path('load_teacher/', views.load_teacher, name='load_teacher'),


    path('semister_students/<str:pk_test>/', views.semister_students, name='semister_students'),
    path('semister_subject/<str:pk_test>/', views.semister_subject, name='semister_subject'),


    #=====================================================================================================================
    #=====================================================================================================================
    #=====================================================================================================================

    path('show_result/', views.show_result, name='show_result'),
    path('show_syllabus/', views.show_syllabus, name='show_syllabus'),
    path('show_assignment/', views.show_assignment, name='show_assignment'),
    path('show_timetable/', views.show_timetable, name='show_timetable'),
    

    #====================================================================================================================
    #====================================================== NEW WORKS ===================================================

    path('links/', views.links, name="links"),
    path('news_page/', views.news_page, name="news_page"),
    path('select_news/<str:pk_test>/', views.select_news, name='select_news'),
    path('gallery/', views.gallery, name="gallery"),
    path('departments/', views.departments, name="departments"),
    path('department_details/', views.department_details, name='department_details'),
    path('admission/', views.admission, name="admission"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('event_save/', views.event_save, name="event_save"),
    path('delete_event/<str:pk_test>/', views.delete_event, name="delete_event"),
    path('delete_news/<str:pk_test>/', views.delete_news, name="delete_news"),
    path('event_grid/', views.event_grid, name='event_grid'),
    path('select_event/<str:pk_test>/', views.select_event, name="select_event"),

    #======================================== ABOUT PAGE =============================================
    
    path('about_objective/', views.about_objective, name="about_objective"),
    path('about_identity/', views.about_identity, name="about_identity"),
    path('about_mission/', views.about_mission, name="about_mission"),

    
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




