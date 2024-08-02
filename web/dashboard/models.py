from django.db import models


class SearchHistory(models.Model):
	query = models.CharField(max_length=1000)

	def __str__(self):
		return self.query


class Project(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=500)
	slug = models.SlugField(unique=True)
	insert_date = models.DateTimeField()

	def __str__(self):
		return self.slug


class OpenAiAPIKey(models.Model):
	id = models.AutoField(primary_key=True)
	key = models.CharField(max_length=500)

	def __str__(self):
		return self.key
	

class OllamaSettings(models.Model):
	id = models.AutoField(primary_key=True)
	selected_model = models.CharField(max_length=500)
	use_ollama = models.BooleanField(default=True)

	def __str__(self):
		return self.selected_model


class NetlasAPIKey(models.Model):
	id = models.AutoField(primary_key=True)
	key = models.CharField(max_length=500)

	def __str__(self):
		return self.key
