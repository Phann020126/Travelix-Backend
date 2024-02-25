from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from tourist_module import Tourist
from package_module import Package
from extended_excursion_module import ExtendedExcursion
from agency_module import Agency

Base = declarative_base()

class PackageReservation(Base):
    __tablename__ = 'package_reservation'

    tourist_id = Column(Integer, ForeignKey('tourist.tourist_id'), primary_key=True)
    package_id = Column(Integer, ForeignKey('package.package_id'), primary_key=True)
    extended_excursion_id = Column(Integer, ForeignKey('extended_excursion.excursion_id'), primary_key=True)
    agency_id = Column(Integer, ForeignKey('agency.agency_id'), primary_key=True)
    reservation_date = Column(Date, nullable=False)

    # Define foreign key relationships
    tourist = relationship(Tourist, back_populates="package_reservations")
    package = relationship(Package, back_populates="tourist_reservations")
    extended_excursion = relationship(ExtendedExcursion, back_populates="package_reservations")
    agency = relationship(Agency, back_populates="package_reservations")

    def __repr__(self):
        return f"<ReservaciónPaquete(turista_id={self.tourist_id}, paquete_id={self.package_id}, excursion_id={self.extended_excursion_id}, agencia_id={self.agency_id}, fecha_reservación='{self.reservation_date}')>"
    
# Set up relationships
Tourist.package_reservations = relationship(PackageReservation, back_populates="tourist")
Package.package_reservations = relationship(PackageReservation, back_populates="package")
ExtendedExcursion.package_reservations = relationship(PackageReservation, back_populates="extended_excursion")
Agency.package_reservations = relationship(PackageReservation, back_populates="agency")
