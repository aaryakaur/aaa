from django.db import models
from datetime import datetime

#def single_slug(request, single_slug):
 #   categories = [c.category_slug for c in TutorialCategory.objects.all()]
  #  if single_slug in categories:
   #   return HttpResponse(f"{single_slug} is a category")
#
 #   tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
  #  if single_slug in tutorials:
   #   return HttpResponse(f"{single_slug} is a Tutorial")

    #return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")




class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category


class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series


# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())

	tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)
	
	def __str__(self):
		return self.tutorial_title

#Property
class Property(models.Model):
	property_price = models.CharField(max_length=200)
	property_land_area = models.CharField(max_length=200)
	property_location = models.CharField(max_length=200)
	property_type = models.CharField(max_length=200)
	class Meta:
		verbose_name_plural = "Property"

	def __str__(self):
		return self.property_location

#class DisasterDetector(models.Model):
#	property_location = models.ForeignKey(Property, default=1, verbose_name="Property", on_delete=models.SET_DEFAULT)
#	class Meta:
#		verbose_name_plural = "area"
#	def __str__(self):
#		return self.area

class Area(models.Model):
	property_location = models.ForeignKey(Property, default=1, verbose_name="area", on_delete=models.SET_DEFAULT)
	flood = models.CharField(max_length=200)
	earthquake = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "AREA"
	def __str__(self):
		return self.flood