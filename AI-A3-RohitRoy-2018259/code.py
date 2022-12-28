from durable.lang import *

# This is the ruleset of choices taken by the student during input
# It contains the cgpa of the student and all the interest areas that the student is interested in
with ruleset('choices'):

	# Machine Learning is one interest of student
	@when_all(m.interest_list.anyItem((item=='Machine Learning')))
	def func1(c):
		c.assert_fact('interest_field', {'interest': 'Machine Learning'})

	# Networking is one interest of student
	@when_all(m.interest_list.anyItem((item=='Networking')))
	def func2(c):
		c.assert_fact('interest_field', {'interest': 'Networking'})

	# Web development is one interest of student
	@when_all(m.interest_list.anyItem((item=='Web development')))
	def func3(c):
		c.assert_fact('interest_field', {'interest': 'Web development'})

	# Electronics is one interest of student
	@when_all(m.interest_list.anyItem((item=='Electronics')))
	def func4(c):
		c.assert_fact('interest_field', {'interest': 'Electronics'})

	# Social Science is one interest of student
	@when_all(m.interest_list.anyItem((item=='Social Science')))
	def func5(c):
		c.assert_fact('interest_field', {'interest': 'Social Science'})

	# Biology is one interest of student
	@when_all(m.interest_list.anyItem((item=='Biology')))
	def func6(c):
		c.assert_fact('interest_field', {'interest': 'Biology'})

	# Animation is one interest of student
	@when_all(m.interest_list.anyItem((item=='Animation')))
	def func7(c):
		c.assert_fact('interest_field', {'interest': 'Animation'})

	# student's cgpa is >= 8
	@when_all((m.cgpa >= 8.0))
	def func8(c):
		ans = input("Your cgpa is very good...would you like to pursue Higher studies ?  (y/n) : ")
		c.assert_fact('Higher_studies', {'response': ans})

	# student's cgpa is < 5
	@when_all((m.cgpa < 5))
	def func9(c):
		c.assert_fact({"subject": "\nYour cgpa is weak...you should focus more on your studies! :)"})

	# output of ruleset 'choices'
	@when_all(+m.subject)
	def output1(c):
		print("{0}".format(c.m.subject))


# this is the ruleset of interest_field
# It contains a particular interest of the student
with ruleset('interest_field'):

	# interest is Machine Learning
	@when_all((m.interest=='Machine Learning'))
	def gunc1(d):
		print()
		print("Since you are interested in Machine Learning, we want to know your experience in it !")
		print("Enter 1 for yes and 0 for no (Enter these carefully !)")
		count = 0

		# here we ask the student if he took these courses in Machine Learning
		count += int(input("Did you take Machine Learning ?  (1/0) : "))
		count += int(input("Did you take Natural Language Processing ?  (1/0) : "))
		count += int(input("Did you take Artificial Intelligence ?  (1/0) : "))
		print()
		d.assert_fact('experience', {'field_name': 'Machine Learning', 'count': count})

	# interest is Networking
	@when_all((m.interest=='Networking'))
	def gunc2(d):
		print()
		print("Since you are interested in Networking, we want to know your experience in it !")
		print("Enter 1 for yes and 0 for no (Enter these carefully !)")
		count = 0

		# here we ask the student if he took these courses in Networking
		count += int(input("Did you take Computer Networks ?  (1/0) : "))
		count += int(input("Did you take Network Security ?  (1/0) : "))
		count += int(input("Did you take Computer Security ?  (1/0) : "))
		print()
		d.assert_fact('experience', {'field_name': 'Networking', 'count': count})

	# interest is Web development
	@when_all((m.interest=='Web development'))
	def gunc3(d):
		print()
		print("Since you are interested in Web development, we want to know your experience in it !")
		print("Enter 1 for yes and 0 for no (Enter these carefully !)")
		count = 0

		# here we ask the student if he took these courses in Web development
		count += int(input("Did you take Information Retrieval ?  (1/0) : "))
		count += int(input("Did you take DBMS ?  (1/0) : "))
		count += int(input("Did you take Foundations of Computer Security ?  (1/0) : "))
		print()
		d.assert_fact('experience', {'field_name': 'Web development', 'count': count})

	# interest is Electronics
	@when_all((m.interest=='Electronics'))
	def gunc4(d):
		print()
		print("Since you are interested in Electronics, we want to know your experience in it !")
		print("Enter 1 for yes and 0 for no (Enter these carefully !)")
		count = 0

		# here we ask the student if he took these courses in Electronics
		count += int(input("Did you take Basic Electronics ?  (1/0) : "))
		count += int(input("Did you take Digital Circuits ?  (1/0) : "))
		count += int(input("Did you take Digital Signal Processing ?  (1/0) : "))
		print()
		d.assert_fact('experience', {'field_name': 'Electronics', 'count': count})

	# interest is Social Science
	@when_all((m.interest=='Social Science'))
	def gunc5(d):
		print()
		print("Since you are interested in Social Science, we want to know your experience in it !")
		print("Enter 1 for yes and 0 for no (Enter these carefully !)")
		count = 0

		# here we ask the student if he took these courses in Social Science
		count += int(input("Did you take Urban Space and Political Power ?  (1/0) : "))
		count += int(input("Did you take Neuroscience of Decision Making ?  (1/0) : "))
		count += int(input("Did you take Environmental Sciences ?  (1/0) : "))
		print()
		d.assert_fact('experience', {'field_name': 'Social Science', 'count': count})

	# interest is Biology
	@when_all((m.interest=='Biology'))
	def gunc6(d):
		print()
		print("Since you are interested in Biology, we want to know your experience in it !")
		print("Enter 1 for yes and 0 for no (Enter these carefully !)")
		count = 0

		# here we ask the student if he took these courses in Biology
		count += int(input("Did you take Computational Gastronomy ?  (1/0) : "))
		count += int(input("Did you take Computing for Medicine ?  (1/0) : "))
		count += int(input("Did you take Machine Learning for Biomedical Applications ?  (1/0) : "))
		count += int(input("Did you take BDMH ?  (1/0) : "))
		print()
		d.assert_fact('experience', {'field_name': 'Biology', 'count': count})

	# interest is Animation
	@when_all((m.interest=='Animation'))
	def gunc7(d):
		print()
		print("Since you are interested in Animation, we want to know your experience in it !")
		print("Enter 1 for yes and 0 for no (Enter these carefully !)")
		count = 0

		# here we ask the student if he took these courses in Animation
		count += int(input("Did you take Introduction to Animation and Graphics ?  (1/0) : "))
		count += int(input("Did you take 3D Animation Film Making ?  (1/0) : "))
		count += int(input("Did you take Affective Computing ?  (1/0) : "))
		print()
		d.assert_fact('experience', {'field_name': 'Animation', 'count': count})

	# output of ruleset 'interest_field'
	@when_all(+m.interest)
	def output2(d):
		pass


# This is the ruleset of experience. It pertains to the experience of the student in a particular interest/field
# This contains the field name and count of courses the student has done in it
with ruleset('experience'):

	# field is Machine Learning and count of courses done in it is >= 2
	@when_all((m.field_name=='Machine Learning') & (m.count>=2))
	def hunc1(e):
		e.assert_fact({'subject': 'YOU CAN PURSUE MACHINE LEARNING !'})
	# field is Machine Learning and count of courses done in it < 2
	@when_all((m.field_name=='Machine Learning') & (m.count<2))
	def hunc2(e):
		pass

	# field is Networking and count of courses done in it is >= 2
	@when_all((m.field_name=='Networking') & (m.count>=2))
	def hunc3(e):
		e.assert_fact({'subject': 'YOU CAN PURSUE NETWORKING !'})
	# field is Networking and count of courses done in it is < 2
	@when_all((m.field_name=='Networking') & (m.count<2))
	def hunc4(e):
		pass

	# field is Web development and count of courses done in it is >= 2
	@when_all((m.field_name=='Web development') & (m.count>=2))
	def hunc5(e):
		e.assert_fact({'subject': 'YOU CAN PURSUE WEB DEVELOPMENT !'})
	# field is Web development and count of courses done in it is < 2
	@when_all((m.field_name=='Web development') & (m.count<2))
	def hunc6(e):
		pass

	# field is Electronics and count of courses done in it is >= 2
	@when_all((m.field_name=='Electronics') & (m.count>=2))
	def hunc7(e):
		e.assert_fact({'subject': 'YOU CAN PURSUE ELECTRONICS !'})
	# field is Electronics and count of courses done in it is < 2
	@when_all((m.field_name=='Electronics') & (m.count<2))
	def hunc8(e):
		pass

	# field is Social Science and count of courses done in it is >= 2
	@when_all((m.field_name=='Social Science') & (m.count>=2))
	def hunc9(e):
		e.assert_fact({'subject': 'YOU CAN PURSUE SOCIAL SCIENCE !'})
	# field is Social Science and count of courses done in it is < 2
	@when_all((m.field_name=='Social Science') & (m.count<2))
	def hunc10(e):
		pass

	# field is Biology and count of courses done in it is >= 2
	@when_all((m.field_name=='Biology') & (m.count>=2))
	def hunc11(e):
		e.assert_fact({'subject': 'YOU CAN PURSUE BIOLOGY !'})
	# field is Biology and count of courses done in it is < 2
	@when_all((m.field_name=='Biology') & (m.count<2))
	def hunc12(e):
		pass

	# field is Animation and count of courses done in it is >= 2
	@when_all((m.field_name=='Animation') & (m.count>=2))
	def hunc13(e):
		e.assert_fact({'subject': 'YOU CAN PURSUE ANIMATION !'})
	# field is Animation and count of courses done in it is < 2
	@when_all((m.field_name=='Animation') & (m.count<2))
	def hunc14(e):
		pass

	# output of ruleset 'experience'
	@when_all(+m.subject)
	def output3(e):
		print("{0}".format(e.m.subject))


# This is the ruleset Higher_studies
# It contains the response of the student (y/n) which depicts if the student wants to opt for it or not
with ruleset('Higher_studies'):

	# response of the student for higher studies is yes
	@when_all((m.response=='y'))
	def iunc1(f):
		f.assert_fact({'subject': 'YOU CAN OPT FOR HIGHER STUDIES !'})

	# response of the student for higher studies is no 
	@when_all((m.response!='y'))
	def iunc2(f):
		pass

	# output if ruleset 'Higher_studies'
	@when_all(+m.subject)
	def output4(f):
		print("{0}".format(f.m.subject))



print("Welcome to our career advisory system ! :)\n")

# These are the available career options in interest_areas_available
interest_areas_available = ['Machine Learning', 'Networking', 'Web development', 'Electronics', 'Social Science', 'Biology', 'Animation']

# interest_areas captures the career areas that the student in interested in
interest_areas = []
for interest in interest_areas_available :
	ans = input("Do you like {0} ? (y/n) : ".format(interest))
	if (ans=='y'):
		interest_areas.append(interest)

print()

# cgpa is the CGPA of the student
cgpa = float(input("Please enter your cgpa : "))
print()

assert_fact('choices', {'interest_list': interest_areas, 'cgpa': cgpa})