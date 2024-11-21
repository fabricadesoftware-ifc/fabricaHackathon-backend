import faker

fake = faker.Faker("pt_BR")

# class Project(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     deploy_link = models.URLField(null=True, blank=True)
#     repository_link = models.URLField(null=True, blank=True)
#     presentation_link = models.URLField(null=True, blank=True)
#     video_link = models.URLField(null=True, blank=True)
#     pitch_link = models.URLField(null=True, blank=True)
#     registration_date = models.DateField(auto_now_add=True, null=True, blank=True)
#     valid_registration = models.BooleanField(default=False, null=True, blank=True)
#     category = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, blank=True)
#     project_photo_base64 = models.OneToOneField(Images, on_delete=models.CASCADE, null=True, blank=True)


def generate_projects(teams_count):
    projects = []
    for _ in range(teams_count):
        projects.append(
            {
                "name": fake.word(),
                "deploy_link": fake.url(),
                "repository_link": fake.url(),
                "presentation_link": fake.url(),
                "video_link": fake.url(),
                "pitch_link": fake.url(),
                "project_photo_base64": None,
                "description": fake.text(),
            }
        )
    return projects
