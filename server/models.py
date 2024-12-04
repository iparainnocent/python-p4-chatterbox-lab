from datetime import datetime
import pytz
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, MetaData
from sqlalchemy_serializer import SerializerMixin

gmt_plus_3 = pytz.timezone("Africa/Nairobi")
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)  # Optional: Set to not nullable if required
    username = db.Column(db.String, nullable=False)  # Optional: Set to not nullable if required
    created_at = db.Column(
        DateTime(timezone=True),
        server_default=db.func.now(),  # Use server default for creation time
        nullable=False,
    )
    updated_at = db.Column(
        DateTime(timezone=True),
        onupdate=db.func.now(),  # Automatically update on record update
        server_default=db.func.now(),  # Set default to now on creation
        nullable=False,
    )