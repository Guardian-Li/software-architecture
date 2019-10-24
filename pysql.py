import pymysql


class phone():
    def __init__(self):
        self.con = pymysql.connect(host="localhost", user="root",password="maybe@1998",database="phone",charset="utf8")
        curs = self.con.cursor()
        sql = "select * from link order by name"
        curs.execute(sql)
        p = curs.fetchall()
        self.__phoneList = p
        self.__curs = curs
        
        
        

    def search(self,str =None, number = None):
        for x in self.__phoneList:
            if str == x[0] or number == x[1]:
                return x
    
    def phoneListShow(self):
        return self.__phoneList

    def insert(self,name = None, number = None):
        sql = "insert into link (name,phone_number) values ('%s','%s');"%(name,number)
        self.__curs.execute(sql)
        self.con.commit()
        
    
    def deleteLink(self,name=None, number = None):
        if name != None and number != None:
            sql = "delete from link where name = '%s' and phone_number = '%s';" % (name,number)
        self.__curs.execute(sql)
        self.con.commit()


    def closeSql(self):
        self.con.close()

if __name__ == "__main__":
    p = phone()
    print(p.search("gxp"))