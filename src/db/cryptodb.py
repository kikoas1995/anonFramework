from pysqlcipher import dbapi2 as sqlcipher

def connect_db(name):
    try:
        db = sqlcipher.connect(name)
        db.executescript('pragma key="testing"; pragma kdf_iter=64000;')
        db.execute('select * from people;').fetchall()
    except Error as e:
        print(e)
    finally:
        db.close()

