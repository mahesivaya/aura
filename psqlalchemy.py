from sqlalchemy import create_engine
# for postgreSQL database credentials can be written as 
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
database = 'postgres'
# for creating connection string
connection_str = "postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
# SQLAlchemy engine
engine = create_engine(connection_str)
# you can test if the connection is made or not
try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')






# ------------ Another Way -------------------

# def get_connection():
#     return create_engine(
#         url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
#     )

# if __name__ == '__main__':
#     try:       
#         # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#         engine = get_connection()
#         print(
#             f"Connection to the {host} for user {user} created successfully.")
#     except Exception as ex:
#         print("Connection could not be made due to the following error: \n", ex)


