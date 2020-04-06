import pymysql
from common.Config import config


class Database:
    """
    this class is defined a database connection which can
    execute QUERY  INSERT  UPDATE  DELETE options
    """
    def __init__(self):
        self.db = pymysql.connect(host=config["host"], port=config["port"], user=config["username"],
                                  passwd=config["password"], db=config["schema"], charset='utf8')
        self.cursor = self.db.cursor()

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print("query success,the result is:{}".format(result))
        except Exception as e:
            print("query failed! the reason is: {}".format(e))

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("update data success.")
        except Exception as e:
            self.db.rollback()
            print("update failed.the reason is: {}".format(e))

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("insert data success.")
        except Exception as e:
            self.db.rollback()
            print("insert failed.the reason is: {}".format(e))

    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("delete data success.")
        except Exception as e:
            self.db.rollback()
            print("delete failed.the reason is: {}".format(e))

    def quit(self):
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    database = Database()
    # test query function
    sql = "select * from student"
    database.query(sql)

    # test insert
    sql = "insert into student(name,sex,stu_no,tea_no,score) values('test2','man','123453','123','23')"
    database.insert(sql)


