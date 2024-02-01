from django.db import models

class MomoCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.BigIntegerField(blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='media', blank=False, null=False)
    category = models.ForeignKey(MomoCategory, on_delete=models.CASCADE, blank=False, null=False, default=1)  # Replace 1 with the actual default category ID

    def __str__(self):
        return self.title


class MenuCategory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class allmenu(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.BigIntegerField(blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='Allmenu', blank=False, null=False)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, blank=False, null=False, default=1)

    def __str__(self):
        return self.title
    


class IngredientCategory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ingredient(models.Model):
    title= models.CharField(max_length=50)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE, blank=False, null=False, default=1)






class Contact(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=40) 
    phone = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return "Message from " + self.fname
