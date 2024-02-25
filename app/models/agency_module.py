from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from package_module import Package
from agency_work_excursion_module import AgencyWorkExcursion
from agency_offer_module import AgencyOffer
from package_offer_facility_module import PackageOfferFacility
from package_reservation_module import PackageReservation

Base = declarative_base()

class Agency(Base):
    __tablename__ = 'agency'

    agency_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    agency_name = Column(String(50), nullable=False)
    agency_address = Column(String(100), nullable=False)
    fax_number = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Agencia(id={self.agency_id}, nombre={self.agency_name}, direccion={self.agency_address}, fax={self.fax_number}, email={self.email})>"
    
    # Add the back_populates attribute to establish the bidirectional relationship
    packages = relationship(Package, back_populates='agency')
    agency_work_excursions = relationship(AgencyWorkExcursion, back_populates='agency')
    agency_offers = relationship(AgencyOffer, back_populates='agency')
    package_offer_facility = relationship(PackageOfferFacility, back_populates='agency')
    package_reservations = relationship(PackageReservation, back_populates='agency')
