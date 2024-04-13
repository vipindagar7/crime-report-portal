from django.db import models
from accounts.models import Custom_user
# Create your models here.

class case(models.Model):
    case_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    inspector = models.ForeignKey(Custom_user, on_delete=models.CASCADE , null = True, blank = True, related_name='inspector')
    case_name = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100)
    case_description = models.TextField()
    case_date = models.DateField()
    case_created_on = models.DateField(auto_now_add=True)
    case_location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    case_files = models.FileField(upload_to='case_files/')
    case_status = models.CharField(max_length=50, null = True, blank = True)