from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from agency_module import Agency
from offer_module import Offer

Base = declarative_base()

class AgencyOffer(Base):
    __tablename__ = 'agency_offer'

    agency_id = Column(Integer, ForeignKey('agency.agency_id'), primary_key=True)
    oferta_id = Column(Integer, ForeignKey('offer.offer_id'), primary_key=True)
    agency_precio = Column(Numeric, nullable=False)

    # Define foreign key relationships
    agency = relationship(Agency, back_populates="agency_offer")
    offer = relationship(Offer, back_populates="agency_offer")

    def __repr__(self):
        return f"AgencyOffer(agency_id={self.agency_id}, oferta_id={self.oferta_id}, agency_precio={self.agency_precio})"