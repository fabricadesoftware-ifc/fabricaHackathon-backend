from django.dispatch import Signal, receiver
from hackathon.tasks import send_applications_accepted_emails_to_students

applications_accepted_changed = Signal()

@receiver(applications_accepted_changed)
def handle_applications_accepted_change(sender, instance, old_value, new_value, **kwargs):
    if new_value:
        send_applications_accepted_emails_to_students.delay(instance)