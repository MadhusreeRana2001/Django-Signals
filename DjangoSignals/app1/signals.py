import time
import threading
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def userPostSaveHandler(sender, instance, created, **kwargs):
    print("Signal handler for User started.")
    # SOLUTION 2:
    if created:
        print(f"[SIGNAL] Signal triggered in thread: {threading.current_thread().ident}")

        # SOLUTION 3:
        try:
            oldEmail = instance.email
            randomString = oldEmail.split("@")[0]
            user = authenticate(username=instance.username, password=randomString)
            if user is not None:
                instance.email = f"new_{oldEmail}"
                instance.save()
            else: print("User not authenticated")

        except Exception as e:
            print(f"[SIGNAL] Error while updating the email of the user: {e}")

        # SOLUTION 1:
        # simulate a delay of 2 seconds
        time.sleep(2)
        print("Signal handler for User finished.")