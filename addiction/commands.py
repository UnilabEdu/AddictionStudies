from flask.cli import with_appcontext
import click
from addiction.extensions import db
from addiction.models.staff import Staff
from addiction.models.user import User, UserRole, Role
from flask import current_app
from addiction.models.file import File
import os

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
        
        new_member.create()



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


    click.echo("Creating files")

    #for linux
    display_name=[
        "ყურადღების ცენტრში: ფენტანილები და სხვა ახალი ოპიოიდები",
        "ყურადღების ცენტრში: სინთეზური კანაბინოიდები" ,  
        "ყურადღების ცენტრში: ფსიქოაქტიური ნივთიერებების მოხმარება და ფსიქიკური ჯანმრთელობის კომორბიდული პრობლემები",
        "ხარისხის სტანდარტების დანერგვა ნარკოლოგიური სერვისებისა და სისტემებისთვის", 
        "ნარკოტიკების ავადმოხმარების პრევენცია", 
        "სამოქმედო ჩარჩო ნარკოტიკებთან დაკავშირებულ პრობლემებზე საპასუხო ჯანდაცვითი და სოციალური ზომების შემუშავებისა და განხორციელებისთვის",
        "მედია, ფსიქიკური ჯანმრთელობა და ადამიანის უფლებები", 
        "კანაფი: ჯანდაცვითი და სოციალური საპასუხო ზომები",
        "ოპიოიდები: ჯანდაცვითი და სოციალური საპასუხო ზომები",
        "ახალი ფსიქოაქტიური ნივთიერებები: ჯანდაცვითი და სოციალური საპასუხო ზომები", 
        "სტიმულატორები: ჯანდაცვითი და სოციალური საპასუხო ზომები",
        "ოპიოიდების მოხმარებასთან დაკავშირებული სიკვდილი: ჯანდაცვითი და სოციალური საპასუხო ზომები",
        "წამლების არასამედიცინო დანიშნულებით გამოყენება: ჯანდაცვითი და სოციალური საპასუხო ზომები",
        "ნარკოტიკების პოლიმოხმარება: ჯანდაცვითი და სოციალური საპასუხო ზომები",  
        "Piloting Comprehensive Social Influence (‘Unplugged’) Program in Georgia: A", 
        "‘Ten Years Later’ – Developing Institutional Mechanisms for Drug Demand Reduction and Addictology Education in Georgia – A Case Study ", 
        "ჩანაცვლებითი თერაპიის სერვისებით მოსარგებლეთა კმაყოფილების კვლევა დასავლეთ საქართველოში", 
        "პრევენციის ევროპული კურიკულუმი",

    ]

    #for windows
    # display_name=[ "‘Ten Years Later’ – Developing Institutional Mechanisms for Drug Demand Reduction and Addictology Education in Georgia – A Case Study ", 
    #                "Piloting Comprehensive Social Influence (‘Unplugged’) Program in Georgia: A", 
    #                "სამოქმედო ჩარჩო ნარკოტიკებთან დაკავშირებულ პრობლემებზე საპასუხო ჯანდაცვითი და სოციალური ზომების შემუშავებისა და განხორციელებისთვის",
    #                "ხარისხის სტანდარტების დანერგვა ნარკოლოგიური სერვისებისა და სისტემებისთვის", 
    #                 "მედია, ფსიქიკური ჯანმრთელობა და ადამიანის უფლებები", 
    #                 "ნარკოტიკების ავადმოხმარების პრევენცია", 
    #                  "პრევენციის ევროპული კურიკულუმი",
    #                 "ყურადღების ცენტრში: სინთეზური კანაბინოიდები" ,  
    #                 "ყურადღების ცენტრში: ფენტანილები და სხვა ახალი ოპიოიდები",
    #                 "ყურადღების ცენტრში: ფსიქოაქტიური ნივთიერებების მოხმარება და ფსიქიკური ჯანმრთელობის კომორბიდული პრობლემები",
    #                 "ჩანაცვლებითი თერაპიის სერვისებით მოსარგებლეთა კმაყოფილების კვლევა დასავლეთ საქართველოში", 
    #                 "კანაფი: ჯანდაცვითი და სოციალური საპასუხო ზომები",
    #                 "ახალი ფსიქოაქტიური ნივთიერებები: ჯანდაცვითი და სოციალური საპასუხო ზომები", 
    #                  "ნარკოტიკების პოლიმოხმარება: ჯანდაცვითი და სოციალური საპასუხო ზომები", 
    #                  "სტიმულატორები: ჯანდაცვითი და სოციალური საპასუხო ზომები",
    #                  "წამლების არასამედიცინო დანიშნულებით გამოყენება: ჯანდაცვითი და სოციალური საპასუხო ზომები", 
    #                  "ოპიოიდების მოხმარებასთან დაკავშირებული სიკვდილი: ჯანდაცვითი და სოციალური საპასუხო ზომები",
    #                  "ოპიოიდები: ჯანდაცვითი და სოციალური საპასუხო ზომები"
    #               ]
    relative='static/publications'
    incomplete_path=os.path.join(current_app.config['BASE_DIR'], relative)
    folder_names=os.listdir(incomplete_path)
    i=0
    for name in folder_names:
        complete_path=os.path.join(incomplete_path, name)
        files=os.listdir(complete_path)
        for filename in files:
            new_file=File(filename=filename, displayname=display_name[i], file_path=complete_path, category=name)
            i+=1
            new_file.create()

    



