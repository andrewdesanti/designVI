from django.shortcuts import render

posts = [
{
	
	'author': 'bruh',
	'title': 'huh',
	'content': 'deedeetdeedeedeet',
	'date_posted' : 'today'

},
{
	
	'author': 'bruh',
	'title': 'huhw2',
	'content': 'deedeetdeedeedeet',
	'date_posted' : 'today'

},
{
	
	'author': 'bruh',
	'title': 'huh3',
	'content': 'deedeetdeedeedeet',
	'date_posted' : 'today'

}


]




def home(request):
	context = {
		'posts': posts

	}
	return render(request, 'app/home.html', context)

def about(request):
	return render(request, 'app/about.html')