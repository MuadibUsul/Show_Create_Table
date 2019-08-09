from create_conn_mysql import ConnMysql
from config import *

"""
获取建表数据的一个类
"""


class Show_Create_Table_Sql(object):
    def __init__(self):
        """
        创建数据库连接，连接数据库的数据来自配置文件config.py
        """
        self.Connect = ConnMysql(HOST=HOST, USERNAME=USERNAME, PASSWORD=PASSWORD)
        self.cursor = self.Connect.conn()

    def show_databases(self):
        """
        查出该账号下的数据库名称，并返回一个迭代器
        :return:
        """
        sql = 'show databases;'
        results = self.Connect.run_sql(self.cursor, sql)
        for result in results:
            yield result[0]

    def show_tables(self, database):
        """
        传入一个数据库名，获取其名下所有表的名称
        :param database:
        :return:
        """
        sql = "select table_name from information_schema.tables where table_schema='" + database + "' and table_type='base table'"
        # print(sql)
        results = self.Connect.run_sql(self.cursor, sql)
        for result in results:
            yield result[0]

    def create_table_sql(self, database, tablename):
        """
        传入库和表的对应关系，并获取相对应的表的建表语句
        :param database:
        :param tablename:
        :return:
        """
        sql = 'show create table ' + database + '.' + tablename
        # print(sql)
        results = self.Connect.run_sql(self.cursor, sql)[0]
        for result in results:
            yield result

    def close_conn(self):
        """
        关闭数据库连接
        :return:
        """
        self.Conn.__close__()

# if __name__ == '__main__':
#     print(Show_Create_Table_Sql().create_table_sql('database_name', 'table_name'))
