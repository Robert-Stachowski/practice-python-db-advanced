from db import SessionLocal, engine
from models import Person, Skill,person_skill, Base
from sqlalchemy.exc import SQLAlchemyError


def clear_table(session):
    session.execute(person_skill.delete())
    session.query(Skill).delete()
    session.query(Person).delete()
    session.commit()

def main():
    Base.metadata.create_all(engine)


    with SessionLocal() as session:
        clear_table(session)
        try:
            persons = [
                Person(name="Xarion"),
                Person(name="Lunara"),
                Person(name="Milo"),
                Person(name="Zyra"),
                Person(name="Olek"),
            ]
            
            skills = [
                Skill(name="Python"),
                Skill(name="SQL"),
                Skill(name="Docker"),
                Skill(name="Git"),
                Skill(name="FastAPI"),
                Skill(name="Django"),
                Skill(name="Linux"),
                Skill(name="Debugging"),
                Skill(name="Testing"),
                Skill(name="Refactoring"),
            ]

            session.add_all(persons + skills)
            session.commit()
            print("\n Załadowano dane poprawnie \n")

            # Przypisz osobom wybrane umiejętności
            # Obiekty persons/skills już są w sesji po commit — nie trzeba ponownie pobierać z bazy
            xarion, lunara, milo, zyra, olek = persons
            python, sql, docker, git, fastapi, django, linux, debugging, testing, refactoring = skills

            xarion.skills = [python, sql, docker]
            lunara.skills = [django, testing]
            milo.skills = [git, linux]
            zyra.skills = [fastapi, debugging, refactoring]
            olek.skills = [fastapi, debugging, refactoring, django, testing]

            session.commit()
            print("\n Przypisano umiejętności \n")
                        



            
            #Dla jednej osoby wypisz listę jej umiejętności.
            person_name = "Olek"
            person = session.query(Person).filter(Person.name==person_name).one()

            print(f"Osoba: '{person_name}', posiada umiejętności: ")

            if not person.skills:
                print("Brak umiejętności")
            for skills in person.skills:                
                print(skills.name)





            print("\n")
            #Dla jednej umiejętności wypisz listę osób, które ją posiadają.
            skill_name = "Refactoring"
            skill = (session.query(Skill).filter(Skill.name==skill_name).one())

            print(f"Skilla: '{skill.name}' posiada: ")

            if not skill.persons:
                    print(f"Nikt nie ma skilla '{skill.name}' ")
            for person in skill.persons:                
                print(person.name)




        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()



if __name__ == "__main__":
    main()