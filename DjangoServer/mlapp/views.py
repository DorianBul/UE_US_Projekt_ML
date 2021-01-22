import subprocess, os
from django.shortcuts import render
from .forms import ImageForm
from django.contrib.auth.decorators import login_required

from .activityLogger import dbManager

@login_required
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Get the current instance object to display in the template
            img_obj = form.instance

            # Process ML for the result
            COMMAND_BASE = "python F:/Uczelniane/Projekty/US/Projekt/server/mlapp/CatOrDog/loadModelToPredict.py "
            command = COMMAND_BASE + str(img_obj.image.url)
            # print("executing command: " + command)
            retVal = os.popen(command).read()
            retVal =  retVal.rstrip()
            # print("executing command result: " + retVal)

            dbManager.AddActionRecord(str(request.user), "Cat or Dog", "{} <-> {}({})".format(retVal, str(img_obj.title), str(img_obj.image.url)))

            return render(request, 'mlapp1/form.html', {'form': form, 'img_obj': img_obj, 'retVal': retVal})
        else:
            print("---\nInvalid form uploaded\n---")
    else:
        form = ImageForm()
    return render(request, 'mlapp1/form.html', {'form': form})

