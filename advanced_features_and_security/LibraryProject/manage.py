from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

# Get content type for Book
book_ct = ContentType.objects.get_for_model(Book)

# Create permissions
can_view = Permission.objects.get(codename='can_view', content_type=book_ct)
can_create = Permission.objects.get(codename='can_create', content_type=book_ct)
can_edit = Permission.objects.get(codename='can_edit', content_type=book_ct)
can_delete = Permission.objects.get(codename='can_delete', content_type=book_ct)

# Create groups
editors, _ = Group.objects.get_or_create(name='Editors')
viewers, _ = Group.objects.get_or_create(name='Viewers')
admins, _ = Group.objects.get_or_create(name='Admins')

# Assign permissions to groups
editors.permissions.set([can_create, can_edit])
viewers.permissions.set([can_view])
admins.permissions.set([can_view, can_create, can_edit, can_delete])
