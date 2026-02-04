from db import SessionLocal, engine
from models import Item, Base
from sqlalchemy.exc import SQLAlchemyError



def clear_table(session):
    session.query(Item).delete()
    session.commit()

def main():
    Base.metadata.create_all(engine)

    with SessionLocal() as session:
        clear_table(session)
        try:
            items = [
                Item(name="Kup mleko", priority=1),
                Item(name="Zapłać rachunki", priority=1),
                Item(name="Oddaj auto do mechanika", priority=2),
                Item(name="Zrób backup komputera", priority=2),
                Item(name="Umyj samochód", priority=3),
                Item(name="Zrób zakupy spożywcze", priority=2),
                Item(name="Umów wizytę u lekarza", priority=1),
                Item(name="Wynieś śmieci", priority=4),
                Item(name="Napisz CV", priority=1),
                Item(name="Wyślij fakturę", priority=1),
                Item(name="Przeczytaj dokumentację SQLAlchemy", priority=3),
                Item(name="Zrób trening", priority=3),
                Item(name="Napraw kran", priority=2),
                Item(name="Zadzwoń do klienta", priority=1),
                Item(name="Zaplanuj tydzień", priority=2),
                Item(name="Posprzątaj biurko", priority=4),
                Item(name="Zaktualizuj system", priority=3),
                Item(name="Odpowiedz na maile", priority=2),
                Item(name="Zrób commit i push", priority=1),
                Item(name="Przygotuj seed do projektu", priority=2),
            ]

            session.add_all(items)
            session.commit()
            print("Zładowano dane do tabeli ")

            print("\n")

            sorted_items = session.query(Item).order_by(Item.priority).all()
            for item in sorted_items:
                print(f"Element: {item.name}| priorytet: {item.priority}" )

            print("\n")

            paginated_items = session.query(Item).order_by(Item.priority, Item.id).limit(5).offset(10).all()
            for item in paginated_items:
                print(item.id,item.name,item.priority)    


        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()

if __name__ == "__main__":
    main()    