"""
Question 4

Manipulating API Data
Fetch the JSON data from
http://dev.dryan.net.s3.amazonaws.com/students.json then sort the
results by each entries "grade" attribute, ascending order of
college completion.
"""


import simplejson
import urllib2
 
r = urllib2.urlopen('http://dev.dryan.net.s3.amazonaws.com/students.json')

#There is an error in the json, because JSON does not support \xNN scape,
#to fix that Im replacing it for \u00NN

grades = ["freshman","sophomore","junior","senior"] 

data = simplejson.loads(r.read().replace('\\x', '\\u00'))

key_function = lambda x: grades.index(x.get('grade').lower())

data_sorted = sorted(data,key=key_function)
print data_sorted
