from django.db import models



# Create your models here.

class Role(models.TextChoices):
    University = "university", "University"
    Student = "student", "Student"
    Business = "companies", "Companies"
    Minister = "minister", "Minister"



class Account(models.Model):

    username = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length= 128)
    role = models.CharField (
        max_length= 10 ,
        choices= Role.choices,
    )
    is_verified = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True) # Date et heure de création

    def __str__(self):
        return f'{self.username}{self.email}{self.password}{self.role}{self.is_verified}{self.created_at}'



class University_Official_DB(models.Model) : 
    name = models.CharField(max_length = 100)
    address = models.TextField() # Pas de limite de caractères
    region = models.CharField(max_length= 50)
    phone = models.CharField(max_length = 15, unique = True)
    email = models.EmailField(unique= True)

    def __str__(self):
        return f'{self.name}{self.address}{self.region}{self.phone}{self.email}'

class University_Certify_me (models.Model) :
    University_acount = models.ForeignKey(Account, on_delete=models.CASCADE  )
    name = models.CharField(max_length= 100)
    address = models.TextField()
    phone = models.CharField(max_length=15, unique=True)


class Companies_Certify_me (models.Model) :
    Companies_acount = models.ForeignKey(Account , on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    address = models.TextField()
    phone = models.CharField(max_length=15, unique=True)

class Ministry_Certify_me (models.Model) :
    Ministry_acount = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    address = models.TextField()
    


