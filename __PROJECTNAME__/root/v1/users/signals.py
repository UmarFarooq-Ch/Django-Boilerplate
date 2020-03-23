# standard library
from functools import wraps

# third party imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


def disable_for_loaddata(signal_handler):
    """
    Decorator that turns off signal handlers when loading fixture data.
    """

    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        if kwargs['raw']:
            return
        signal_handler(*args, **kwargs)

    return wrapper


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
@disable_for_loaddata
def update_user_handler(sender, instance, created, **kwargs):
    """updates updated_at field of User model

    Arguments:
        sender  -- auth user model name
        instance -- newly created user object instance
        created -- boolean flag to check if instance is created
    """
    if not created:
        return

    # DO YOUR TASK HERE
    # # # EXAMPLE # # #
    # if instance.user_type == 1:
    #     Doctor.objects.get_or_create(user=instance)
    #     group = Group.objects.get(id=instance.user_type)
    #     instance.groups.add(group)
    #
    # elif instance.user_type == 2:
    #     Patient.objects.get_or_create(user=instance)
    #     group = Group.objects.get(id=instance.user_type)
    #     instance.groups.add(group)
