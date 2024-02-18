from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from tourist_module import Tourist
from tourist_type_module import TouristType

Base = declarative_base()

class TouristBeTouristType(Base):
    __tablename__ = 'tourist_be_tourist_type'

    tourist_id = Column(Integer, ForeignKey('tourist.tourist_id'), primary_key=True)
    tourist_type_id = Column(Integer, ForeignKey('tourist_type.tourist_type_id'), primary_key=True)

    # Define foreign key relationships
    tourist = relationship(Tourist, back_populates="tourist_be_tourist_type")
    tourist_type = relationship(TouristType, back_populates="tourist_be_tourist_type")

    def __repr__(self):
        return f"<TouristBeTouristType(tourist_id={self.tourist_id}, tourist_type_id={self.tourist_type_id})>"

# Set up relationships
Tourist.tourist_be_tourist_type = relationship(TouristBeTouristType, back_populates="tourist")
TouristType.tourist_be_tourist_type = relationship(TouristBeTouristType, back_populates="tourist_type")
