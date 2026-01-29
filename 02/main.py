from db import Session, engine
from models import Author, Book, Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func



def main():
    Base.metadata.create_all(engine)

    with Session() as session:
        try:
            
            # Autor1
            author1 = Author(name="George Orwell")
            author1.books_var.append(Book(title="1984"))
            author1.books_var.append(Book(title="Animal Farm"))

            # Autor2
            author2 = Author(name="J.R.R. Tolkien")
            author2.books_var.append(Book(title="The Hobbit"))
            author2.books_var.append(Book(title="The Lord of the Rings"))
            author2.books_var.append(Book(title="The Silmarillion"))

            session.add_all([author1, author2])
            session.commit()





            found_author_books = session.query(Author).filter(Author.name=="J.R.R. Tolkien").one()
            for book in found_author_books.books_var:
                print(f"Autor: {found_author_books.name}, Książki: {book.title}")



            # Przyjrzyj się proszę temu zapytaniu — działa, ale nie wiem, czy jest poprawnie złożone.
            found_more_than_one_book = session.query(Author, func.count(Book.id).label("book_count")).join(Book).group_by(Author.id).all()
            for author, book_count in found_more_than_one_book:
                if book_count >1:
                    print(f"Autor: {author.name}, Ilość książek: {book_count}")



        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()




if __name__ == "__main__":
    main()