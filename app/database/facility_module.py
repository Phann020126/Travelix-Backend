from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from package_offer_facility_module import PackageOfferFacility

Base = declarative_base()

class Facility(Base):
    __tablename__ = 'facility'

    facility_id = Column(Integer, primary_key=True, nullable=False)
    facility_description = Column(String(100), nullable=False)

    # Add the back_populates attribute to establish the bidirectional relationship
    package_offer_facility = relationship(PackageOfferFacility, back_populates='facility')

    def __repr__(self):
        return f"<Facility(facility_id={self.facility_id}, facility_description={self.facility_description})>"
