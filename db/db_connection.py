import pymysql

host = 'nomizodb-do-user-6621383-0.a.db.ondigitalocean.com'
user = 'doadmin'
password = 'dl41ga9bofbves9a'
port = 25060
db = 'defaultdb'


def connection():
    cnx = pymysql.Connect(host=host,
                          user=user,
                          password=password,
                          port=port,
                          db=db)

    try:
        with cnx.cursor() as cursor:
            sql1 = "SELECT * FROM `client`"
            cursor.execute(sql1)
            # result = cursor.fetchone()
            for row in cursor:
                print(row)

    finally:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    connection()
