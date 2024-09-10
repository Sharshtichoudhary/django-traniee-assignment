from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import time
import threading
#  Ques1 - By default, Django signals are executed synchronously
# A specific event occurs in your Django application, triggering the emission of a signal.In my example, i am saving a new object of MyModel.
# When the signal is emitted, Django immediately calls each registered receiver function. These functions execute in the same order they were registered.


@receiver(post_save, sender=MyModel)
def handle_mymodel_save(sender, instance, created, **kwargs):
    if created:
        print(f"New instance created: {instance}")
        time.sleep(5)  # 5 sec delay for other task like sending email or otp verification
        print(f"Finished processing for {instance.name}")
    else:
        print(f"Instance updated: {instance}")



# Ques2 -Yes, by default, Django signals run in the same thread as the caller that the signal handler executes within the same process and thread as the code that triggers the signal.
@receiver(post_save, sender=MyModel)
def mymodel_post_save(sender, instance, created, **kwargs):
    print(f"Signal Handler: Running in thread {threading.get_ident()}")



# Ques3 -Django signals run in the same database transaction as the caller.If the transaction is rolled back, the changes made by the signal handler will also be rolled back.
@receiver(post_save, sender=MyModel)
def mymodel_post_save(sender, instance, created, **kwargs):
    if created:
        # Create another instance within the same transaction
        from .models import NewModel
        NewModel.objects.create(name="Related instance")