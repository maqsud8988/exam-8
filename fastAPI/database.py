from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine('postgresql://postgres:maqsud8988localhost:5432/exam_8', echo=True)
Base = declarative_base()
session = sessionmaker()

