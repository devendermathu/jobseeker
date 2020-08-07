from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


company_chooses = (
    ("Company","Company"),
    ("Trader","Trader"),
    ("Wholeseller","Wholeseller"),
    ("Broker","Broker"),
    ("Other","Other"),
)

class Person_information(models.Model):
    Name_of_supplier = models.CharField(max_length=50,null=True,blank=True)
    contact_number = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Name_of_his_company = models.CharField(max_length=100,null=True,blank=True)
    Type_of_organization = models.CharField(max_length=50,choices=company_chooses,default="Company")
    def __str__(self):
        return self.Name_of_supplier

class order(models.Model):
    M_name = models.CharField(max_length=100,null=True,blank=True)
    M_price = models.IntegerField(null=True,blank=True)
    M_quantity = models.IntegerField(null=True,blank=True)
    M_saller = models.CharField(max_length=50,null=True,blank=True)
    M_comapany = models.CharField(max_length=100)
    M_amount = models.FloatField(blank=True,null=True)
    M_date = models.DateField(default=datetime.now(),blank=True,null=True)


class Instock(models.Model):
    N_name = models.CharField(max_length=100,null=True,blank=True)
    N_price = models.IntegerField(null=True,blank=True)
    N_quantity = models.IntegerField(null=True,blank=True)
    N_supplier_name = models.ForeignKey(Person_information,on_delete=models.CASCADE)
    N_data = models.DateField(default=datetime.now(),blank=True,null=True)


# Contact for Job   
# contact = 6395207049
# Email = hrd@increvenue.com
# link = https://www.naukri.com/job-listings-data-analyst-data-crawling-increvenue-rare-vectors-private-limited-gurgaon-1-to-5-years-280520003316?src=jobsearchDesk&sid=15955235269893426&xp=2&px=1
# link = https://amantyatech.com/amantyacareer/data-mining-engineer/