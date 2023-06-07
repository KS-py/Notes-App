from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Note
from .forms import CreateNote

def home(response):
	return render(response, "home.html", {"Notes": Note.objects.all})

def create(response):
	if response.method == "POST":
		form = CreateNote(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			c = form.cleaned_data["text"]
			note = Note(name=n, content=c)
			note.save()
		return HttpResponseRedirect("/home")
	else:
		form = CreateNote()

	return render(response, "create.html", {"form": form})

def edit(response, id):
	list_to_edit = Note.objects.get(id=id)

	if response.method == 'POST':
			list_to_edit.name = response.POST.get("title")
			print(list_to_edit.name)
			list_to_edit.content = response.POST.get("content")
			print(list_to_edit.content)
			list_to_edit.save()
			return HttpResponseRedirect("/home")
	return render(response, "edit_list.html", {"list_to_edit": list_to_edit})

def delete(response, id):
	list_to_delete = Note.objects.get(id=id)

	if response.method == 'POST':
		list_to_delete.delete()
		return HttpResponseRedirect("/home")

	return render(response, "delete.html", {"list_to_delete": list_to_delete})


