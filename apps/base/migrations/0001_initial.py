# Generated by Django 3.0.5 on 2020-12-13 02:22

import apps.base.models.usercustom
import apps.base.rename_image
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=30, verbose_name='First_name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last_Nanme')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Masculine'), ('U', 'Undefined')], default='U', max_length=64, verbose_name='Gender')),
                ('avatar', models.ImageField(blank=True, default='avatar/default_avatar.png', max_length=255, null=True, storage=apps.base.rename_image.RenameImage(), upload_to=apps.base.models.usercustom.image_path)),
                ('day_of_birth', models.DateField(blank=True, null=True, verbose_name='Gender')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='PyConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('receptor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conversation',
                'verbose_name_plural': 'Conversations',
            },
        ),
        migrations.CreateModel(
            name='PyPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='Content')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='PyMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('conversation_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Conversation', to='base.PyConversation')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Me', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='PyFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='Accepted')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('receptor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Receptor', to=settings.AUTH_USER_MODEL)),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friend',
                'verbose_name_plural': 'Friends',
            },
        ),
        migrations.CreateModel(
            name='PyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes')),
                ('content', models.CharField(max_length=300, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PyPublication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
