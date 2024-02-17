from sqlalchemy import create_engine

login = ''
password = ''
hostname = ''
conn_string = 'mysql+pymysql://%s:%s@%s?charset=utf8mb3' % (login, password, hostname)
engine = create_engine(conn_string)