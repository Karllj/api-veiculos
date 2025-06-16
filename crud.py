from sqlalchemy.orm import Session
from models import Veiculo

def get_veiculos(db: Session):
    return db.query(Veiculo).all()

def create_veiculo(db: Session, modelo: str, marca: str, ano: int):
    novo = Veiculo(modelo=modelo, marca=marca, ano=ano)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def delete_veiculo(db: Session, veiculo_id: int):
    veiculo = db.query(Veiculo).get(veiculo_id)
    if veiculo:
        db.delete(veiculo)
        db.commit()
