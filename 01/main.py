from db import Session, engine
from models import Note, Base
from sqlalchemy.exc import SQLAlchemyError


def main():
    Base.metadata.create_all(engine)

    with Session() as session:
        try:
            note_1 = Note(
                title="Lista zakupów",
                body="Mleko, chleb, jajka, masło",
                pinned=False
            )

            note_2 = Note(
                title="Pomysły do projektu",
                body="Sprawdzić SQLAlchemy relationships i migracje",
                pinned=False
            )

            session.add_all([note_1, note_2])
            session.commit()

            
            found_note = session.query(Note).filter(Note.title=="Lista zakupów").first()
            if found_note is not None:
                print("Znaleziono notatke: ",found_note.title)
                print("treść notatki: ",found_note.body)
            else:
                print("Brak notatki o podanej nazwie")

            
            query_note = session.query(Note).filter(Note.pinned==False).first()
            if query_note is not None:
                query_note.pinned = True
                session.commit()
            else:
                print("Nie znaleziono notatki z pinned=False")


            delete_note = session.query(Note).order_by(Note.id).offset(1).first()
            if delete_note is not None:
                session.delete(delete_note)
                session.commit()
                print("usunieto notatkę: ", delete_note.title)
            else:
                print("Nie znaleziono notatki do usunięcia")


        except SQLAlchemyError:
            session.rollback()    
            

if __name__ == "__main__":
    main()
