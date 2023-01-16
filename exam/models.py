from django.db import models

from student.models import Student

class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

class QuestionSheet(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title =models.CharField(max_length=150)
    file =models.FileField(upload_to='docs/')
    total_marks=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.course_name} --> {self.title}"

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    question_sheet =models.ForeignKey(QuestionSheet,on_delete=models.CASCADE)
    answer =models.FileField(upload_to='answer')
    marks = models.PositiveIntegerField(default=0,blank=True)



