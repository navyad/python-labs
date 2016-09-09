from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    attrs = Column(PickleType)

    def __repr__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()


def create_user(session, **kwargs):
    kwargs['attrs'] = {"country": "India", "city": "Bangalore"}
    user = User(**kwargs)
    session.add(user)
    return session


def update_user(session, user):
    user.last_name = "Kumar"
    session.commit()
    return session


def query_filter(session, **kwargs):
    query = session.query(User)
    records = query.filter_by(**kwargs)
    return records

if __name__ == "__main__":
    session = get_session()
    user_1 = {"first_name": "Ed", "last_name": "Harris"}
    session = create_user(session, **user_1)

    user_2 = {"first_name": "Nav", "last_name": "Yadav"}
    session = create_user(session, **user_2)

    user_3 = {"first_name": "Bob", "last_name": "Yadav"}
    session = create_user(session, **user_3)

    # type(_query): sqlalchemy.orm.query.Query
    _query = query_filter(session, **{"last_name": "Yadav"})
    print [entry.first_name for entry in _query.all()]

    session = update_user(session, _query.first())
    _query = query_filter(session, **{"last_name": "Kumar"})
    print _query.first()

    _query = query_filter(session, **{"last_name": "Bale"})
    print _query.first()  # None

    _query = session.query(User).filter()
    print [entry.attrs for entry in _query.all()]
