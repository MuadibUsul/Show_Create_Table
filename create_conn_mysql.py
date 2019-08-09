import pymysql


class ConnMysql(object):
    def __init__(self, HOST, USERNAME, PASSWORD):
        """
        传入地址，用户名，密码并创建一个DB连接
        :param HOST:
        :param USERNAME:
        :param PASSWORD:
        """
        self.host = HOST
        self.username = USERNAME
        self.password = PASSWORD
        self.db = pymysql.connect(self.host, self.username, self.password)

    def conn(self):
        """
        返回一个游标
        :return:
        """
        cursor = self.db.cursor()
        return cursor

    def run_sql(self, cursor, sql):
        """
        传入游标与相应的SQL代码，并执行
        :param cursor:
        :param sql:
        :return:
        """
        cursor.execute(sql)
        return cursor.fetchall()

    def __close__(self):
        """
        关闭数据库连接
        :return:
        """
        self.db.close()