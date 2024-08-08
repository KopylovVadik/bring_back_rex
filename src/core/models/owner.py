import uuid

from sqlalchemy import Column, String, DateTime, func, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from core.models.base import Base


class Owner(Base):
    __tablename__ = 'owners'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    first_name = Column(String, comment='Имя')
    last_name = Column(String, comment='Фамилия')
    phone_number = Column(String, unique=True, comment='Номер телефона')
    email = Column(String, unique=True, comment='Адрес электронной почты')
    telegram = Column(String, unique=True, nullable=True, comment='Телеграм')
    created_at = Column(DateTime, default=func.now())


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String, comment='Кличка')
    birth_date = Column(Date, comment='Дата рождения')
    brand = Column(String, nullable=True, comment='Порода')
    special_feature = Column(String, nullable=True, comment='Особые приметы')
    owner_id = Column(UUID(as_uuid=True), ForeignKey('owners.id'))
    created_at = Column(DateTime, default=func.now())
