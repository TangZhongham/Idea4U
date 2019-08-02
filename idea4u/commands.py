import click
from idea4u import app
from idea4u import db


@app.cli.command()
def initdb():
    db.create_all()
    click.echo("数据库创建中")
