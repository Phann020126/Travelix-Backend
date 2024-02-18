from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from extended_excursion_module import ExtendedExcursion

Base = declarative_base()

class ExcursionAsociateHotel(Base):
    __tablename__ = 'excursion_asociate_hotel'

    excursion_id = Column(Integer, ForeignKey('extended_excursion.excursion_id'), primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), primary_key=True)
    departure_date = Column(Date, nullable=False)
    arrival_date = Column(Date)

    # Define the relationship with the 'ExtendedExcursion' class
    excursion = relationship(ExtendedExcursion, back_populates="excursion_asociate_hotel")

    # Define the relationship with the 'Hotel' class
    hotel = relationship("Hotel", back_populates="excursion_asociate_hotel")

    def __repr__(self):
        return f"ExcursionAsociateHotel(excursion_id={self.excursion_id}, hotel_id={self.hotel_id}, fecha_salida={self.departure_date}, fecha_llegada={self.arrival_date})"
