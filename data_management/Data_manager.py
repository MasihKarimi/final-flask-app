from sqlalchemy import create_engine
import pandas as pd


class DataManager:
    def __init__(self, ip_address, user_name, user_mdp, db):
        self.ip_address = ip_address
        self.user_name = user_name
        self.user_mdp = user_mdp
        self.db = db
        self.engine_details = "mysql+pymysql://{user}:{pw}@{ip_add}/{db}".format(user=self.user_name, pw=self.user_mdp,
                                                                                 ip_add=self.ip_address, db=self.db)

    def db_connection(self):
        engine = create_engine(self.engine_details)
        return engine

    def import_db(self):
        # Please enter username, password and data name
        data = pd.read_sql('SELECT * FROM profile_recommendation_db',
                           con=self.db_connection())
        return data



