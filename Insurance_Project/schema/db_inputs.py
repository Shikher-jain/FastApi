from sqlalchemy import Column, Integer, Float, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from typing import Literal

Base = declarative_base()

class InsuranceData(Base):
    __tablename__ = 'insurance_data'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    age: int = Column(Integer, nullable=False)
    weight: float = Column(Float, nullable=False)
    height: float = Column(Float, nullable=False)
    income_lpa: float = Column(Float, nullable=False)
    smoker: bool = Column(Boolean, nullable=False)  
    city: str = Column(String, nullable=False)
    occupation: Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'] = Column(String, nullable=False)
 