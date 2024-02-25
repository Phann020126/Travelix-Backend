from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from tourist_module import Tourist
from excursion_module import Excursion

Base = declarative_base()

class ExcursionReservation(Base):
    __tablename__ = 'excursion_reservation'

    tourist_id = Column(Integer, ForeignKey('tourist.tourist_id'), primary_key=True)
    excursion_id = Column(Integer, ForeignKey('excursion.excursion_id'), primary_key=True)
    reservation_date = Column(Date, nullable=False)

    # Define foreign key relationships
    tourist = relationship("Tourist", back_populates="excursion_reservations")
    excursion = relationship("Excursion", back_populates="tourist_reservations")

    def __repr__(self):
        return f"<ExcursionReservation(tourist_id={self.tourist_id}, excursion_id={self.excursion_id}, reservation_date={self.reservation_date})>"

# Set up relationships
Tourist.excursion_reservations = relationship("ExcursionReservation", back_populates="tourist")
Excursion.excursion_reservations = relationship("ExcursionReservation", back_populates="excursion")
