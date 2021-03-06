# Generated by Django 2.2.4 on 2020-07-15 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=120, null=True)),
                ('course_code', models.CharField(max_length=120, null=True)),
                ('semister_or_year', models.CharField(choices=[('Semister', 'Semister'), ('Year', 'Year')], max_length=120)),
                ('no_of_semister_or_year', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choose_img', models.ImageField(upload_to='events')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('event_title', models.CharField(max_length=120, null=True)),
                ('event_description', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choose_img', models.ImageField(upload_to='news')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('event_title', models.CharField(max_length=120, null=True)),
                ('event_description', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_semister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semister_name', models.CharField(max_length=120, null=True)),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
            ],
        ),
        migrations.CreateModel(
            name='Add_subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=120, null=True)),
                ('subject_name', models.CharField(max_length=120, null=True)),
                ('select_subject_type', models.CharField(choices=[('Core', 'Core'), ('Optional', 'Optional')], max_length=120)),
                ('theory_marks', models.CharField(max_length=50, null=True)),
                ('Practical_marks', models.CharField(max_length=50, null=True)),
                ('select_course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
            ],
        ),
        migrations.CreateModel(
            name='Add_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=50, null=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('maritual_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated')], max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=120)),
                ('experience', models.CharField(choices=[('4 Year', '4 Year'), ('3 Year', '3 Year'), ('1 Year', '1 Year'), ('2 Year', '2 Year')], max_length=50)),
                ('date_of_birth', models.DateField()),
                ('teacher_picture', models.ImageField(upload_to='media')),
                ('address', models.TextField()),
                ('father_name', models.CharField(max_length=120, null=True)),
                ('phone_no', models.IntegerField()),
                ('insitute', models.CharField(blank=True, max_length=120, null=True)),
                ('name_of_exam', models.CharField(blank=True, max_length=120, null=True)),
                ('grade_gpa', models.CharField(max_length=100, null=True)),
                ('board', models.CharField(max_length=120, null=True)),
                ('passing_year', models.DateField()),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
            ],
        ),
        migrations.CreateModel(
            name='Assign_subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
                ('select_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_subject')),
                ('select_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Add_timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, upload_to='assignment')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
            ],
        ),
        migrations.CreateModel(
            name='Add_syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, upload_to='media/documents')),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
                ('select_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_subject')),
            ],
        ),
        migrations.CreateModel(
            name='Add_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=120, null=True)),
                ('student_cnic', models.IntegerField()),
                ('domicile', models.CharField(choices=[('FATA', 'FATA'), ('Charsadda', 'Charsadda'), ('Peshawar', 'Peshawar')], max_length=100)),
                ('email', models.CharField(max_length=50, null=True)),
                ('date_of_birth', models.CharField(max_length=50, null=True)),
                ('maritual_status', models.CharField(choices=[('Maried', 'Maried'), ('Single', 'Single'), ('Divorced', 'Divorced')], max_length=50)),
                ('Nationality', models.CharField(choices=[('Pakistani', 'Pakistani'), ('Other', 'Other')], max_length=120)),
                ('address', models.TextField()),
                ('user_picture', models.ImageField(upload_to='media')),
                ('father_name', models.CharField(max_length=50, null=True)),
                ('phone_no', models.IntegerField()),
                ('father_cnic', models.IntegerField()),
                ('father_ocupation', models.CharField(max_length=50, null=True)),
                ('monthly_income', models.IntegerField()),
                ('institute_name', models.CharField(blank=True, max_length=120, null=True)),
                ('exam_name', models.CharField(blank=True, max_length=120, null=True)),
                ('total_marks', models.IntegerField()),
                ('obtain_marks', models.IntegerField()),
                ('grade', models.IntegerField(choices=[('A', 'A'), ('Fail', 'Fail'), ('C', 'C'), ('B', 'B')])),
                ('board_roll_no', models.IntegerField()),
                ('passing_year', models.DateField()),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
            ],
        ),
        migrations.CreateModel(
            name='Add_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, upload_to='result')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
            ],
        ),
        migrations.CreateModel(
            name='Add_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=120, null=True)),
                ('programming_technology', models.CharField(max_length=120, null=True)),
                ('select_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Expired', 'Expired')], max_length=120)),
                ('date_created', models.DateField()),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
                ('select_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_student')),
            ],
        ),
        migrations.CreateModel(
            name='Add_fine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_fine', models.CharField(max_length=120, null=True)),
                ('amount', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Expired', 'Expired')], max_length=120)),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
                ('select_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_student')),
            ],
        ),
        migrations.CreateModel(
            name='Add_assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, upload_to='assignment')),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_course')),
                ('select_semister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_semister')),
                ('select_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Add_subject')),
            ],
        ),
    ]
