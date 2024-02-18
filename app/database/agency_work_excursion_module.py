from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from agency_module import Agency
from excursion_module import Excursion

Base = declarative_base()

class AgencyWorkExcursion(Base):
    __tablename__ = 'agency_work_excursion'

    agency_id = Column(Integer, ForeignKey('agency.agency_id'), primary_key=True)
    excursion_id = Column(Integer, ForeignKey('excursion.excursion_id'), primary_key=True)

    # Define foreign key relationships
    agency = relationship(Agency, back_populates='agency_work_excursions')
    excursion = relationship(Excursion, back_populates='agency_work_excursions')

    def __repr__(self):
        return f"<AgencyWorkExcursion(agency_id={self.agency_id}, excursion_id={self.excursion_id})>"
