from asyncio import streams
import email
import profile
from tkinter import CASCADE
from django.db import models

# Create your models here.
class School(models.Model):
    school_name=models.CharField(max_length=15)
    school_address=models.CharField(max_length=30)
    school_email=models.EmailField(max_length=45)
    location=models.CharField(max_length=24)
    contact=models.IntegerField()

class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField(max_length=45)
    GENDER_CHOICES=(
        ("F","Female"), ("M","Male"), ("P","Prefer not to say")
    )
    gender=models.CharField(max_length=2,null=True,choices=GENDER_CHOICES)
    adress=models.TextField(max_length=20)
    STREAM_CHOICES=(
        ("A","Adalab"),("H","Hopperlab"),("A","Anitab")
    )
    stream=models.CharField(max_length=2,null=True,choices=STREAM_CHOICES)
    ROOM_CHOICES=(
        ("C","Chalbi"),("S","Serengeti"),("T","Tanga"),("M","Manda"),
        ("K","Kivu"),("K","Kalahari"),("A","Abaderes"),("S","Stavo"),
        ("M","Mara"),("S","Serengeti"),("R","Rusinga")
    )
    room=models.CharField(max_length=7,null=True,choices=ROOM_CHOICES)
    age=models.PositiveBigIntegerField(2)
    admission_number=models.IntegerField()
    school=models.ForeignKey('School',on_delete=models.CASCADE,null=True,related_name="School_Student")
    phonenumber=models.IntegerField()
    emergency_contact=models.IntegerField()

class Student_Id(models.Model):
    Student=models.CharField(max_length=45)
    date_issued=models.DateField()
    expiry_date=models.DateField
    profile_picture=models.ImageField()

class Teachers_Panel(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    
    UNITSPECIALITY_CHOICES=(
        ("K","Kotlin"), ("P","Python"), ("R","Research"), ("P","Personal Development"),
        ("N","Navigating Your Journey"), ("P","Product Design"), ("I","Internet Of Things"), ("D","Django"),
        ("D","Design"), ("J","Java Script"), ("R","React"),
    )
    unit_speciality=models.CharField(max_length=15,null=True,choices=UNITSPECIALITY_CHOICES)
    contact=models.PositiveBigIntegerField()
    email=models.EmailField(max_length=45)
    profile=models.ImageField()

class School_Fees(models.Model):
    Student=models.ForeignKey('Student',on_delete=models.CASCADE,null=True,related_name="Student_School_Fees")
    full_fees=models.ImageField()
    amount_paid=models.IntegerField()
    balance=models.ImageField()
    reciept=models.CharField(max_length=4)


class Reciept(models.Model):
    Student=models.ForeignKey('Student',on_delete=models.CASCADE,null=True,related_name="Student_Reciept")
    school_account=models.ForeignKey('School',on_delete=models.CASCADE,null=True,related_name="School_Reciept")
    amount_paid=models.IntegerField(100)
    amount_balance=models.IntegerField()
    receipt_number=models.IntegerField()

class School_Account(models.Model):
    school=models.ForeignKey('School',on_delete=models.CASCADE,null=True,related_name="School_Account_School")
    account_name=models.CharField(max_length=15)
    account_number=models.IntegerField()

class Staff(models.Model):
    First_name=models.CharField(max_length=15)
    Last_name=models.CharField(max_length=15)
    OCCUPATION_CHOICES=(
        ("C","Chef"),("G","Gardener"),("M","Matron"),("T","Trainors"),("A","Accountant"),
        ("E","Event Co-ordinator"),("E","Engineer"),("G","Gatemen"),("C","Cooks"),("D","Dean"),
    )
    Occupation=models.CharField(max_length=8,null=True,choices=OCCUPATION_CHOICES)
    Email=models.EmailField(max_length=45)
    Contact=models.IntegerField()

class Academic_Analysis(models.Model):
    student=models.ForeignKey("Student",on_delete=models.CASCADE,null=True,related_name="Academic_Analysis_Student")
    GRADE_CHOICES=(
        ("A","A"),("B","B"),("C","C"),("D","D"),("E","E"),("F","F"),
    
    )
    grade=models.CharField(max_length=4,null=True,choices=GRADE_CHOICES)

class Library_Management(models.Model):
    student=models.ForeignKey("Student",on_delete=models.CASCADE,null=True,related_name="Library_Management_Student")
    Date_issued=models.DateTimeField()
    Return_date=models.DateTimeField()



