# Generated by Django 3.0.5 on 2020-12-24 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pycomment',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.PyPublication'),
        ),
        migrations.AlterField(
            model_name='pycomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pyconversation',
            name='receptor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pyconversation',
            name='sender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pymessage',
            name='conversation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Conversation', to='base.PyConversation'),
        ),
        migrations.AlterField(
            model_name='pymessage',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Me', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pypublication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]