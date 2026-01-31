from db import Session, engine
from models import Person, Skill,person_skill, Base
from sqlalchemy.exc import SQLAlchemyError


def clear_table(session):
    session.query(person_skill)
    session.query(Skill).delete()
    session.query(Person).delete()
    session.commit()

def main():
    Base.metadata.create_all(engine)


    with Session() as session:
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

            session.add_all(persons+skills)            
            session.commit()
            print("\n Załadowano dane poprawnie \n")

            #Przypisz osobom wybrane umiejętności.
            persons = session.query(Person).all()
            skills = session.query(Skill).all()

            person_by_name = {p.name: p for p in persons}
            skill_by_name = {s.name: s for s in skills}

            assignments = {
                "Xarion": ["Python", "SQL", "Docker"],
                "Lunara": ["Django", "Testing"],
                "Milo":   ["Git", "Linux"],
                "Zyra":   ["FastAPI", "Debugging", "Refactoring"],
                "Olek":   ["FastAPI", "Debugging", "Refactoring","Django", "Testing"]
            }
        
            for person_name, skill_name in assignments.items():
                person = person_by_name[person_name]
                person.skills = [skill_by_name[name] for name in skill_name]

            session.commit()
            print("\n Przypisano umiejętności \n")

            


            
            
            #Dla jednej osoby wypisz listę jej umiejętności.
            person_name = "Olek"
            person = session.query(Person).filter(Person.name==person_name).one()

            print(f"Osoba: '{person_name}', posiada umiejętności: ")

            for skills in person.skills:
                if not person.skills:
                    print("Brak umiejętności")
                print(skills.name)





            print("\n")
            #Dla jednej umiejętności wypisz listę osób, które ją posiadają.
            skill_name = "Refactoring"
            skill = (session.query(Skill).filter(Skill.name==skill_name).one())

            print(f"Skilla: '{skill.name}' posiada: ")

            for person in skill.persons:
                if not skill.persons:
                    print(f"Nikt nie ma skilla '{skill.name}' ")
                print(person.name)




        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()



if __name__ == "__main__":
    main()