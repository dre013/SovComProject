from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, Sequence


from database import Base

class ExtrajudicialBankruptcyMessage(Base):
    __tablename__ = "ExtrajudicialBankruptcyMessage"

    Id = Column(String, primary_key=True, index=True)
    Number = Column(String)
    Type = Column(String)
    PublishDate = Column(String)
    FinishReason = Column(String)

class Publisher(Base):
    __tablename__ = "Publisher"

    id = Column(Integer, Sequence("Publisher_id"), primary_key=True, index=True)
    Name = Column(String)
    Inn = Column(String)
    Ogrn = Column(String)
    owner_id = Column(String)

class Debtor(Base):
    __tablename__ = "Debtor"

    id = Column(Integer, Sequence("Debtor_id"), primary_key=True, index=True)
    Name = Column(String)
    BirthDate = Column(String)
    BirthPlace = Column(String)
    Index = Column(String)
    Region = Column(String)
    City = Column(String)
    Street = Column(String)
    Home = Column(String)
    Apartment = Column(String)
    Inn = Column(String)
    owner_id = Column(String)


class Bank(Base):
    __tablename__ = "Bank"

    id = Column(Integer, Sequence("Bank_id"), primary_key=True, index=True)
    Name = Column(String)
    Bik = Column(String)
    owner_id = Column(String)


class MonetaryObligation(Base):
    __tablename__ = "MonetaryObligation"

    id = Column(Integer, Sequence("MonetaryObligation_id"), primary_key=True, index=True)
    CreditorName = Column(String)
    Content = Column(String)
    Basis = Column(String)
    TotalSum = Column(Numeric)
    DebtSum = Column(Numeric)
    PenaltySum = Column(Numeric)
    owner_id = Column(String)


class ObligatoryPayment(Base):
    __tablename__ = "ObligatoryPayment"

    id = Column(Integer, Sequence("ObligatoryPayment_id"), primary_key=True, index=True)
    Name = Column(String)
    Sum = Column(Numeric)
    PenaltySum = Column(Numeric)
    owner_id = Column(String)
