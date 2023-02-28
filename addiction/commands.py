from flask.cli import with_appcontext
import click
from addiction.extensions import db
from addiction.models.staff import Staff
from addiction.models.user import User, UserRole, Role
from addiction.models.home import Home
from addiction.models.projects import Project
from flask import current_app
from addiction.models.file import File
import os
import csv
from csv import reader

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
    click.echo("Creating staff")
    
    path=os.path.join(current_app.config['BASE_DIR'], 'csvfiles', 'staff.csv')
    with open(path, "r") as staff_csv:
        csv_reader= csv.DictReader(staff_csv)
        for row in csv_reader:
            new_member = Staff(name=row['name'], email=row['email'], position=row['position'])
            new_member.create()
    


    click.echo("Creating users")
    admin_user=User(username="admin1", password='asdf', email='admin@gmail.com')
    admin_user.create()

    roles=['user', 'moderator', 'admin']
    for role in roles:
        new_role=Role(name=role)
        new_role.create()
    
    admin_role=Role.query.filter_by(name="admin").first()
    admin_user_role=UserRole(user_id=admin_user.id, role_id=admin_role.id)
    admin_user_role.create()


    click.echo("Creating files")
    path=os.path.join(current_app.config['BASE_DIR'], 'csvfiles', 'file.csv')
    with open(path, "r") as file_csv:
        csv_reader= csv.DictReader(file_csv)
        for row in csv_reader:
            new_file = File(filename=row['filename'], displayname=row['displayname'], category=row['category'], folder=row['folder'])
            new_file.create()


    click.echo("Creating home")
    
    path=os.path.join(current_app.config['BASE_DIR'], 'csvfiles', 'home.csv')
    with open(path, 'r') as home_csv:
        csv_reader= csv.DictReader(home_csv)
        for row in csv_reader:
            new_item= Home(about=row['about'], directions=row['directions'], history=row['history'])
            new_item.create()
    

    click.echo("Creating Projects")

    path=os.path.join(current_app.config['BASE_DIR'], 'csvfiles', 'projects.csv')
    with open(path, 'r') as projects_csv:
        csv_reader= csv.DictReader(projects_csv)
        for row in csv_reader:
            new_project= Project(current=row['current'], implemented=row['implemented'])
            new_project.create()



    



