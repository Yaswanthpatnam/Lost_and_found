from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('Electronics', 'Electronics'),
    ('Documents', 'Documents'),
    ('Stationery', 'Stationery'),
    ('Accessories', 'Accessories'),
    ('Personal Items', 'Personal Items'),
]

LOCATION_CHOICES = [
    ('Left Parking', 'Left Parking'),
    ('Right Parking', 'Right Parking'),
    ('Inner Parking', 'Inner Parking'),
    ('Main Gate', 'Main Gate'),
    ('Fountain','Fountain'),
    ('Garden','Garden'),
    ('A Block', 'A Block'),
    ('B Block', 'B Block'),
    ('C Block', 'C Block'),
    ('Auditorium','Auditorium'),
    ('D Block','D Block'),
    ('E Block','E Block'),
    ('Canteen', 'Canteen'),
    ('Library', 'Library'),
    ('SISTK-A Block','SISTK-A Block'),
    ('SISTK-B Block', 'SISTK-B Block'),
    ('Office Room','Office Room'),
    ('Examination Cell','Examination Cell'),
    ('Mechanical Workshop','Mechanical Workshop'),
    ('SISTK-Mechanical Workshop','SISTK-Mechanical Workshop'),
    ('Yoga hall','Yoga hall'),
    ('GYM','GYM'),
    ('Telugu-Girls hostel','Telugu-Girls hostel'),
    ('Bihar-Girls hostel','Bihar-Girls hostel'),
    ('Telugu-Boys hostel','Telugu-Boys hostel'),
    ('Bihar-Boys hostel','Bihar-Boys hostel'),
    ('Play Ground-FootBall', 'Play Ground-FootBall'),
    ('Play Ground-BasketBall','Play Ground-BasketBall'),

]


    
class FoundItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()    
    image = models.ImageField(upload_to='lost_images/', blank=True, null=True)
    contact_info = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Personal Items')
    date_found = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Found: {self.title}"
 
class SearchItem(models.Model):
    category = models.CharField(max_length=50, choices = CATEGORY_CHOICES)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    date_time = models.DateTimeField(null=True, blank=True)    

    def __str__(self):
        return f"Search: {self.category} at {self.location} on {self.date_time}"