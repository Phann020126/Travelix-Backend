from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from excursion_reservation_module import ExcursionReservation
from package_reservation_module import PackageReservation
from tourist_be_tourist_type_module import TouristBeTouristType

Base = declarative_base()

class Tourist(Base):
    __tablename__ = 'tourist'

    tourist_id = Column(Integer, primary_key=True, autoincrement=True)
    tourist_name = Column(String(50), nullable=False)
    nationality = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Turista(turista_id={self.tourist_id}, turista_nombre='{self.tourist_name}', nacionalidad='{self.nationality}')>"

    # Add the back_populates attribute to establish the bidirectional relationship
    excursion_reservations = relationship(ExcursionReservation, back_populates="tourist")
    package_reservations = relationship(PackageReservation, back_populates="tourist")
    tourist_be_tourist_type = relationship(TouristBeTouristType, back_populates="tourist")