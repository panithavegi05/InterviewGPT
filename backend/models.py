from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    resume = Column(String)


class Interview(Base):

    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True)

    candidate_id = Column(Integer)

    question = Column(String)

    answer = Column(String)

    score = Column(Integer)


from database import engine

Base.metadata.create_all(bind=engine)


class Report(Base):

    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)

    candidate_id = Column(Integer)

    recommendation = Column(String)