from sqlalchemy import Column, Integer, String
from database import Base

class Veiculo(Base):
    __tablename__ = "veiculos"
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, index=True)
    marca = Column(String)
    ano = Column(Integer)
