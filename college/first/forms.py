from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CourseForm(forms.ModelForm):
    class Meta:
        model = Add_course
        fields = ('course_name', 'course_code',
                  'semister_or_year', 'no_of_semister_or_year')
        labels = {
            'course_name': '',
            'course_code': '',
            'semister_or_year' : '',
            'no_of_semister_or_year' : '',
        }

class SemisterYearForm(forms.ModelForm):
    class Meta:
        model = Add_semister
        fields = '__all__'
        labels = {
            'select_course': '',
            'semister_name': '',
        }
        widgets = {
            'semister_name': forms.TextInput(attrs={'placeholder': 'Semister / Year'}),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Add_subject
        fields = ('select_course', 'select_semister', 'subject_code',
                  'subject_name', 'select_subject_type', 'theory_marks', 'Practical_marks')
        labels = {
            'select_course' : '',
            'select_semister': '',
            'subject_code' : '',
            'subject_name' : '',
            'select_subject_type' : '',
            'theory_marks' : '',
            'Practical_marks' : ''
        }
        widgets = {
            'subject_code': forms.TextInput(attrs={'placeholder': 'Subject Code'}),
            'subject_name': forms.TextInput(attrs={'placeholder': 'Subject Name'}),
            'theory_marks': forms.TextInput(attrs={'placeholder': 'Theory Marks'}),
            'Practical_marks': forms.TextInput(attrs={'placeholder': 'Practical Marks'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields['select_course'].requred = False

class StudentSearchForm(forms.ModelForm):
    class Meta:
        model = Add_student
        fields = ['select_course', 'select_semister']
        labels = {
        'select_course': '',
        'select_semister': '',
        }
        widgets = {
            'select_course': forms.Select(attrs={'class': 'form-control'}),
            'select_semister': forms.Select(attrs={'class': 'form-control'}),
        }


class SubjectSearchForm(forms.ModelForm):
    class Meta:
        model = Add_subject
        fields = ['select_course', 'select_semister']


class TeacherSearchForm(forms.ModelForm):
    class Meta:
        model = Add_teacher
        fields = ['teacher_name']
        labels = {
            'teacher_name':'Search'
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Add_student
        fields = ['select_course', 'select_semister', 'student_name', 'student_cnic', 'domicile', 'email', 'phone_no', 'date_of_birth', 
                    'maritual_status', 'Nationality', 'address', 'user_picture', 'father_name', 'phone_no', 'father_cnic', 'father_ocupation',
                        'monthly_income', 'institute_name', 'exam_name', 'total_marks', 'obtain_marks', 'grade', 'board_roll_no', 'passing_year']

        def clean_student_name(self):
            for instance in Add_student.objects.all():
                if instance.student_name == student_name:
                    raise forms.ValidationError("This Username Already Taken")

        def clean_institute_name(self):
            institute_name = self.cleaned_data.get('institute_name')
            if (institute_name == ""):
                raise forms.validationError("This is Field you cannot left blank")


        labels = {
            'select_course': '',
            'select_semister':'',
            'student_name':'',
            'student_cnic':'',
            'domicile':'',
            'email':'',
            'phone_no':'',
            'date_of_birth':'',
            'maritual_status': '',
            'Nationality': '',
            'address': '',
            'user_picture': '',
            'father_name': '',
            'phone_no':'',
            'father_cnic': '',
            'father_ocupation':'',
            'monthly_income': '',
            'institute_name': '',
            'exam_name':'',
            'total_marks': '',
            'obtain_marks': '',
            'grade': '',
            'board_roll_no':'',
            'passing_year': '',
        }

        widgets = {
            'student_name': forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'yyy / mm / dd'}),
            'father_name': forms.TextInput(attrs={'placeholder': 'Father Name'}),
            'father_ocupation': forms.TextInput(attrs={'placeholder': 'Father Occupation'}),
            'institute_name': forms.TextInput(attrs={'placeholder': 'Institute Name'}),
            'exam_name': forms.TextInput(attrs={'placeholder': 'Name Of Exam'}),
            'passing_year': forms.TextInput(attrs={'placeholder': 'Passing Year'}),
        }





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name' ,'username', 'email', 'password1', 'password2')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Add_project
        fields = ('select_course', 'select_semister', 'select_student', 'project_title', 'programming_technology', 'select_status', 'date_created')
        labels = {
            'select_course': '',
            'select_semister': '',
            'select_student': '',
            'project_title': '',
            'programming_technology': '',
            'select_status': '',
            'date_created': '',
        }
        widgets = {
            'project_title': forms.TextInput(attrs={'placeholder': 'Project Title'}),
            'programming_technology': forms.TextInput(attrs={'placeholder': 'Programming Technology'}),
            'date_created': forms.TextInput(attrs={'placeholder': 'yyyy/mm/dd'})
        }

class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Add_syllabus
        fields = ('select_course', 'select_semister', 'select_subject', 'upload_file')
        labels = {
            'select_course': '',
            'select_semister': '',
            'select_subject': '',
            'upload_file': '',
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Add_assignment
        fields = ('select_course', 'select_semister', 'select_subject', 'upload_file')
        labels = {
            'select_course': '',
            'select_semister': '',
            'select_subject': '',
            'upload_file': '',
        }


class FineForm(forms.ModelForm):
    class Meta:
        model = Add_fine
        fields = ('select_course', 'select_semister', 'select_student', 'reason_for_fine', 'amount', 'status')
        labels = {
            'select_course': '',
            'select_semister': '',
            'select_student': '',
            'reason_for_fine': '',
            'amount': '',
            'status': '',
        }
        widgets = {
            'reason_for_fine': forms.TextInput(attrs={'placeholder':'Reason For Fine'}),
            'amount': forms.TextInput(attrs={'placeholder':'Enter Amount'})
        }


class TimeTableForm(forms.ModelForm):
    class Meta:
        model = Add_timetable
        fields = {'select_course', 'select_semister', 'upload_file'}
        labels = {
            'select_course': '',
            'select_semister': '',
            'upload_file': '',
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Add_teacher
        fields = {'select_course', 'select_semister', 'teacher_name', 'email_id', 'phone_no', 'maritual_status', 'gender', 'experience',
                    'date_of_birth', 'teacher_picture', 'address', 'father_name', 'phone_no', 'insitute', 'name_of_exam', 
                        'grade_gpa', 'board', 'passing_year'}

        labels = {
            'select_course': '',
            'select_semister': '',
            'teacher_name': '',
            'email_id': '',
            'phone_no': '',
            'maritual_status': '',
            'gender': '',
            'experience': '',
            'date_of_birth': '',
            'teacher_picture': '',
            'address': '',
            'father_name': '',
            'phone_no': '',
            'insitute': '',
            'name_of_exam': '',
            'grade_gpa': '',
            'board': '',
            'passing_year': '',
        }                

class ResultForm(forms.ModelForm):
    class Meta:
        model = Add_result
        fields = {'select_course', 'select_semister', 'upload_file'}
        labels = {
            'select_course': '',
            'select_semister': '',
            'upload_file': '',
        }

class AssignSubjectForm(forms.ModelForm):
    class Meta:
        model = Assign_subject
        fields = {'select_course', 'select_semister', 'select_teacher', 'select_subject'}
        labels = {
            'select_course': '',
            'select_semister': '',
            'select_teacher': '',
            'select_subject': '',
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = Add_news
        fields = {'Choose_img', 'event_title', 'event_description'}
        labels = {
            'Choose_img': '',
            'event_title': '',
            'event_description': '',
        }
        widgets = {
            'event_title': forms.TextInput(attrs={'placeholder': 'Event Title'}),
            'event_description': forms.TextInput(attrs={'placeholder': 'Write Event Description'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Add_event
        fields = {'Choose_img', 'event_title', 'event_description'}
        labels = {
            'Choose_img': '',
            'event_title': '',
            'event_description': '',
        }
        widgets = {
            'event_title': forms.TextInput(attrs={'placeholder': 'Event Title'}),
            'event_description': forms.TextInput(attrs={'placeholder': 'Write Event Description'}),
        }
