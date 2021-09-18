from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.expressions import CombinedExpression
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail

# def users_imgs_path(instance, filename):
#     return 'images/Users/{0}/{1}'.format(instance.get_full_name(), filename)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save a user with the given Email, first name, Last Name, and password.
        """
        if not email:
            raise ValueError('The User must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email = email, 
            first_name = first_name, 
            last_name = last_name, 
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)
    

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    """
    Users within the Platfy authentication system are represented by this
    model.

    Email, first name, last name and password are required. Other fields are optional.
    """
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists.'),
        },
    )
    first_name = models.CharField(
        _('first name'),
        max_length=100,
        blank=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=100,
        blank=True
    )
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
    date_joined = models.DateTimeField(
        _('date joined'),
        default = timezone.now 
    )
    objects                     = UserManager()

    USERNAME_FIELD              = 'email'
    REQUIRED_FIELDS             = ['first_name', 'last_name']
    class Meta:
        verbose_name            = _('user')
        verbose_name_plural     = _('users')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s'% (self.first_name, self.last_name)
        return full_name.strip()


    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, self.email, **kwargs)


class FacebookAccounts(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    id              = models.CharField(max_length=100, primary_key=True)
    code            = models.CharField(max_length=1000)
    access_token    = models.CharField(max_length=1000)
    name            = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'facebook account'
        verbose_name_plural = 'facebook accounts'