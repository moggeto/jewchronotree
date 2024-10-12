from core.models.people import Person

# Создание записи
def create_person(session, name, birth_date=None, death_date=None, tribe=None, role=None):
    new_person = Person(name=name, birth_date=birth_date, death_date=death_date, tribe=tribe, role=role)
    session.add(new_person)
    session.commit()
    return new_person

# Чтение всех записей
def get_all_people(session):
    return session.query(Person).all()

# Чтение записи по ID
def get_person_by_id(session, person_id):
    return session.query(Person).filter_by(id=person_id).first()

# Обновление записи
def update_person(session, person_id, **kwargs):
    person = session.query(Person).filter_by(id=person_id).first()
    if not person:
        return None

    for key, value in kwargs.items():
        if hasattr(person, key):
            setattr(person, key, value)

    session.commit()
    return person

# Удаление записи
def delete_person(session, person_id):
    person = session.query(Person).filter_by(id=person_id).first()
    if person:
        session.delete(person)
        session.commit()
        return True
    return False