from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from tourist_type_module import TouristType

Base = declarative_base()

class TouristType(Base):
    __tablename__ = 'tourist_type'

    tourist_type_id = Column(Integer, primary_key=True, nullable=False)
    tourist_type_name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<TouristType(tourist_type_id={self.tourist_type_id}, tourist_type_name={self.tourist_type_name})>"
    
    # Set up relationships
    tourist = relationship("Tourist", back_populates="tourist_type")
    tourist_be_tourist_type = relationship("TouristBeTouristType", back_populates="tourist_type")
    