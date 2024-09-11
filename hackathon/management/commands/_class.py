from hackathon.models import ClassInfo, Course
from hackathon.resources.data_class import classes, courses


def populate_courses():
    if Course.objects.exists():
        return

    courses_to_insert = [Course(**course) for course in courses]
    Course.objects.bulk_create(courses_to_insert)


def populate_classes():
    if ClassInfo.objects.exists():
        return

    classes_to_insert = [ClassInfo(**class_info) for class_info in classes]
    
    courses = Course.objects.all()
    course_dict = {course.acronym: course for course in courses}

    for class_info in classes_to_insert:
        class_name = class_info.name
        
        for acronym, course in course_dict.items():
            if acronym in class_name:
                class_info.course = course
                break
    
    ClassInfo.objects.bulk_create(classes_to_insert)