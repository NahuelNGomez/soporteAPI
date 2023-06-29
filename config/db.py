from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://dbname_vctu_user:o5llq8bCpKyW3RRpvyZ60XsWnNY8XmaC@dpg-ci5vl498g3n4q9ulaju0-a.oregon-postgres.render.com:5432/dbname_vctu"

engine = create_engine(DATABASE_URL)

meta = MetaData()
conn = engine.connect()