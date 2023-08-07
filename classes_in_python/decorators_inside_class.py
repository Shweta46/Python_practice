class class_1 :
	def dec(func) :
		def inner(self) :
			print('Started.')
			func(self)
			print('Completed.\n')
		return inner
	@dec
	def func1(self) :
		print('Class 1.')

class class_2(class_1) :
	@class_1.dec
	def func2(self) :
		print('Class 2.')

llist = class_2()
llist.func1()
llist.func2()
