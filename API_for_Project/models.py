from django.db import models





class poojas(models.Model):
	class Meta:
		verbose_name_plural="poojas"
	pooja_id = models.CharField(max_length=10)
	pooja_name = models.CharField(max_length=50)
	Pooja_picture =  models.ImageField(upload_to='static/Pooja_picture',null=True)

	def __str__(self):
		return self.pooja_name 


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
('Andaman & Nicobar Islands','Andaman & Nicobar Islands'), 
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'), 
('Assam','Assam'),
('Bihar','Bihar'), 
('Chandigarh','Chandigarh'), 
('Chattisgarh','Chattisgarh'),
('Dadra & Nagar Haveli','Dadra & Nagar Haveli'), 
('Daman and Diu','Daman and Diu'), 
('Delhi','Delhi'),
('Goa','Goa'),
('Gujrat','Gujrat'), 
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'), 
('Jammu & Kashmir','Jammu & Kashmir'), 
('Jharkhand','Jharkhand'), 
('Karnataka','Karnataka'), 
('Kerala','Kerala'), 
('Lakshadweep','Lakshadweep'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'), 
('Manipur','Manipur'), 
('Meghalaya','Meghalaya'), 
('Mizoram','Mizoram'), 
('Nagaland','Nagaland'), 
('Odisa','Odisa'), 
('Puducherry','Puducherry'), 
('Punjab','Punjab'), 
('Rajasthan','Rajasthan'), 
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'), 
('Telangana','Telangana'), 
('Tripura','Tripura'), 
('Uttarakhand','Uttarakhand'), 
('Uttar Pradesh','Uttar Pradesh'), 
('West Bengal','West Bengal'),
)

CATEGORY_CHOICES=(
    ('CR','Occasional'),
    ('ML','Festival'),
    ('MS','Homas'),
    
)



class items(models.Model):
    items_list = models.CharField(max_length=200)
    def __str__(self):
        return self.items_list




class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    Items =  models.ManyToManyField(items)
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='API_for_Project/static/Pooja_picture',null=False)
    def __str__(self):
        return self.title

class dict(models.Model):
     name = models.CharField(max_length =50)
     price = models.FloatField()
     def __str__(self):
        return self.name

class Products(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    Items =  models.ManyToManyField(dict,db_index=True)
    #document = DictField(child=CharField())
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='API_for_Project/static/Pooja_picture',null=False)
    def __str__(self):
        return self.title

class cxategories(models.Model):
     Category = models.CharField(max_length=100)
     Category_image = models.ImageField(upload_to='static/Pooja_picture',null=False)
     classified = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default="")
     def __str__(self):
          return self.Category



