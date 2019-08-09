from show_create_table import Show_Create_Table_Sql
from save_to_file import Export
from config import *

if __name__ == '__main__':
    show_create_table = Show_Create_Table_Sql()
    for database in show_create_table.show_databases():
        if database in IGNORE_DATABASE:
            # print(database)
            pass
        else:
            for table in show_create_table.show_tables(database):
                contents = show_create_table.create_table_sql(database, tablename=table)
                for content in contents:
                    print(content)
                    exporter = Export(database, table).save_as_sql(content)
