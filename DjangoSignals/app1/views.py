import time
import string
import random
import threading
from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.models import User


def base(request):
    return render(request, 'base.html')


def createUser(request):
    # SOLUTION 2:
    thread = threading.current_thread().ident

    startTime = time.time()
    randomString = ''.join(random.choices(string.ascii_letters, k=4))
    exceptionMessage = ""

    try:
        with transaction.atomic():
            # create a new user to trigger the post_save signal
            User.objects.create_user(username=f"testUser_{randomString}", email=f"{randomString}@gmail.com", password=f"{randomString}")
            exceptionMessage = "[VIEW] Simulated failure to update email by signal of the newly created user inside view" 

            # SOLUTION 3:
            # simulate an error to roll back the transaction
            raise Exception(exceptionMessage)
    
    except Exception as e:
        print(e)

    # SOLUTION 1:
    endTime = time.time()
    totalTime = round((endTime - startTime), 2)

    context = {
        "totalTime": totalTime,
        "thread": thread,
        "exceptionMessage": exceptionMessage
    }

    return render(request, 'response.html', context=context)