# Generated by Django 5.0.1 on 2024-01-28 17:27

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import kilid_app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('province_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AgencyManager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('agency_manger_id', models.IntegerField(primary_key=True, serialize=False)),
                ('usr', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usr_is_%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EstateAgency',
            fields=[
                ('state_agency_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('phone_no', models.CharField(default='1234567890', max_length=10, validators=[kilid_app.models.only_int, django.core.validators.MinLengthValidator(10)], verbose_name='Phone number')),
                ('number_of_employees', models.IntegerField()),
                ('logo', models.ImageField(upload_to='images')),
                ('address', models.CharField(max_length=255)),
                ('agency_manager', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='kilid_app.agencymanager')),
            ],
        ),
        migrations.CreateModel(
            name='AgencyAdvisor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('advisor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('usr', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='usr_is_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('state_agency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='kilid_app.estateagency')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('area', models.IntegerField()),
                ('year', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('parking', models.IntegerField()),
                ('storage_area', models.IntegerField()),
                ('loby_area', models.IntegerField()),
                ('sports_hall_area', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('elevator', models.BooleanField()),
                ('balcony', models.BooleanField()),
                ('security_guard', models.BooleanField()),
                ('pool', models.BooleanField()),
                ('sauna', models.BooleanField()),
                ('jacuuzi', models.BooleanField()),
                ('air_conditioning', models.BooleanField()),
                ('clearance_hall', models.BooleanField()),
                ('central_antenna', models.BooleanField()),
                ('remote_door', models.BooleanField()),
                ('roof_guarden', models.BooleanField()),
                ('deal_type', models.CharField(max_length=150)),
                ('city', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='kilid_app.city')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('ad_id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('ad_code', models.CharField(max_length=7, unique=True, validators=[django.core.validators.MinLengthValidator(7), kilid_app.models.only_int])),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=512)),
                ('mortgage', models.BooleanField()),
                ('rent', models.BooleanField()),
                ('buy', models.BooleanField()),
                ('exchange', models.BooleanField()),
                ('collaborative', models.BooleanField()),
                ('convertible', models.BooleanField()),
                ('presell', models.BooleanField()),
                ('administrative_position', models.BooleanField()),
                ('borrower', models.BooleanField()),
                ('newly_build', models.BooleanField()),
                ('in_proportionate_share', models.BooleanField()),
                ('main_image', models.ImageField(upload_to='')),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('image4', models.ImageField(upload_to='')),
                ('image5', models.ImageField(upload_to='')),
                ('estate_agency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='kilid_app.estateagency')),
                ('house', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='kilid_app.house')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('province', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='kilid_app.province')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='kilid_app.region'),
        ),
    ]