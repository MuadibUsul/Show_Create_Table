import os

"""
输出成SQL文件的一个文件类
"""


class Export(object):
    def __init__(self, database, filename):
        """
        传入数据库的名称作为文件夹名，传入该数据库内的表名称作为文件名
        :param database:
        :param filename:
        """
        self.mkdir_dir(database)
        self.filepath = './create_table_sql_data/' + database + '/' + filename + '.sql'
        self.FileObj = open(self.filepath, 'w')

    def mkdir_dir(self, database):
        """
        传入数据库的名称，也就是文件夹名称，判断是否存在。
        不存在则创建该文件夹
        :param database:
        :return:
        """
        file_dir = './create_table_sql_data/' + database
        if os.path.exists(file_dir):
            pass
        else:
            os.mkdir('./create_table_sql_data/' + database)

    def save_as_sql(self, content):
        """
        传入需要写入的内容
        :param content:
        :return:
        """
        self.FileObj.writelines(content)

    def __close__(self):
        """
        关闭文件io
        :return:
        """
        self.FileObj.close()
