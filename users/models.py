from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, is_staffer, is_manager, restaurant, password=None):
        if not username:
            raise ValueError("User must have a username.")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            # first_name = first_name,
            # last_name = last_name,
            is_manager = is_manager,
            is_staffer=is_staffer,
            restaurant=restaurant
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(            
            username=username,
            email='arain@gmail.com',
            is_staffer=False,
            is_manager=False,
            restaurant='Not',
            password=password,
        )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id                  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username            = models.CharField(unique=True, max_length=30)
    first_name          = models.CharField(max_length=30, blank=True, null=True)
    last_name           = models.CharField(max_length=30, blank=True, null=True)
    email               = models.EmailField(max_length=254, blank=True, null=True)
    is_active           = models.BooleanField(default=True)
    is_staffer          = models.BooleanField(default=False)
    is_manager          = models.BooleanField(default=False)
    restaurant          = models.CharField(max_length=70, default='Not Specified')
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    date_joined         = models.DateTimeField(auto_now_add=False, blank=True, null=True)  
    last_login          = models.DateTimeField(auto_now=False, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True


# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # # Create your models here.


# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
#     is_staffer = models.BooleanField(default=False)
#     pic = models.ImageField(upload_to="profile_pics", height_field=None, width_field=None, 
#                             max_length=None, blank=True, null=True)

#     def __str__(self):
#         return self.username

#     def create_user(self, email, username, password=None):
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username
#         )
#         user.set_password(password)
#         user.save(self._db)
#         return user

        
  