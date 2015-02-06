from polls.models import Question
from sof.models import SofQuestions
from django.core.files import File

def run():
	print "Hello"
	with open('test.txt', 'w+') as f:
		myfile = File(f)

		for i in SofQuestions.objects.all()[:5]:
		
			myfile.write ("<" + str(i.post_id)+ ">")
			myfile.write ("<" + str(i.score) + ">")
			myfile.write ("<" + i.title + "> . \n")

	myfile.closed()
	f.closed()