# Generated by Django 4.0.1 on 2022-01-26 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can mark returned', 'Set book as returned'),)},
        ),
    ]