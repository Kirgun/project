from django.shortcuts import render
from .models import Staff

def main_menu(request):
	staffs = Staff.objects.all()
	print(Staff)
	title = "Main"
	context = {
 		"title_docum":title,
		"staffs":staffs
		}
	return render(request,"main_menu.html",context)