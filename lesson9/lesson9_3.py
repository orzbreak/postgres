#請幫我自訂一個function
#連線至postgres DB
#建立環境參數的樣板
import psycopg2
#請幫我建立一個function
#傳入connection 函數
#建立一個cursor
#執行SQL查詢
#並回傳查詢結果

def execute_query(conn, query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
            return result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def connect_db()-> psycopg2.extensions.connection:
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="raspberry",
            host="host.docker.internal",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None





def main():
    conn = connect_db()
    if conn:
        print("Connection successful!")
        query = "SELECT * FROM your_table_name;"
        results = execute_query(conn, query)
        if results is not None:
            for row in results:
                print(row)
        conn.close()
    else:
        print("Connection failed.")
    pass

if __name__ == '__main__':
    main()