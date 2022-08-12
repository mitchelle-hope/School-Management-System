from django.contrib import admin

from system.models import Academic_Analysis, Library_Management, Reciept, School, School_Account, School_Fees, Staff, Student, Student_Id, Teachers_Panel

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Student_Id)
admin.site.register(School_Fees)
admin.site.register(Reciept)
admin.site.register(School_Account)
admin.site.register(Staff)
admin.site.register(Academic_Analysis)
admin.site.register(Library_Management)
