from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    serialize_rules=('-baked_goods.bakery',)

    id = db.Column(db.Integer, primary_key=True)

    baked_goods=db.relationship('BakedGood',backref='bakery')

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    serialize_rules=('-bakery.baked_goods')

    id = db.Column(db.Integer, primary_key=True)
    bakery_id = db.Column(db.Integer,db.ForeignKey('bakeries.id'))

    bakery=db.relationship('Bakery',backref='baked_goods')
    