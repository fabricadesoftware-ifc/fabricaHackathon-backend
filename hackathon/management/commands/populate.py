from django.core.management.base import BaseCommand, CommandError, CommandParser
from hackathon.management.commands._user import (
    populate_users,
    populate_students,
    populate_avaliators,
)
from hackathon.management.commands._class import populate_courses, populate_classes
from hackathon.management.commands._edition import populate_editions
from hackathon.management.commands._avaliation import populate_criteria
from hackathon.management.commands._team import populate_teams


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--user",
            action="store_true",
            help="Inserts user data in the database for testing (Students, Teachers, Avaliators)",
        )
        parser.add_argument(
            "--class",
            action="store_true",
            help="Inserts class data in the database for testing (Classes, Courses)",
        )
        parser.add_argument(
            "--edition",
            action="store_true",
            help="Inserts edition data in the database for testing (Editions, Criteria)",
        )
        parser.add_argument(
            "--team",
            action="store_true",
            help="Inserts team data in the database for testing (Teams)",
        )
        parser.add_argument(
            "--avaliation",
            action="store_true",
            help="Inserts avaliation data in the database for testing (Avaliations)",
        )
        parser.add_argument(
            "--all",
            action="store_true",
            help="Inserts all data in the database for testing",
        )

    def handle(self, *args, **options) -> None:
        try:
            if options.get("user"):
                self.__handle_user()
            if options.get("class"):
                self.__handle_class()
            if options.get("edition"):
                self.__handle_edition()
            if options.get("avaliation"):
                self.__handle_avaliation()
            if options.get("team"):
                self.__handle_team()
            # if options.get("all"):
            #     self.__handle_all()

            self.stdout.write(self.style.SUCCESS("Data inserted successfully"))

        except CommandError as exc:
            raise CommandError("Something went wrong") from exc

        except Exception as e:
            self.stdout.write(self.style.ERROR(e))

    def __handle_user(self) -> None:
        self.stdout.write("Populating Users...", ending=" ")
        populate_users()
        self.stdout.write(self.style.SUCCESS("OK"))

        self.stdout.write("Populating Students...", ending=" ")
        populate_students()
        self.stdout.write(self.style.SUCCESS("OK"))

        self.stdout.write("Populating Avaliators...", ending=" ")
        populate_avaliators()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_class(self) -> None:
        self.stdout.write("Populating Courses...", ending=" ")
        populate_courses()

        self.stdout.write("Populating Classes...", ending=" ")
        populate_classes()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_avaliation(self) -> None:
        self.stdout.write("Populating Criteria...", ending=" ")
        populate_criteria()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_edition(self) -> None:
        self.stdout.write("Populating Editions...", ending=" ")
        populate_editions()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_team(self) -> None:
        self.stdout.write("Populating Teams...", ending=" ")
        populate_teams()
        self.stdout.write(self.style.SUCCESS("OK"))

    # def __handle_all(self) -> None:
    #     self.stdout.write("Populating Everything...", ending=" ")

    #     self.__handle_user()
    #     self.__handle_class()
    #     self.__handle_edition()
    #     self.__handle_team()

    #     self.stdout.write(self.style.SUCCESS("OK"))
