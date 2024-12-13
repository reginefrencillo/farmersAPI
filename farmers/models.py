from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.utils.timezone import now
from datetime import date

class Commodity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Barangay(models.Model):
    code = models.CharField(max_length=3, unique=True)  # e.g., '001', '002'
    name = models.CharField(max_length=100)  # e.g., 'Barangay 1'

    def __str__(self):
        return self.name

class Farmer(models.Model):
    # Dropdown options for gender, civil status, educ attainment, and religion
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    CIVIL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widow/er', 'Widow/er'),
        ('Legally Separated', 'Legally Separated')
    ]

    EDUC_ATTAINMENT_CHOICES = [
        ('Pre-school', 'Pre-school'),
        ('Elementary','Elementary'),
        ('High School (non K-12)', 'High School (non K-12)'),
        ('Junior High School (K-12)', 'Junior High School (K-12)'),
        ('Senior High School (K-12)', 'Senior High School (K-12)'),
        ('College', 'College'),
        ('Post Graduate', 'Post Graduate'),
        ('Vocational','Vocational'),
        ('None', 'None')
    ]

    LIVELIHOOD = [
        ('Farmer', 'Farmer'),
        ('Farmworkers', 'Farmworkers'),
        ('Fisherfolk', 'Fisherfolk')
    ]

    # Photo field for uploading employee picture
    profile_photo = models.ImageField(upload_to='farmers_photos/', blank=True, null=True)  # Optional field for the photo
    rsbsa_id = models.CharField(max_length=50, unique=True)

    # Personal Information Fields
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    ext_name = models.CharField(max_length=10, blank=True, null=True)
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    pwd = models.BooleanField(default=False)
    fourps_beneficiary = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=11, null = True)
    
    religion = models.CharField(max_length=10, default="", null=False)
    educ_attainment = models.CharField(max_length=50, choices=EDUC_ATTAINMENT_CHOICES, default='High School')
    civil_status = models.CharField(max_length=50, choices=CIVIL_STATUS_CHOICES, default='Single')
    
    date_of_birth = models.DateField(null = True)
    birthplace = models.CharField(max_length=100, default="", null=False)
    indigenous_people = models.BooleanField(default=False, null = True)
    indeigenous_specify = models.CharField(max_length=100, default="", null=True)



    # Address Fields
    house_no = models.CharField(max_length=10, default="", null=False)
    street = models.CharField(max_length=100, default="", null=False)
    barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)  # Use ForeignKey
    municipality = models.CharField(max_length=100, default="Matnog", null=False)
    province = models.CharField(max_length=100, default="Sorsogon", null=False)
    region = models.CharField(max_length=100, default="V - Bicol", null=False)
    
 
    # Household Information
    name_of_spouse = models.CharField(max_length=100, blank=True)
    mothers_maiden = models.CharField(max_length=100)
    name_of_household_head = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    household_members = models.IntegerField()
    household_male = models.IntegerField()
    household_female = models.IntegerField()
    
    # Government ID Information
    govern_id = models.BooleanField(default=False)
    id_type = models.CharField(max_length=50, blank=True, null=True)
    id_no = models.CharField(max_length=100, blank=True, null=True)
    

    # Emergency Information
    if_emergency = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=11)
    
    # Membership Information
    member_of_farmers_associate = models.BooleanField(default=False)
    specify = models.CharField(max_length=100, blank=True, null=True)
    
    # Livelihood Information
    main_livelihood = models.CharField(max_length=20, choices=LIVELIHOOD, default='Farmer')
    commodities = models.ManyToManyField(Commodity)
    specify_position = models.CharField(max_length=100, blank=True, null=True)

    # Mapping Information
    north_neighbor = models.CharField(max_length=100, blank=True)
    south_neighbor = models.CharField(max_length=100, blank=True)
    east_neighbor = models.CharField(max_length=100, blank=True)
    west_neighbor = models.CharField(max_length=100, blank=True)

    date_added = models.DateTimeField(default=timezone.now)  # Automatically set on creation


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        """Calculates age based on date_of_birth."""
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


    def save(self, *args, **kwargs):
        if not self.rsbsa_id:
            self.rsbsa_id = self.generate_rsbsa_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.rsbsa_id}'

   