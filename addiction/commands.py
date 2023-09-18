from flask.cli import with_appcontext
import click
import os
import csv

from addiction.extensions import db
from addiction.models import Staff, User, Role, Project, HomePageText, Publication, PublicationCategory
from addiction.config import Constants


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


@click.command("populate_db")
@with_appcontext
def populate_db():

    # Staff
    click.echo("Creating staff")
    path = os.path.join(Constants.PROJECT_ROOT, 'csv', 'staff.csv')
    with open(path, "r", encoding='UTF-8') as staff_csv:
        csv_reader = csv.DictReader(staff_csv)
        for row in csv_reader:
            new_member = Staff(name=row['name'], email=row['email'], position=row['position'])
            new_member.create()

    # Roles
    click.echo("Creating Roles")
    roles = ['user', 'admin']
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    # Admin User
    click.echo("Creating admin user")
    admin_user = User(username="admin", password='password123', email='admin@gmail.com', role_id=2)
    admin_user.create()

    # Categories
    click.echo("Creating publication categories")
    categories = ["აკადემიური პუბლიკაციები", "კვლევითი ანგარიშები", "მკურნალობის გზამკვლევები",
                  "პრევენციის სახელმძღვანელოები", "ფსიქოგანათლება", "წიგნები", "წლიური ანგარიშები"]
    for category in categories:
        new_category = PublicationCategory(name=category)
        new_category.create()

    # Publications
    click.echo("Creating publications")
    path = os.path.join(Constants.PROJECT_ROOT, 'csv', 'file.csv')
    with open(path, "r", encoding='utf-8-sig') as file_csv:
        csv_reader = csv.DictReader(file_csv)
        for row in csv_reader:
            new_publication = Publication(name=row['name'], filename=row['filename'], imagename=row['image'], category_id=row['category'])
            new_publication.create()

    # Texts for home page
    click.echo("Creating Home page texts")
    path = os.path.join(Constants.PROJECT_ROOT, 'csv', 'home.csv')
    with open(path, 'r', encoding='utf-8-sig') as home_csv:
        csv_reader = csv.DictReader(home_csv)
        for row in csv_reader:
            new_item = HomePageText(name=row['name'], text=row['text'], category=row['category'])
            new_item.create()

    # Projects
    click.echo("Creating Projects")
    path = os.path.join(Constants.PROJECT_ROOT, 'csv', 'projects.csv')
    with open(path, 'r', encoding='utf-8-sig') as projects_csv:
        csv_reader = csv.DictReader(projects_csv)
        for row in csv_reader:
            new_project = Project(year=row['years'], title=row['name'], description=row['description'], is_finished=int(row['is_complete']))
            new_project.create()