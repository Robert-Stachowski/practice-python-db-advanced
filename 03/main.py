from db import Session, engine
from models import Person, Skill, person_skill, Base
from sqlalchemy.exc import SQLAlchemyError


def main():
    Base.metadata.create_all(engine)


    with Session() as session:
        try:
            # --- osoby ---
            persons = [
                Person(name="Xarion"),
                Person(name="Lunara"),
                Person(name="Milo"),
                Person(name="Zyra"),
                Person(name="Olek"),
            ]

            # --- umiejętności ---
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
            session.flush()
            """
            session.flush():
            - wysyła INSERT/UPDATE do DB
            - nadaje ID
            - NIE zamyka transakcji
            - rollback cofnie wszystko
            """
            



            session.commit()


        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()



if __name__ == "__main__":
    main()