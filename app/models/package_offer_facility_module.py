from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from package_module import Package
from excursion_module import Excursion
from agency_module import Agency
from facility_module import Facility

Base = declarative_base()

class PackageOfferFacility(Base):
    __tablename__ = 'package_offer_facility'

    package_id = Column(Integer, ForeignKey('package.package_id'), primary_key=True)
    excursion_id = Column(Integer, ForeignKey('excursion.excursion_id'), primary_key=True)
    agency_id = Column(Integer, ForeignKey('agency.agency_id'), primary_key=True)
    facility_id = Column(Integer, ForeignKey('facility.facility_id'), primary_key=True)

    # Define foreign key relationships
    package = relationship(Package, back_populates="offer_facilityes")
    excursion = relationship(Excursion, back_populates="package_offer_facility")
    agency = relationship(Agency, back_populates="package_offer_facility")
    facility = relationship(Facility, back_populates="package_offer_facility")

    def __repr__(self):
        return f"<PackageOfferFacility(package_id={self.package_id}, excursion_id={self.excursion_id}, agency_id={self.agency_id}, facility_id={self.facility_id})>"


# Set up relationships
Package.package_offer_facility = relationship(PackageOfferFacility, back_populates="package")
Excursion.package_offer_facility = relationship(PackageOfferFacility, back_populates="excursion")
Agency.package_offer_facility = relationship(PackageOfferFacility, back_populates="agency")
Facility.package_offer_facility = relationship(PackageOfferFacility, back_populates="facility")
