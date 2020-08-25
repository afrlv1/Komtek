from django.db import models


class Guide(models.Model):
	name = models.CharField(max_length=200, verbose_name='Наименование')
	title = models.CharField(max_length=100, verbose_name='Короткое наименование')
	description = models.TextField(blank=True, verbose_name='Описание')
	version = models.CharField(unique=True, max_length=50, verbose_name='Версия справочника')
	date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Справочник'
		verbose_name_plural = 'Справочники'
		ordering = ['date']


class GuideElement(models.Model):
	guide = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name='Справочник')
	code = models.CharField(max_length=50, verbose_name='Код элемента')
	value = models.CharField(max_length=200, verbose_name='Значение элемента')

	def __str__(self):
		return self.code

	class Meta:
		verbose_name = 'Элемент справочника'
		verbose_name_plural = 'Элементы справочника'
