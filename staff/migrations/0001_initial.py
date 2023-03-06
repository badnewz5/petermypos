# Generated by Django 4.1.7 on 2023-02-20 18:23

from django.db import migrations, models
import django.utils.timezone
import staff.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('national_id', models.IntegerField(null=True, verbose_name='National ID Number')),
                ('phone_number', models.CharField(max_length=50, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='User name')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('dob', models.DateField(blank=True, default='1990-01-01', max_length=250, verbose_name='Date of birth')),
                ('nationality', models.CharField(blank=True, default='Kenyan', max_length=50, null=True, verbose_name='Nationality')),
                ('postal_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Postal address')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='City')),
                ('street', models.CharField(blank=True, max_length=200, null=True, verbose_name='Street or road')),
                ('house', models.CharField(blank=True, max_length=200, null=True, verbose_name='House or plot number')),
                ('occupation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Occupation')),
                ('employer', models.CharField(blank=True, max_length=250, verbose_name='Employer')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('other', 'Other')], default='single', max_length=50, verbose_name='Marital Status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'staff',
                'verbose_name_plural': 'staff',
            },
            managers=[
                ('objects', staff.managers.UserManager()),
            ],
        ),
    ]
