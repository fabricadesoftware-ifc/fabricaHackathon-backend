from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    workload = models.IntegerField()
    acronym = models.CharField(max_length=10)
    course_level = models.CharField(
        max_length=10,
        choices=[
            ('tech', 'Técnico'),
            ('grad', 'Graduação'),
            ('postgrad', 'Pós-Graduação'),
            ('master', 'Mestrado'),
            ('doct', 'Doutorado')
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['name']