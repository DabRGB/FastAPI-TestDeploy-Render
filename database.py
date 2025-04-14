import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = os.environ.get("postgresql://todolist_django_render_pqsu_user:0WNrhPMDSLxLPkX65wUXUwH266NARXx5@dpg-cvnu4mruibrs73aeldg0-a.singapore-postgres.render.com/todolist_django_render_pqsu")

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
