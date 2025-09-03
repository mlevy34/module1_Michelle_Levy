Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 09:44:33) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print('michelle')
michelle
>>> 
>>> def hello1(name) :
	print('hello',name)

	
>>> hello1(michelle)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    hello1(michelle)
NameError: name 'michelle' is not defined
>>> 
>>> 
>>> hello1('michelle')
hello michelle
>>> hello1('ml')
hello ml
>>> 