import psycopg2, os 

def getConnection():
    try:
        connection = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        print(os.getenv('DB_NAME'),os.getenv('DB_USER'),os.getenv('DB_PASS'),os.getenv('DB_HOST'),os.getenv('DB_PORT'))
        print(f"DB connection Successfull !!")
        return connection
    except Exception as e:
        print(f"{e}")
        return None
    
getConnection()
