#Connecting to a dockerized mysql DB
#Make sure the docker MySql is running
# docker run -d -p 3306:3306 --name mysql  -e MYSQL_DATABASE=sample -e MYSQL_USER=mysql -e MYSQL_ROOT_PASSWORD=mysql -e MYSQL_PASSWORD=mysql -d mysql:latest

'''
All about SQL
MySql 8 is running as a docker image and  using python mysql connector to access it

'''
import mysql.connector
class DBTalk:
    def sql_loader (self):
        emps = [
           (9001, "Jeff Russell", "sales"),
           (9002, "Jane Boorman", "sales"),
           (9003, "Tom Heints", "sales")
          ]
        conn = self.get_connection()
        #Clean tables
        sql = 'delete from salary'
        # Delete stuff from emp
        self.execute_sql(sql, conn, False)
        sql = 'delete from emps'
        #Delete stuff from emp
        self.execute_sql(sql,conn, False)
        #Delete stuff from sales
        sql = 'delete from orders'
        # Delete stuff from emp
        self.execute_sql(sql,conn, True)
        #Get new Connection since connection is closed
        conn = self.get_connection()
        for emp in emps:
            empNumber = emp[0]
            empName = emp[1]
            empDept = emp[2]
            sql = f'insert into emps values ({empNumber} , "{empName}" , "{empDept}")'
            self.execute_sql(sql,conn, False)
        #Commit all Emps
        self.execute_sql(None, conn, True)
        #Commit salaries
        conn = self.get_connection()
        salary = [
            (9001, 3000),
            (9002, 2800),
            (9003, 2500)
        ]
        query_add_salary = ("""INSERT INTO salary (empno, salary) VALUES (%s, %s)""")
        cursor =conn.cursor()
        for sal in salary:
            cursor.execute(query_add_salary, sal)
        try:
            conn.commit()

            # Querying to get result
            query = ("SELECT * FROM emps WHERE  empno > %s")
            empno = 9001
            cursor.execute(query, (empno,)) #Value must be a tuple or list
            for (empno, empname, job) in cursor:
                print("{}, {}, {}".format(empno, empname, job))

        except Exception as e:
            print(f'Exception happened while committing {e}')
        finally:
            try:
                cursor.close()
                conn.close()
            except Exception as e:
                print(f'Could not close connection {e}')


    def execute_sql (self, sqlstring, conn, commit):
        try:
            if sqlstring:
                cursor = conn.cursor()
                cursor.execute(sqlstring)
            if commit:
                conn.commit()
        except Exception as e:
            print(f'There was an exception that occured {e}')
            conn.rollback()
        finally:
            if sqlstring:
                cursor.close()
            if commit:
                conn.close()

    def get_connection(self):
        return mysql.connector.connect(user='mysql', password='mysql', host='127.0.0.1', database='sample')

sqlRoller = DBTalk()
sqlRoller.sql_loader()


