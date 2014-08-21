"""
Question 2
Create a Many­to­Many relationship
Create two models connected by a many­to­many relationship.
Model 1:
Campus
city
state
name

Model 2:
Student
first name
last name
Bearing in mind that a student can belong to more than one campus,
set up their relationship with an additional field denoting if a
particular campus is their primary campus.
"""

class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)


class Campus(models.Model):
	students = models.Many­ToManyField(Student,through='StudentBelongs')
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

class StudentBelongs(models.Model):
	campus = models.ForeignKey(Campus)
	student = models.ForeignKey(Student)
	is_primary = models.BooleanField(default=False)