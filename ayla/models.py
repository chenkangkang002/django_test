from django.db import models

# Create your models here.
from sqlalchemy.testing import db


class Project(db.Model):
    __tablename__ = 'project'  # 表名
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(200),nullable=False)  # 项目名称
    parent_id = db.Column(db.Integer, nullable=False)  # 父级id