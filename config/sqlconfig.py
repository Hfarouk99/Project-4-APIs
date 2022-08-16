import sqlalchemy as alch
import pymysql
import os
import dotenv

dotenv.load_dotenv()
password = os.getenv("sql_pw")                                 #pulls password to access SQL
dbName = "spotify"                                                     # finds the database that will create the conection
conectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}" # will stablish the conection
engine = alch.create_engine(conectionData)                          # we create the engine to run the confirg and conect.