from django.db import models
from PIL import Image

# Create your models here.

class Add_course(models.Model):
    CATEGORY = (
        ('Semister','Semister'),
        ('Year','Year'),
    )
    course_name = models.CharField(max_length=120, null=True)
    course_code = models.CharField(max_length=120, null=True)
    semister_or_year = models.CharField(max_length=120, choices=CATEGORY)
    no_of_semister_or_year = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.course_name
    

class Add_semister(models.Model):
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    semister_name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.semister_name


class Add_subject(models.Model):
    CATEGORY2 = (
        ('Core', 'Core'),
        ('Optional', 'Optional'),
    )
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE, blank=True)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=120, null=True)
    subject_name = models.CharField(max_length=120, null=True)
    select_subject_type = models.CharField(max_length=120, choices=CATEGORY2)
    theory_marks = models.CharField(max_length=50, null=True)
    Practical_marks = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.subject_name

class Add_student(models.Model):
    CATEGORY3 = (
        ('Maried', 'Maried'),
        ('Single', 'Single'),
        ('Divorced', 'Divorced')
    )
    CATEGORY2 = {
        ('Pakistani', 'Pakistani'),
        ('Other', 'Other'),
    }
    CATEGORY1 = {
        ('FATA', 'FATA'),
        ('Charsadda', 'Charsadda'),
        ('Peshawar', 'Peshawar'),
    }
    CATEGORY5 = {
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('Fail', 'Fail')
    }
    #=================== Personal Information =========================================
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=120, blank=True)
    student_cnic = models.IntegerField()
    domicile = models.CharField(max_length=100, choices=CATEGORY1)
    email = models.CharField(max_length=50, blank=True)
    phone_no = models.CharField(max_length=50, blank=True)
    date_of_birth = models.CharField(max_length=50, blank=True)
    maritual_status = models.CharField(max_length=50, choices=CATEGORY3)
    Nationality = models.CharField(max_length=120, choices=CATEGORY2)
    address = models.TextField()
    user_picture = models.ImageField(upload_to='media')

    #==================== Gurdian Information ===========================================
    father_name = models.CharField(max_length=50, blank=True)
    phone_no = models.IntegerField()
    father_cnic = models.IntegerField()
    father_ocupation = models.CharField(max_length=50, blank=True)
    monthly_income = models.IntegerField()

    #=================== Precious Academic Information ==================================
    institute_name = models.CharField(max_length=120, blank=True)
    exam_name = models.CharField(max_length=120, blank=True)
    total_marks = models.IntegerField()
    obtain_marks = models.IntegerField()
    grade = models.CharField(max_length=120, choices=CATEGORY5)
    board_roll_no = models.IntegerField()
    passing_year = models.DateField()

    def __str__(self):
        return self.student_name

class Add_teacher(models.Model):
    CATEGORY3 = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated')
    )
    CATEGORY2 = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    }
    CATEGORY4 = {
        ('1 Year', '1 Year'),
        ('2 Year', '2 Year'),
        ('3 Year', '3 Year'),
        ('4 Year', '4 Year')
    }
    # =========================================== Personal Information ====================================
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50, null=True)
    email_id = models.EmailField()
    phone_no = models.IntegerField()
    maritual_status = models.CharField(max_length=50, choices=CATEGORY3)
    gender = models.CharField(max_length=120, choices=CATEGORY2)
    experience = models.CharField(max_length=50, choices=CATEGORY4)
    date_of_birth = models.DateField()
    teacher_picture = models.ImageField(upload_to='media')
    address = models.TextField()

    #================================== Gurdian Information ================================================
    father_name = models.CharField(max_length=120, null=True)
    phone_no = models.IntegerField()

    # ================================  Educational Information ============================================
    insitute = models.CharField(max_length=120, null=True, blank=True)
    name_of_exam = models.CharField(max_length=120, null=True, blank=True)
    grade_gpa = models.CharField(max_length=100, null=True)
    board = models.CharField(max_length=120, null=True)
    passing_year = models.DateField()

    def __str__(self):
        return self.teacher_name


class Add_project(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Expired', 'Expired')
    )
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    select_student = models.ForeignKey(Add_student, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=120, null=True)
    programming_technology = models.CharField(max_length=120, null=True)
    select_status = models.CharField(max_length=120, choices=STATUS)
    date_created = models.DateField()


class Add_syllabus(models.Model):
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    select_subject = models.ForeignKey(Add_subject, on_delete=models.CASCADE)
    upload_file = models.FileField(upload_to='media/documents', blank=True)

    def __str__(self):
        return self.select_subject


class Add_assignment(models.Model):
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    select_subject = models.ForeignKey(Add_subject, on_delete=models.CASCADE)
    upload_file = models.FileField(upload_to='assignment', blank=True)

class Add_fine(models.Model):
    STATUS = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Expired', 'Expired')
    )
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    select_student = models.ForeignKey(Add_student, on_delete=models.CASCADE)
    reason_for_fine = models.CharField(max_length=120, null=True)
    amount = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=120, choices=STATUS)


class Add_timetable(models.Model):
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    upload_file = models.FileField(upload_to='assignment', blank=True)
    date_created = models.DateField(auto_now_add=True)

class Add_result(models.Model):
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    upload_file = models.FileField(upload_to='result', blank=True)
    date_created = models.DateField(auto_now_add=True)

class Assign_subject(models.Model):
    select_course = models.ForeignKey(Add_course, on_delete=models.CASCADE)
    select_semister = models.ForeignKey(Add_semister, on_delete=models.CASCADE)
    select_teacher = models.ForeignKey(Add_teacher, on_delete=models.CASCADE)
    select_subject = models.ForeignKey(Add_subject, on_delete=models.CASCADE)



#==========================================================================================================================
#==========================================================================================================================
#---------------------------------- COLLEGE DATABASES --------------------------------------------------------------------
#==========================================================================================================================
#==========================================================================================================================

class Add_event(models.Model):
    Choose_img = models.ImageField(upload_to='events')
    date_created = models.DateField(auto_now_add=True)
    event_title = models.CharField(max_length=120, null=True)
    event_description = models.CharField(max_length=1000, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Choose_img.open(self.Choose_img.path)

        if img.height > 100 or img.weight > 100:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Choose_img.path)


class Add_news(models.Model):
    Choose_img = models.ImageField(upload_to='news')
    date_created = models.DateField(auto_now_add=True)
    event_title = models.CharField(max_length=120, null=True)
    event_description = models.CharField(max_length=1000, null=True)




