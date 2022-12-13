import mysql.connector as ap
import traceback

def insert_rows(args):
    sql ="INSERT INTO info1(name,age) VALUES(%s,%s)"
    try:
        conn = ap.connect(
            host='localhost',
            passwd="nishant@123",
            port=3306,
            database="newone",
            user="root"
        )
        cursor = conn.cursor()
        cursor.execute(sql,args)
    except:
        print(traceback.format_exc())

    else:
        conn.commit()
    finally:

        cursor.close()
        conn.close()

def update_rows(args):
    sql = "UPDATE info1 SET name=%s,age=%s WHERE id=%s; "
    try:
        conn = ap.connect(
            host='localhost',
            passwd="nishant@123",
            port=3306,
            database="newone",
            user="root"
        )
        cursor1 = conn.cursor()
        cursor1.execute(sql,args)
    except:
        print(traceback.format_exc())

    else:
        conn.commit()
    finally:

        cursor1.close()
        conn.close()

def delete_rows(args):
    sql = "DELETE FROM info1 WHERE id=%s;"

    try:
        conn = ap.connect(
            host='localhost',
            passwd="nishant@123",
            port=3306,
            database="newone",
            user="root"
        )
        cursor2 = conn.cursor()
        cursor2.execute(sql,args)
    except:
        print(traceback.format_exc())

    else:
        conn.commit()
    finally:

        cursor2.close()
        conn.close()

def insert_args():
    name=input("enter name:-\n")
    age =input("enter age:-\n")
    insert_rows((name,age))

def update1():
    name=input("enter name:-\n")
    age = input("enter age:-\n")
    id1= input("enter id:-\n")
    update_rows((name,age,id1))

def delete1():
    id1=input("enter id:-\n")
    delete_rows((id1,))

dic1={"1":insert_args,"2":update1,"3":delete1}
while True:
    comand=input(""" choice one of the below
                1) insert
                2) update
                3) delete \n""")
    dic1[comand]()
    if( input("press 'c' to escape").lower()=="c"):
        break

print("done")


# qp="UPADE INTO emfo1 name='rahul' where = id='4'" \
#    "delete from info1 where id =5.
