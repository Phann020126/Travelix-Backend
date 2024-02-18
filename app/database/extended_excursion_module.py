from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database.excursion_module import Excursion
from package_module import Package
from package_reservation_module import PackageReservation

Base = declarative_base()

class ExtendedExcursion(Base):
    __tablename__ = 'extended_excursion'

    excursion_id = Column(Integer, primary_key=True)
    
    # Define Foreign Key relationship with the 'excursion' table
    excursion = relationship(Excursion, back_populates='extended_excursion', uselist=False)
    packages = relationship(Package, back_populates='extended_excursion')
    package_reservations = relationship(PackageReservation, back_populates='extended_excursion')


    def __repr__(self):
        return f"<ExcursionProlongada(excursion_id={self.excursion_id})>"
    
# Set up relationships
Excursion.extended_excursion = relationship(ExtendedExcursion, back_populates='excursion', uselist=False)
Package.extended_excursion = relationship(ExtendedExcursion, back_populates='packages')
PackageReservation.extended_excursion = relationship(ExtendedExcursion, back_populates='package_reservations')
    