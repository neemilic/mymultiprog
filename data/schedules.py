import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Schedule(SqlAlchemyBase):
    __tablename__ = 'schedules'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    time = sqlalchemy.Column(sqlalchemy.Time, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
