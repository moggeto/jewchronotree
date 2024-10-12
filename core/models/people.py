from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# many to many study relationship
study_association_table = Table('study_association', Base.metadata,
                                Column('teacher_id', Integer, ForeignKey('person.id')),
                                Column('student_id', Integer, ForeignKey('person.id'))
                                )


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    birth_date = Column(String)
    death_date = Column(String)
    tribe = Column(String)
    role = Column(String)
    description = Column(String)

    #family
    father_id = Column(Integer, ForeignKey('person.id'))
    children = relationship('Person', backref='father', remote_side=[id])


    #study
    teachers = relationship('Person',
                            secondary = study_association_table,
                            primaryjoin = id == study_association_table.c.student_id,
                            secondaryjoin = id == study_association_table.c.teacher_id,
                            backref = 'students')


    def __repr__(self):
        return f"<Person(name={self.name}, birth_date={self.birth_date}, death_date={self.death_date}, tribe={self.tribe}, role={self.role}), description={self.description}>"