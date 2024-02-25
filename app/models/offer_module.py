from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database.hotel_module import Hotel
from agency_offer_module import AgencyOffer

Base = declarative_base()

class Offer(Base):
    __tablename__ = 'offer'

    oferta_id = Column(Integer, primary_key=True, autoincrement=True)
    oferta_price = Column(Numeric, nullable=False)
    oferta_description = Column(String(100))
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)

    # Define the relationship between oferta and hotel
    hotel = relationship(Hotel, back_populates="offers")
    agency_offers = relationship(AgencyOffer, back_populates='offers')


    def __repr__(self):
        return f"<Oferta(oferta_id={self.oferta_id}, precio={self.oferta_price}, descripcion={self.oferta_description}, hotel_id={self.hotel_id})>"
