from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


person_skill = Table(
    "person_skill",
    Base.metadata,
    person_id = Column(Integer, ForeignKey("person.id"), primary_key=True),
    skill_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)
    )


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    skills = relationship("Skill", secondary=person_skill, back_populates="persons")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    persons = relationship("Person", secondary=person_skill, back_populates="skills")




