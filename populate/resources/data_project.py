import faker

fake = faker.Faker("pt_BR")


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
                "description": fake.text(),
            }
        )
    return projects
