from django.db import models
import datetime as dt
from datetime import datetime

# Create your models here.

class Blog(models.Model):
	blogheading = models.CharField(max_length=255)
	blogtime = models.DateTimeField(auto_now_add=True, blank = True)
	blogcontent = models.TextField()
	blogimage = models.ImageField(upload_to='images/',default=None, blank=True, null=True)

	def blogSummery(self):
		return self.blogcontent[:100]

	def datePretty(self):
		return self.blogtime.strftime('%b %e %Y') #strftme.org

	def __str__(self):
		return self.blogheading

