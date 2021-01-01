from django.shortcuts import render, redirect
from .models import *
from .forms import CourseForm, TeacherForm, StudentForm, SubjectForm, StudentSearchForm, SubjectSearchForm, TeacherSearchForm, CreateUserForm, ProjectForm, SyllabusForm, AssignmentForm, FineForm, SemisterYearForm, TimeTableForm, ResultForm, AssignSubjectForm, NewsForm, EventForm
from django.http import HttpResponse
from .filters import Add_studentFilter
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#=================================================== HOME PAGE START ============================================================

def links(request):
    return render(request, 'college_website/links.html')

def front_home(request):
    all_events = Add_event.objects.all()
    all_news = Add_news.objects.all()
    content = {'all_events': all_events, 'all_news': all_news}
    return render(request, 'college_website/index-2.html', content)

def news_page(request):
    all_news = Add_news.objects.all()
    content = {'all_news': all_news}
    return render(request, 'college_website/newsgrid.html', content)

def select_news(request, pk_test):
    select_news = Add_news.objects.get(id=pk_test)
    content = {'select_news': select_news}
    return render(request, 'college_website/newsdetail.html', content)


def show_result(request):
    all_result = Add_result.objects.all()
    content = {'all_result': all_result}
    return render(request, 'college_website/download/result.html', content)


def show_syllabus(request):
    all_syllabus = Add_syllabus.objects.all()
    content = {'all_syllabus': all_syllabus}
    return render(request, 'college_website/download/syllabus.html', content)


def show_assignment(request):
    all_assignment = Add_assignment.objects.all()
    content = {'all_assignment': all_assignment}
    return render(request, 'college_website/download/assignment.html', content)


def show_timetable(request):
    all_table = Add_timetable.objects.all()
    content = {'all_table': all_table}
    return render(request, 'college_website/download/time_table.html', content)

def gallery(request):
    return render(request, 'college_website/gallery.html')

def departments(request):
    return render(request, 'college_website/departments.html')

def department_details(request):
    return render(request, 'college_website/departmentdetail.html')

def admission(request):
    return render(request, 'college_website/admissions.html')

def contact_us(request):
    return render(request, 'college_website/contactusvone.html')

#================================================== About Pages =================================================
#================================================================================================================

def about_objective(request):
    return render(request, 'college_website/about/aboutobjectives.html')

def about_identity(request):
    return render(request, 'college_website/about/aboutouridentity.html')

def about_mission(request):
    return render(request, 'college_website/about/aboutvisionmission.html')


#=================================================== LOGIN PAGE START ============================================================

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                messages.info(request, "Username Or password is incorrect")
        return render(request, 'login/login.html')


#=================================================== LOGOUT PAGE START ============================================================

def logout_user(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url='login')
def home(request):
    all_users = User.objects.count()
    all_teachers = Add_teacher.objects.count()
    all_students = Add_student.objects.count()
    all_courses = Add_course.objects.count()
    all_subjects = Add_subject.objects.count()
    all_projects = Add_project.objects.count()
    all_fines = Add_fine.objects.count()
    all_news = Add_news.objects.all()
    all_events = Add_event.objects.all()
    news_form = NewsForm()
    event_form = EventForm()
    event_count = Add_event.objects.count()
    news_count = Add_news.objects.count()

#============================================================================================================
#========================================= News Form Coding Form ============================================

    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES)
        if news_form.is_valid():
            news_form.save()
            return redirect('/home')
        else:
            return HttpResponse("Something Wrong")

#============================================================================================================
#========================================= Event Form Coding Form ============================================


    content = {'all_users':all_users, 'all_teachers':all_teachers, 'all_students':all_students, 
                'all_courses':all_courses, 'all_subjects': all_subjects, 'all_projects':all_projects, 'all_fines':all_fines, 
                    'all_news':all_news, 'all_events': all_events, 'news_form': news_form, 'event_form': event_form, 'event_count':event_count,
                        'news_count':news_count}
    return render(request, 'index.html', content)

def event_save(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)
        if event_form.is_valid():
            event_form.save()
            return redirect('/home')
        else:
            return HttpResponse('Something Wrong')

def delete_event(request, pk_test):
    select_event = Add_event.objects.get(id=pk_test)
    select_event.delete()
    return redirect('/home')

def delete_news(request, pk_test):
    select_news = Add_news.objects.get(id=pk_test)
    select_news.delete()
    return redirect('/home')

def event_grid(request):
    all_event = Add_event.objects.all()
    content = {'all_event':all_event}
    return render(request, 'college_website/event_grid.html', content)

def select_event(request, pk_test):
    select_event = Add_news.objects.get(id=pk_test)
    content = {'select_event': select_event}
    return render(request, 'college_website/event_detail.html', content)


#=========================================== SHOW ALL COURSE PAGE START ===========================================================

@login_required(login_url='login')
def course(request):
    all_courses = Add_course.objects.all()
    context = {'all_courses':all_courses}
    return render(request, 'course/courses.html', context)


#=================================================== COURSE SAVE PAGE START ========================================================

@login_required(login_url='login')
def course_save(request):
    all_courses = Add_course.objects.all()
    if request.method == 'POST':
        course_code = request.POST['course_code']
        course_name = request.POST['course_name']
        select_duration = request.POST['select_duration']
        semister_year = request.POST['semister_year']
        data = Add_course(course_code=course_code, course_name=course_name,
                          semister_or_year=select_duration, no_of_semister_or_year=semister_year)
        data.save()
        messages.success(request, "Course Added Successfully...")
        return redirect('course')
    else:
        messages.error(request, "Something wrong in your models...")
        return redirect('course')
    total_courses = all_courses.count()
    context = {'all_courses': all_courses,
               'total_courses': total_courses, 'messages': messages}
    return render(request, 'course/courses.html', context)

#=================================================== COURSE REMOVE PAGE START =======================================================


@login_required(login_url='login')
def course_remove(request, pk_test):
    data = Add_course.objects.get(id=pk_test)
    data.delete()
    messages.error(request, " Course Deleted... ")
    return redirect('/course')


#=============================================== COURSE UPDATE PAGE START ============================================================

@login_required(login_url='login')
def course_update(request, pk_test):
    course = Add_course.objects.get(id=pk_test)
    course_form = CourseForm(instance=course)
    if request.method == 'POST':
        course = CourseForm(request.POST, instance=course)
        if course.is_valid():
            course.save()
            messages.warning(request, 'Course Updated...')
            return redirect('/course')
    context = {'course': course, 'course_form': course_form}
    return render(request, 'course/course_update.html', context)


@login_required(login_url='login')
def add_semister_year(request):
    form = SemisterYearForm()
    if request.method == 'POST':
        form = SemisterYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_semister_year')
        else:
            return HttpResponse("Something Wrong")
    data = Add_semister.objects.all()
    context = {'form':form, 'data':data}
    return render(request, 'course/add_semister.html', context)


@login_required(login_url='login')
def course_semister(request, pk_test):
    select_course = Add_course.objects.get(id=pk_test)
    semister = select_course.add_semister_set.all()
    semister_count = select_course.add_semister_set.all().count()
    student_count = select_course.add_student_set.all().count()
    teacher_count = select_course.add_teacher_set.all().count()
    subject_count = select_course.add_subject_set.all().count()
    content = {'select_course':select_course, 'semister': semister, 'semister_count':semister_count, 'student_count':student_count, 'teacher_count':teacher_count, 'subject_count':subject_count}
    return render(request, 'course/course_semister.html', content)

@login_required(login_url='login')
def semister_detail(request, pk_test):
    select_semister = Add_semister.objects.get(id=pk_test)
    student_count = select_semister.add_student_set.all().count()
    student = select_semister.add_student_set.all()
    teacher = select_semister.add_teacher_set.all()
    teacher_count = select_semister.add_teacher_set.all().count()
    subject_count = select_semister.add_subject_set.all().count()
    subject = select_semister.add_subject_set.all()
    assignment_count = select_semister.add_assignment_set.all().count()
    assignment = select_semister.add_assignment_set.all()
    content = {'assignment':assignment, 'subject':subject, 'teacher':teacher, 'student':student, 'assignment_count': assignment_count, 'select_semister':select_semister, 'student_count':student_count, 'teacher_count':teacher_count, 'subject_count':subject_count}
    return render(request, 'course/semister_details.html', content)

@login_required(login_url='login')
def semister_year_remove(request, pk_test):
    select = Add_semister.objects.get(id=pk_test)
    select.delete()
    return redirect('/add_semister_year')



#========================================== STUDENT FORM UPDATE AND SAVE PAGE START ===================================================

@login_required(login_url='login')
def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Add_student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "student/student_save.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST, request.FILES)
        else:
            student = Add_student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
        	form.save()
        	return redirect('/student_list')
    content = {'form':form}
    return render(request, 'student/student_save.html', content)


@login_required(login_url='login')
def student_list(request):
    all_student = Add_student.objects.all()
    form = StudentSearchForm(request.POST or None)
    content = {'all_student':all_student, 'form':form}
    if request.method == 'POST':
        all_student = Add_student.objects.all().filter(
            Q(select_course=form['select_course'].value()) & Q(select_semister=form['select_semister'].value()))
        content = {'all_student':all_student, 'form':form}
    return render(request, 'student/student.html', content)


#=================================================== STUDENT PROFILE PAGE START =======================================================

@login_required(login_url='login')
def student_profile(request, pk_test):
    students = StudentForm()
    student = Add_student.objects.get(id=pk_test)
    fine = student.add_fine_set.all()
    project = student.add_project_set.all()
    content = {'student': student, 'students':students, 'fine':fine, 'project':project}
    return render(request, 'student/student_profile.html', content)


#============================================== SEARCH STUDENT PAGE START ============================================================

@login_required(login_url='login')
def search_student_real(request):
	course = StudentForm(request.POST)
	content = {'course':course}
	if request.method == 'POST':
		srch = request.POST['srh']
		if srch:
			match = Add_student.objects.filter(Q(first_name__icontains=srch) | Q(last_name__icontains=srch) | Q(roll_no__icontains=srch))
			if match:
				return render(request, 'student/search_section.html', {'sr':match})
			else:
				messages.error(request, "No result found")
	return render(request, 'student/search_section.html', content)


@login_required(login_url='login')
def search_student(request):
    return render(request, 'student/search_section.html')



#=================================================== SHOW STUDENT PAGE START ==========================================================

def load_semister(request):
    select_course = request.GET.get('select_course')
    semister = Add_semister.objects.filter(select_course=select_course).order_by('id')
    print("Course ID============ :", select_course)

    select_semister = request.GET.get('select_semister')
    subject = Add_subject.objects.filter(select_semister=select_semister).order_by('subject_name')
    print("Semister ID=========== :", select_semister)
    return render(request, 'semister_dropdown.html', {'semister': semister, 'subject': subject, 'teacher':teacher})

def load_student(request):
    select_course = request.GET.get('select_course')
    semister = Add_semister.objects.filter(select_course=select_course).order_by('id')
    print("Course ID============ :", select_course)

    select_semister = request.GET.get('select_semister')
    student = Add_student.objects.filter(select_semister=select_semister).order_by('first_name')
    return render(request, 'semister_dropdown.html', {'semister':semister, 'student':student})

def load_teacher(request):
    select_course = request.GET.get('select_course')
    semister = Add_semister.objects.filter(select_course=select_course).order_by('id')
    print("Course ID============ :", select_course)

    select_semister = request.GET.get('select_semister')
    teacher = Add_teacher.objects.filter(select_semister=select_semister).order_by('teacher_name')
    return render(request, 'semister_dropdown.html', {'semister':semister, 'teacher':teacher})



#=================================================== MY FILTER JUST PRACTICE PAGE START ===============================================

def my_filter(request):
    form = SyllabusForm()
    attendance = Take_attendance.objects.all()
    if request.method == 'POST':
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        else:
            return HttpResponse("Something Wrong")
    context = {'form': form, 'attendance':attendance}
    return render(request, 'myfilter.html', context)


#========================================= SHOW AND ADD SUBJECT PAGE START ============================================================

@login_required(login_url='login')
def subject(request):
    subject_form = SubjectForm(request.POST)
    if subject_form.is_valid():
        subject_form.save()
        return redirect('/subject')
    all_subjects = Add_subject.objects.all()
    all_courses = Add_course.objects.all()
    form = SubjectSearchForm(request.POST or None)
    if request.method == 'POST':
        all_subjects = Add_subject.objects.all().filter(
            Q(select_course=form['select_course'].value()) & Q(select_semister=form['select_semister'].value()))
    else:
        messages.error(request, "No result found")
    context = {'all_subjects': all_subjects, 'all_courses':all_courses, 'subject_form':subject_form, 'form':form}
    return render(request, 'subject/subjects.html', context)


#========================================= UPDATE STUBJECT PAGE START =================================================================

@login_required(login_url='login')
def subject_update(request, pk_test):
    subject = Add_subject.objects.get(id=pk_test)
    subject_form = SubjectForm(instance=subject)
    if request.method == 'POST':
        subject = SubjectForm(request.POST, instance=subject)
        if subject.is_valid():
            subject.save()
            return redirect('/subject')
        else:
            return HttpResponse("some errors")
    context = {'subject': subject, 'subject_form': subject_form}
    return render(request, 'subject/subject_update.html', context)


#========================================= SUBJECT REMOVE PAGE START ==================================================================

@login_required(login_url='login')
def subject_remove(request, pk_test):
    all_subject = Add_subject.objects.get(id=pk_test)
    all_subject.delete()
    return redirect('/subject')


#========================================= SHOW AND SEARCH TEACHER PAGE START ==========================================================

@login_required(login_url='login')
def teacher(request):
    all_teachers = Add_teacher.objects.all()
    teacher_form = TeacherForm()
    form = TeacherSearchForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        all_teacher = Add_teacher.objects.all().filter(Q(teacher_name__icontains=form['teacher_name'].value()))
        context = {'all_teacher': all_teacher}
    context = {'all_teachers':all_teachers, 'form':form, 'teacher_form':teacher_form}
    return render(request, 'teacher/teacher.html', context)


#========================================= TEACHER SAVE PAGE START =====================================================================

@login_required(login_url='login')
def teacher_save(request):
    teacher_form = TeacherForm()
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('/teacher')
        else:
            return HttpResponse("Something Wrong")
            print(teacher_form)
    context = {'teacher_form':teacher_form}
    return render(request, 'teacher/teacher.html', context)


@login_required(login_url='login')
def teacher_profile(request, pk_test):
    teacher = Add_teacher.objects.get(id=pk_test)
    subject = teacher.assign_subject_set.all()
    total_subject = teacher.assign_subject_set.all().count()
    context = {'teacher':teacher, 'subject': subject, 'total_subject':total_subject}
    return render(request, 'teacher/teacher_profile.html', context)


#========================================= UPDATE TEACHER PAGE START ==================================================================

@login_required(login_url='login')
def teacher_update(request, pk_test):
	teacher = Add_teacher.objects.get(id=pk_test)
	teacher_form = TeacherForm(instance=teacher)
	if request.method == 'POST':
		teacher = TeacherForm(request.POST, instance=teacher)
		if teacher.is_valid():
			teacher.save()
			return redirect('/teacher')
		else:
			return HttpResponse("some errors")
	return render(request, 'teacher/teacher_update.html', {'teacher_form':teacher_form})


#========================================= STEACHER REMOVE PAGE =======================================================================

@login_required(login_url='login')
def teacher_remove(request, pk_test):
    select_teacher = Add_teacher.objects.get(id=pk_test)
    select_teacher.delete()
    return redirect('/teacher')


#========================================= SHOW PROJECT REPORT PAGE START ===============================================================

@login_required(login_url='login')
def project_report(request):
    all_project = Add_project.objects.all()
    project_count = Add_project.objects.all().count()
    completed_count = Add_project.objects.filter(
        select_status='Completed').count()
    pending_count = Add_project.objects.filter(select_status='Pending').count()
    expired_count = Add_project.objects.filter(select_status='Expired').count()
    print(completed_count)
    form = ProjectForm(request.POST)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/project_report')
        else:
            return HttpResponse("Something Wrong")
    content = {'all_project': all_project, 'form': form, 'project_count': project_count,
               'completed_count': completed_count, 'pending_count': pending_count, 'expired_count': expired_count}
    return render(request, 'project/project_reports.html', content)


#========================================= UPDATE PROJECT REPORT PAGE START =============================================================

@login_required(login_url='login')
def project_update(request, pk_test):
    project = Add_project.objects.get(id=pk_test)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        project = ProjectForm(request.POST, instance=project)
        if project.is_valid():
            project.save()
            return redirect('/project_report')
        else:
            return HttpResponse("some errors")
    content = {'form': form}
    return render(request, 'project/project_update.html', content)


#========================================= REMOVE PROJECT PAGE START ====================================================================

def project_remove(request, pk_test):
    project = Add_project.objects.get(id=pk_test)
    project.delete()
    return redirect('/project_report')


#========================================= SHOW SYLLABUS PAGE START =====================================================================

@login_required(login_url='login')
def syllabus(request):
    all_syllabus = Add_syllabus.objects.all()
    form = SyllabusForm()
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/syllabus')
        else:
            return HttpResponse('Something Wrong')
    content = {'all_syllabus': all_syllabus, 'form': form}
    return render(request, 'syllabus/syllabus.html', content)


#========================================= UPDATE SYLLABUS PAGE START ====================================================================

@login_required(login_url='login')
def syllabus_update(request, pk_test):
    syllabus = Add_syllabus.objects.get(id=pk_test)
    form = SyllabusForm(instance=syllabus)
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES, instance=syllabus)
        if form.is_valid():
            form.save()
            return redirect('/syllabus')
        else:
            return HttpResponse("some errors")
    content = {'form': form}
    return render(request, 'syllabus/syllabus_update.html', content)


#========================================= REMOVE SYLLABUS PAGE START ====================================================================

@login_required(login_url='login')
def syllabus_remove(request, pk_test):
    syllabus = Add_syllabus.objects.get(id=pk_test)
    syllabus.delete()
    return redirect('/syllabus')


#========================================= SHOW ASSIGNMENT PAGE START ====================================================================

@login_required(login_url='login')
def assignment(request):
    all_assignment = Add_assignment.objects.all()
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/assignment')
        else:
            return HttpResponse("fail")
    content = {'all_assignment': all_assignment, 'form': form}
    return render(request, 'assignmet/assignment.html', content)


#========================================= UPDATE ASSIGNMENT PAGE START ===================================================================

@login_required(login_url='login')
def assignment_update(request, pk_test):
    assignment = Add_assignment.objects.get(id=pk_test)
    form = AssignmentForm(instance=assignment)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('/assignment')
        else:
            return HttpResponse("some errors")
    content = {'form': form}
    return render(request, 'assignmet/assignment_update.html', content)


#========================================= REMOVE ASSIGNMENT PAGE START ==================================================================

def assignment_remove(request, pk_test):
    assignment = Add_assignment.objects.get(id=pk_test)
    assignment.delete()
    return redirect('/assignment')


#========================================= TIME TABLE PAGE START =======================================================================

@login_required(login_url='login')
def time_table(request):
    form = TimeTableForm()
    if request.method == 'POST':
        form = TimeTableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/time_table')
        else:
            return HttpResponse("something wrong")
    all_table = Add_timetable.objects.all()
    content = {'all_table':all_table, 'form': form}
    return render(request, 'time_table/time_table.html', content)


@login_required(login_url='login')
def time_table_update(request, pk_test):
    select_table = Add_timetable.objects.get(id=pk_test)
    form = TimeTableForm(instance=select_table)
    if request.method == 'POST':
        form = TimeTableForm(request.POST, request.FILES, instance=select_table)
        if form.is_valid():
            form.save()
            return redirect('/time_table')
        else:
            return HttpResponse("something wrong")
    content = {'form':form}
    return render(request, 'time_table/time_table_update.html', content)



def time_table_remove(request, pk_test):
    select_table = Add_timetable.objects.get(id=pk_test)
    select_table.delete()
    return redirect("/time_table")


@login_required(login_url='login')
def register_user(request):
    all_users = User.objects.all()
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    content = {'form':form, 'all_users':all_users}
    return render(request, 'register_user.html', content)


#========================================= ADD OR REGISTER USERS =======================================================================

@login_required(login_url='login')
def add_user(request):
    all_users = User.objects.all()
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register_user')
    content = {'form': form, 'all_users': all_users}
    return render(request, 'add_user/add_user.html', content)


#========================================= UPDATE USER PAGE START ======================================================================

@login_required(login_url='login')
def user_update(request, pk_test):
    select_user = User.objects.get(id=pk_test)
    form = CreateUserForm(instance=select_user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            return HttpResponse("something Wrong")
            return redirect('/register_user')
    content = {'form':form}
    return render(request, 'add_user/update_user.html', content)


#========================================= USER REMOVE PAGE START ============================================================

def user_remove(request, pk_test):
    select_user = User.objects.get(id=pk_test)
    select_user.delete()
    return redirect('/register_user')


#=============================================== STUDENT FINE PAGE START ================================================================

@login_required(login_url='login')
def student_fine(request):
    all_fines = Add_fine.objects.all()
    fine_count = Add_fine.objects.all().count()
    fine_paid = Add_fine.objects.filter(status='Paid').count()
    fine_unpaid = Add_fine.objects.filter(status='Unpaid').count()
    expired_fine = Add_fine.objects.filter(status='Expired').count()
    form = FineForm()
    if request.method == 'POST':
        form = FineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student_fine')
    content = {'all_fines':all_fines, 'form':form, 'fine_count':fine_count, 'fine_paid':fine_paid, 'fine_unpaid':fine_unpaid, 'expired_fine':expired_fine}
    return render(request, 'student/student_fine_list.html', content)



#========================================= STUDENT FINE UPDATE PAGE START ===============================================================

@login_required(login_url='login')
def fine_update(request, pk_test):
    select_fine = Add_fine.objects.get(id=pk_test)
    form = FineForm(instance=select_fine)
    if request.method == 'POST':
        form = FineForm(request.POST, instance=select_fine)
        if form.is_valid():
            form.save()
            return redirect('/student_fine')
        else:
            return HttpResponse("something Wrong")
    content = {'form':form}
    return render(request, 'student/update_fine.html', content)


#========================================= STUDENT FINE REMOVE PAGE START ===============================================================

def fine_remove(request, pk_test):
    select_fine = Add_fine.objects.get(id=pk_test)
    select_fine.delete()
    return redirect('/student_fine')


#========================================= ENTER MARKS PAGE START =========================================================================

@login_required(login_url='login')
def enter_marks(request):
    all_courses = Add_course.objects.all()
    all_semister = Add_semister.objects.all()
    content = {'all_courses': all_courses, 'all_semister': all_semister}
    return render(request, 'enter_marks.html', content)


#=========================================  ============================================================

@login_required(login_url='login')
def select_course(request, pk_test):
    select_course = Add_course.objects.get(id=pk_test)
    semister = select_course.add_semister_set.all()
    content = {'semister':semister}
    return render(request, 'semister.html', content)

@login_required(login_url='login')
def semister_subject(request, pk_test):
    select_semister = Add_semister.objects.get(id=pk_test)
    subject = select_semister.add_subject_set.all()
    context = {'subject':subject}
    return render(request, 'semister_subject.html', context)

@login_required(login_url='login')
def semister_students(request, pk_test):
    select_semister = Add_semister.objects.get(id=pk_test)
    students = select_semister.add_student_set.all()
    content = {'students':students}
    return render(request, 'semister_student.html', content)


@login_required(login_url='login')
def result(request):
    all_result = Add_result.objects.all()
    form = ResultForm()
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result')
        else:
            return HttpResponse("Something Wrong")
    content = {'form':form, 'all_result':all_result}
    return render(request, 'result/result.html', content)


@login_required(login_url='login')
def result_update(request, pk_test):
    select_result = Add_result.objects.get(id=pk_test)
    form = ResultForm(instance=select_result)
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES, instance=select_result)
        if form.is_valid():
            form.save()
            return redirect('/result')
        else:
            return HttpResponse("Something Wrong")
    content = {'form':form}
    return render(request, 'result/result_update.html', content)


def result_delete(request, pk_test):
    select_result = Add_result.objects.get(id=pk_test)
    select_result.delete()
    return redirect('result')


def load_course(request):
    course_id = request.GET.get('select_course')
    semister = Add_semister.objects.filter(course_id=course_id).order_by('name')
    content = {'semister':semister}
    return render(request, 'myfilter.html', content)


#========================================= ASSIGN SUBJECT TO STUDENT PAGE START ===========================================================

@login_required(login_url='login')
def assign_subject(request):
    all_subject = Assign_subject.objects.all()
    form = AssignSubjectForm()
    if request.method == 'POST':
        form = AssignSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assign_subject')
        else:
            return HttpResponse("Something Wrong")
    content = {'form':form, 'all_subject': all_subject}
    return render(request, 'assign/assing_subject.html', content)

@login_required(login_url='login')
def assing_subject_update(request, pk_test):
    select_subject = Assign_subject.objects.get(id=pk_test)
    form = AssignSubjectForm(instance=select_subject)
    if request.method == 'POST':
        form = AssignSubjectForm(request.POST, instance=select_subject)
        if form.is_valid():
            form.save()
            return redirect('/assign_subject')
        else:
            return HttpResponse("Something Wrong")
    content = {'form':form}
    return render(request, 'assign/assign_subject_update.html', content)

def assign_subject_delete(request, pk_test):
    select_subject = Assign_subject.objects.get(id=pk_test)
    select_subject.delete()
    return redirect('assign_subject')


#=========================================================================================================================
#=========================================================================================================================
#=========================================================================================================================






