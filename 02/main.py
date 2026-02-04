from db import SessionLocal, engine
from models import Author, Book, Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from sqlalchemy.orm import selectinload

def clear_table(session):
    session.query(Book).delete()
    session.query(Author).delete()
    session.commit()

def main():
    Base.metadata.create_all(engine)

    with SessionLocal() as session:
        clear_table(session)
        try:
            
            # Autor1
            author1 = Author(name="George Orwell")
            author1.books.append(Book(title="1984"))
            author1.books.append(Book(title="Animal Farm"))

            # Autor2
            author2 = Author(name="J.R.R. Tolkien")
            author2.books.append(Book(title="The Hobbit"))
            author2.books.append(Book(title="The Lord of the Rings"))
            author2.books.append(Book(title="The Silmarillion"))

            session.add_all([author1, author2])
            session.commit()




            # Zapytanie przez SQL 
            found_author_books = (
                session.query(Author)
                .options(selectinload(Author.books))
                .filter(Author.name=="J.R.R. Tolkien").one()
                )
            print(f"Autor: {found_author_books.name}")
            print("Książki: \n")
            for book in found_author_books.books:
                print(book.title)


            # tu zapytanie przez pythona. 
            #found_more_than_one_book = session.query(Author, func.count(Book.id).label("book_count")).join(Book).group_by(Author.id).all()
            #for author, book_count in found_more_than_one_book:
            #    if book_count >1:
            #        print(f"Autor: {author.name}, Ilość książek: {book_count}")


            #Lepsza wersja - zapytanie przez SQL
            found_more_than_one_book = (
                session.query(Author).
                join(Book).
                options(selectinload(Author.books)).
                group_by(Author.id).
                having(func.count(Book.id)>1).all()
                )
            

            print("\nAutorzy posiadający więcej niż 1 książkę: \n")

            for author in found_more_than_one_book:
                titles=[book.title for book in author.books]
                print(f"{author.name} książki: {', '.join(titles)}")    
            
            


        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()




if __name__ == "__main__":
    main()