import pymysql

import click
from flask import current_app, g
from flask.cli import with_appcontext

#连接数据库
def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            'localhost',
            'root',
            'beiming135',
            'cs'
            #current_app.config['DATABASE'],
            #detect_types=pymysql.PARSE_DECLTYPES
        )
        #g.db.row_factory = pymysql.Row

    return g.db

#关闭连接
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
#初始化数据库
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        sqls = f.read().decode('utf-8').replace('\n','').split(';')
        while '' in sqls:
            sqls.remove('')
        for sql in sqls:
            db.cursor().execute(sql)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
