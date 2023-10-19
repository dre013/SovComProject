from pydantic import BaseModel
from typing import Optional
from decimal import Decimal


class EJBMessage_schema(BaseModel):
    id: str
    Number: str
    Type: str
    PublishDate: str
    FinishReason: str

    class Config:
        orm_mode = True

class Publisher(EJBMessage_schema):
    Name: str
    Inn: str
    Ogrn: str
    owner_id: str

class Debtor_schema(EJBMessage_schema):
    Name: str
    BirthDate: str
    BirthPlace: str
    Index: Optional[str]
    Region: Optional[str]
    City: Optional[str]
    Street: Optional[str]
    Home: Optional[str]
    Apartment: Optional[str]
    Inn: str
    owner_id: str
    
    

class Bank_schema(EJBMessage_schema):
    Name: Optional[str]
    Bik: Optional[str]
    owner_id: Optional[str]

class MonetaryObligation_schema(EJBMessage_schema):
    CreditorName: Optional[str]
    Content: Optional[str]
    Basis: Optional[str]
    TotalSum: Optional[Decimal]
    DebtSum: Optional[Decimal]
    PenaltySum: Optional[Decimal]
    owner_id: Optional[str]

class ObligatoryPayment_schema(EJBMessage_schema):
    Name: Optional[str]
    Sum: Optional[Decimal]
    PenaltySum: Optional[Decimal]
    owner_id: Optional[str]
