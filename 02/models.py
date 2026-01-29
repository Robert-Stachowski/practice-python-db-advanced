from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books_var = relationship("Book", back_populates="author_var") # Dziwna nazwa zmiennej, ale przynajmniej nie miesza mi się z nazwą tabeli...


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author_var = relationship("Author", back_populates="books_var") #to samo co wyżej ;) 
