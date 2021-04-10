from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"
        db_table = "category"
        ordering = ['name', 'description']

    def __str__(self):
        return self.name

# Create your models here.
class Task(models.Model):
    BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))

    title = models.CharField(max_length=40)
    description = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="task")
    due_date = models.DateField()
    completed = models.BooleanField(default=False, choices=BOOL_CHOICES)

    class Meta:
        verbose_name_plural = "tasks"
        db_table = "task"
        ordering = ['title', 'category', 'due_date', 'completed']

    def __str__(self):
        return self.nome

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'title': str(self.title),
            'category': str(self.category),
            'due_date': str(self.due_date),
            'completed': self.completed,
        }