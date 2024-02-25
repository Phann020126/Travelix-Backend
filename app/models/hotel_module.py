from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.offer_module import Offer
from app.database.excursion_asociate_hotel_module import ExcursionAsociateHotel


Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotel'

    hotel_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    hotel_name = Column(String(50), nullable=False)
    hotel_address = Column(String(100), nullable=False)
    hotel_category = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Hotel(id={self.hotel_id}, nombre={self.hotel_name}, direccion={self.hotel_address}, categoria={self.hotel_category})>"
 
    hotel = relationship(Offer, back_populates="offers")
    excursion_asociate_hotel = relationship(ExcursionAsociateHotel, back_populates="hotel")
    