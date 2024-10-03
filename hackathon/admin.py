from django.contrib import admin

from .models import Course, ClassInfo, Edition, Student, Team, Criterion, Avaliation, Ranking, Category

admin.site.register(Course)
admin.site.register(ClassInfo)
admin.site.register(Edition)
admin.site.register(Student)
admin.site.register(Team)
admin.site.register(Criterion)
admin.site.register(Avaliation)
admin.site.register(Ranking)
admin.site.register(Category)