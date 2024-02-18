from sqlalchemy import Column, Integer, Numeric, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from agency_module import Agency 
from extended_excursion_module import ExtendedExcursion 
from package_offer_facility_module import PackageOfferFacility 
from package_reservation_module import PackageReservation

Base = declarative_base()

class Package(Base):
    __tablename__ = 'package'

    package_id = Column(Integer, primary_key=True, autoincrement=True)
    agencia_id = Column(Integer, ForeignKey('agency_module.agencia_id'), nullable=False)
    excursion_id = Column(Integer, ForeignKey('extended_excursion.excursion_id'), nullable=False)
    package_duration = Column(Integer, nullable=False)
    package_description = Column(String(100), nullable=False)
    package_price = Column(Numeric, nullable=False)

    # Relationships
    agency = relationship(Agency, back_populates='packages')  
    extended_excursion = relationship(ExtendedExcursion, back_populates='packages')
    package_offer_facility = relationship(PackageOfferFacility, back_populates='package')
    package_reservations = relationship(PackageReservation, back_populates='package')

    def __repr__(self):
        return f"<Package(package_id={self.package_id}, agencia_id={self.agencia_id}, excursion_id={self.excursion_id}, package_duration={self.package_duration}, package_description={self.package_description}, package_price={self.package_price})>"
