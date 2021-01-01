import django_filters

from .models import *

class  Add_studentFilter(django_filters.FilterSet):
	first_name = django_filters.CharFilter(field_name='first_name')
	class Meta:
		models = Add_student
		fields = ['first_name']
