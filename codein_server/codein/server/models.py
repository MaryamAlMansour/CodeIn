from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.
#Extending the abstractBaseUser class.

class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    USER_CHOICES = ((1, 'Regular User'), (2, 'Developer'))
    developer = models.IntegerField(choices=USER_CHOICES, default='1')
    python = models.BooleanField(default=False)
    Java = models.BooleanField(default=False)
    C = models.BooleanField(default=False)
    Ruby = models.BooleanField(default=False)
    HTML = models.BooleanField(default=False)
    CSS = models.BooleanField(default=False)
    JavaScript = models.BooleanField(default=False)
    OtherLanguages = models.CharField(max_length=12)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    ## define the user manager class for User
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''

        return self.get_short_name()
