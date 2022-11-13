# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog")
# from django.conf import settings

# import sys 
# sys.path.append('/Users/deepakmarathe/Documents/code/my/django-blog')

# import django 
# django.setup()


from users.models import User
print(User.objects.all().count())
for user in User.objects.all():
    print(user.email)