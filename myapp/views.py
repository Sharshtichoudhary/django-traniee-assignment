
# Create your views here.
from django.db import transaction
from myapp.models import MyModel, NewModel

def test_transaction_rollback():
    with transaction.atomic():
        obj = MyModel.objects.create(name="Shrishti ", description="Rollback instance")
        # Check if Newmodel instance is created
        print("Before rollback:")
        print("NewModel count:", NewModel.objects.count())
        
        # Rollback the transaction
        transaction.set_rollback(True)

    # Check if AnotherModel instance was rolled back
    print("After rollback:")
    print("NewModel count:", NewModel.objects.count())