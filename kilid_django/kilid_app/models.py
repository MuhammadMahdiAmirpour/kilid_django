from django.db import models
from django.core.validators import ValidationError
from django.core.validators import MinLengthValidator, int_list_validator
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     user_id = models.IntegerField(primary_key=True, )
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     username = models.CharField(max_length=150)
#     password = models.CharField(max_length=150)
#     email = models.EmailField()

def only_int(value):
    if not value.isdigit():
        raise ValidationError("field contains non digit charcters")

class Province(models.Model):
    province_id = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=150)

class Region(models.Model):
    region_id = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=150)
    province = models.ForeignKey(Province, default=None, on_delete=models.DO_NOTHING)

class City(models.Model):
    city_id = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=150)
    region = models.ForeignKey(Region, default=None, on_delete=models.DO_NOTHING)

class AgencyManager(User):
    agency_manger_id = models.IntegerField(primary_key=True, )
    usr = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING, related_name="usr_is_%(class)s_related")

class EstateAgency(models.Model):
    state_agency_id = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=150)
    phone_no = models.CharField(verbose_name="Phone number", max_length=10, validators=[only_int,MinLengthValidator(10),], default='1234567890')
    number_of_employees = models.IntegerField()
    logo = models.ImageField(upload_to="images")
    address = models.CharField(max_length=255)
    agency_manager = models.ForeignKey(AgencyManager, default=None, on_delete=models.DO_NOTHING)

class AgencyAdvisor(User):
    advisor_id = models.IntegerField(primary_key=True)
    usr = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="usr_is_%(class)s_related")
    state_agency = models.ForeignKey(EstateAgency, default=None, on_delete=models.DO_NOTHING)

class House(models.Model):
    house_id= models.PositiveBigIntegerField(primary_key=True, )
    area = models.IntegerField()
    year = models.IntegerField()
    rooms = models.IntegerField()
    parking = models.IntegerField()
    storage_area = models.IntegerField()
    loby_area = models.IntegerField()
    sports_hall_area = models.IntegerField()
    address = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)
    elevator = models.BooleanField()
    balcony = models.BooleanField()
    security_guard = models.BooleanField()
    pool = models.BooleanField()
    sauna = models.BooleanField()
    jacuuzi = models.BooleanField()
    air_conditioning = models.BooleanField()
    clearance_hall = models.BooleanField()
    central_antenna = models.BooleanField()
    remote_door = models.BooleanField()
    roof_guarden = models.BooleanField()
    deal_type = models.CharField(max_length=150)
    city = models.ForeignKey(City, default=None, on_delete=models.DO_NOTHING)

class Advertisement(models.Model):
    ad_id= models.PositiveBigIntegerField(primary_key=True, )
    ad_code = models.CharField(unique=True, max_length=7, validators=[MinLengthValidator(7),only_int,])
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)

    # booleans
    mortgage = models.BooleanField()
    rent = models.BooleanField()
    buy = models.BooleanField()
    exchange = models.BooleanField()
    collaborative = models.BooleanField()
    convertible = models.BooleanField()
    presell = models.BooleanField()
    administrative_position = models.BooleanField()
    borrower = models.BooleanField()
    newly_build = models.BooleanField()
    in_proportionate_share = models.BooleanField()
    
    # images 
    main_image = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()

    # foreign keys
    house = models.ForeignKey(House, default=None, on_delete=models.DO_NOTHING)
    estate_agency = models.ForeignKey(EstateAgency, default=None, on_delete=models.DO_NOTHING)


