from django.core.management.base import BaseCommand, CommandError, CommandParser
from ._user import (
    populate_users,
    populate_students,
    populate_avaliators,
    populate_teachers,
)
from ._class import populate_courses, populate_classes
from ._edition import populate_editions
from ._avaliation import (
    populate_criteria,
    populate_avaliations,
)
from ._ranking import populate_rankings
from ._team import populate_teams
from ._category import populate_categories
from ._supporter import populate_supporters


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
            "--supporter",
            action="store_true",
            help="Inserts supporter data in the database for testing (Supporters)",
        )
        parser.add_argument(
            "--ranking",
            action="store_true",
            help="Inserts ranking data in the database for testing (Rankings)",
        )
        parser.add_argument(
            "--category",
            action="store_true",
            help="Inserts category data in the database for testing (Categories)",
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
            if options.get("supporter"):
                self.__handle_supporter()
            if options.get("ranking"):
                self.__handle_ranking()
            if options.get("category"):
                self.__handle_category()
            if options.get("all"):
                self.__handle_all()

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

        self.stdout.write("Populating Teachers...", ending=" ")
        populate_teachers()
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

        self.stdout.write("Populating Avaliations...", ending=" ")
        populate_avaliations()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_edition(self) -> None:
        self.stdout.write("Populating Editions...", ending=" ")
        populate_editions()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_team(self) -> None:
        self.stdout.write("Populating Teams...", ending=" ")
        populate_teams()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_supporter(self) -> None:
        self.stdout.write("Populating Supporters...", ending=" ")
        populate_supporters()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_ranking(self) -> None:
        self.stdout.write("Populating Rankings...", ending=" ")
        populate_rankings()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_category(self) -> None:
        self.stdout.write("Populating Categories...", ending=" ")
        populate_categories()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self) -> None:
        self.stdout.write("Populating Everything...", ending=" ")

        self.__handle_class()
        self.__handle_user()
        self.__handle_category()
        self.__handle_supporter()
        self.__handle_edition()
        self.__handle_team()
        self.__handle_avaliation()
        self.__handle_ranking()

        self.stdout.write(self.style.SUCCESS("OK"))