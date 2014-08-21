"""
Question 3

Explain duck typing
Python is well known for it's use of duck typing. Please explain
what this is and write a simple example of it in action
"""

"Answer:"

"""Duck typing refers to a style of typing where the valid semantics of an object is ensure by its methods and attributes rather than its type itself. 

A example could be: "I'm in the forest and I see a superman flying like a duck, or swimming like a duck, superman is a duck"

In Pyhon if a function take an object and call object's quack() method, it does not check if the object type is a duck, it just call the method quack and if the object has not the method,
it just raise an error, otherwise continue. The correct way to handle the errors relies on programmer's hands.""" 


class Duck():
	def quack(self):
		print "Quack,Quack"


class Superman():
	def quack(self):
		print "Im superman and Im quacking"


def  I_want_quack(object):
	object.quack()


superman = Superman()
duck = Duck()
I_want_quack(superman)
I_want_quack(duck)



