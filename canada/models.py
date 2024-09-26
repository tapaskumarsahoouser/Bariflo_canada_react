from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)      
    email = models.EmailField(max_length=254)    
    phno = models.CharField(max_length=15)       
    companyname = models.CharField(max_length=100)
    message = models.TextField()                  

    def __str__(self):
        return f"{self.name} - {self.email}"
