from flask.cli import with_appcontext
import click
from addiction.extensions import db
from addiction.models.staff import Staff
from addiction.models.user import User, UserRole, Role


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
    staff_members=[
        ("ჯანა ჯავახიშვილი", "darejan.javakhishvili@iliauni.edu.ge", "ილიაუნის ადიქტოლოგიის ინსტიტუტის დირექტორი და მკვლევარი, ფსიქოლოგიურ მეცნიერებათა დოქტორი, ილიაუნის მეცნიერებათა და ხელოვნების ფაკულტეტის პროფესორი; საქართველოს ადიქტოლოგთა ასოციაცის თანადამფუძნებელი და გამგეობის წევრი; ტრავმული სტრესის კვლევის საერთაშორისო საზოგადოების (ISTSS) დირექტორთა საბჭოს წევრი"),
        ("დავით ოთიაშვილი", 'davit.otiashvili@iliauni.edu.ge ', "ილიაუნის ადიქტოლოგიის ინსტიტუტის თანადამფუძნებელი და მკვლევარი, ჯანმრთელობის ფსიქოლოგიის დოქტორი, ილიაუნის სამედიცინო სკოლის ასოცირებული პროფესორი, საქართველოს ადიქტოლოგთა ასოციაციის თავმჯდომარე, საქართველოს ნარკომანიასთან ბრძოლის უწყებათაშორისი საბჭოს წევრი, სადაც წარმოადგენს არასამთავრობო სექტორს"),
        ("ირმა კირთაძე", 'irma.kirtadze@iliauni.edu.ge', "ილიაუნის ადიქტოლოგიის ინტიტუტის თანადამფუძმნებელი და მკვლევარი, საზოგადოებრივი ჯანმრთელობის დოქტორი, ილიაუნის მეცნიერებათა და ხელოვნების ფაკულტეტის ასოცირებული პროფესორი, საქართველოს ადიქტოლოგთა ასოციაციის თანადამფუძნებელი და გამგეობის წევრი "),
        ("მარიამ რაზმაძე", "mariam.razmadze.3@iliauni.edu.ge", "ილიაუნის ადიქტოლოგიის ინსტიტუტის კოორდინატორი და მკვლევარი, ფსიქიკური ჯანმრთელობის მაგისტრი, საქართველოს ადიქტოლოგთა ასოციაცის წევრი, ევროპის პრევენციის კურიკულუმის ეროვნული ტრენერი")
    ]

    for member in staff_members:
        new_member = Staff(name=member[0], email=member[1], position=member[2])
        db.session.add(new_member)
    
        
    db.session.commit()


    click.echo("Creating users")
    admin_user=User(username="admin1", password='asdf')
    admin_user.create()

    roles=['user', 'moderator', 'admin']
    for role in roles:
        new_role=Role(name=role)
        new_role.create()
    
    admin_role=Role.query.filter_by(name="admin").first()
    admin_user_role=UserRole(user_id=admin_user.id, role_id=admin_role.id)
    admin_user_role.create()
    



