import pymysql

import click
from flask import current_app, g
from flask.cli import with_appcontext

#获取数据库连接
def get_db():
    """
    @return: 数据库连接对象，使用MySQL
    """
    if 'db' not in g:
        g.db = pymysql.connect(
            'localhost',
            'root',
            'beiming135',
            'cs'
        )

    return g.db

#关闭连接
def close_db(e=None):
    """
       取出存放在g中的数据库连接对象，
       如果没有返回None

    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


#初始化数据库
def init_db():
    """
    执行schema.sql中的sql语句，初始化数据表
    """
    db = get_db()
    cursor = db.cursor()
    with current_app.open_resource('schema.sql') as f:
        sqls = f.read().decode('utf-8').replace('\n','').split(';')
        while '' in sqls:
            sqls.remove('')
        for sql in sqls:
            cursor.execute(sql)

#创建一个名为‘init-db’的命令行，调用init_db函数
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    #告诉 Flask 在返回响应后进行清理的时候调用此函数
    app.teardown_appcontext(close_db)
    #添加一个新的 可以与 flask 一起工作的命令。(也就是可以通过flask init-db(上面绑定的命令名) 来调用该函数)
    app.cli.add_command(init_db_command)
