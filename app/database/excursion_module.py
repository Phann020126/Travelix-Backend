from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from agency_work_excursion_module import AgencyWorkExcursion
from package_offer_facility_module import PackageOfferFacility
from excursion_reservation_module import ExcursionReservation
from extended_excursion_module import ExtendedExcursion

Base = declarative_base()

class Excursion(Base):
    __tablename__ = 'excursion'

    excursion_id = Column(Integer, primary_key=True, autoincrement=True)
    excursion_price = Column(String(50), nullable=False)
    departure_location = Column(String(50), nullable=False)
    departure_day_of_week = Column(String(20), nullable=False)
    departure_time = Column(Time, nullable=False)
    arrival_location = Column(String(50), nullable=False)
    arrival_day_of_week = Column(String(20), nullable=False)
    arrival_time = Column(Time, nullable=False)

    def __repr__(self):
        return f"<Excursion(id={self.excursion_id}, precio={self.excursion_price}, salida={self.departure_location}, dia_salida={self.departure_day_of_week}, hora_salida={self.departure_time}, llegada={self.arrival_location}, dia_llegada={self.arrival_day_of_week}, hora_llegada={self.arrival_time})>"
    
    # Add the back_populates attribute to establish the bidirectional relationship
    agency_work_excursions = relationship(AgencyWorkExcursion, back_populates='excursion')
    package_offer_facility = relationship(PackageOfferFacility, back_populates='excursion')
    excursion_reservations = relationship(ExcursionReservation, back_populates='excursion')
    extended_excursion = relationship(ExtendedExcursion, back_populates='excursion', uselist=False)