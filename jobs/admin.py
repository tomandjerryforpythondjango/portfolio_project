from django.contrib import admin
from jobs.models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
	class Meta:
		model = Job
		fields = '__all__'

admin.site.register(Job, JobAdmin)