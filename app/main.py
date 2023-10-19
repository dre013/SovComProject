import xml.etree.ElementTree as ET

from database import SessionLocal, engine
import models, schemas, parser_xml

models.Base.metadata.create_all(bind=engine)


tree = ET.parse("ExtrajudicialBankruptcy_20230808_2.xml")
db = SessionLocal()


def post_message(db, message: schemas.EJBMessage_schema):
    db_message = models.ExtrajudicialBankruptcyMessage(Id=message.id, Number=message.Number, Type=message.Type, PublishDate=message.PublishDate,
                                                       FinishReason=message.FinishReason)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    db.close()
    return 


def post_debtor(db, debtor: schemas.Debtor_schema):
    db_debtor = models.Debtor(Name=debtor.Name, BirthDate=debtor.BirthDate, BirthPlace=debtor.BirthPlace, Index=debtor.Index, Region=debtor.Region, City=debtor.City,
                              Home=debtor.Home, Apartment=debtor.Apartment, Inn=debtor.Inn, owner_id=debtor.owner_id)
    db.add(db_debtor)
    db.commit()
    db.refresh(db_debtor)
    db.close()
    return


def post_publisher(db, publisher: schemas.Publisher):
    db_publisher = models.Publisher(Name=publisher.Name, Inn=publisher.Inn, Ogrn=publisher.Ogrn, owner_id=publisher.owner_id)
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    db.close()
    return


def post_banks(db, bank: schemas.Bank_schema):
    db_bank = models.Bank(Name=bank.Name, Bik=bank.Bik, owner_id=bank.owner_id)
    db.add(db_bank)
    db.commit()
    db.refresh(db_bank)
    db.close()
    return


def post_monet(db, monet: schemas.MonetaryObligation_schema):
    db_monet = models.MonetaryObligation(CreditorName=monet.CreditorName, Content=monet.Content, Basis=monet.Basis, TotalSum=monet.TotalSum, DebtSum=monet.DebtSum,
                                         PenaltySum=monet.PenaltySum, owner_id=monet.owner_id)
    db.add(db_monet)
    db.commit()
    db.refresh(db_monet)
    db.close()
    return


def post_obligation(db, obligation: schemas.ObligatoryPayment_schema):
    db_obligation = models.ObligatoryPayment(Name=obligation.Name, Sum=obligation.Sum, PenaltySum=obligation.PenaltySum, owner_id=obligation.owner_id)
    db.add(db_obligation)
    db.commit()
    db.refresh(db_obligation)
    db.close()
    return


def exe(xml_f, db):
    print("Processing...")
    for tag in xml_f.findall("ExtrajudicialBankruptcyMessage"):
        db_data = parser_xml.ExtrajudicialBankruptcyMessage(tag)
        for i in range(0, len(db_data)):
            if db_data[i] == schemas.EJBMessage_schema:
                post_message(db, message=db_data[i])
            elif db_data[i] == schemas.Debtor_schema:
                post_debtor(db, debtor=db_data[i])
            elif db_data[i] == schemas.Publisher:
                post_publisher(db, publisher=db_data[i])

        for bank in tag.findall("Banks/Bank"):
            db_banks = parser_xml.banks(bank)
            for j in range(0, len(db_banks)):
                post_banks(db, bank=db_banks[j])

        for mon in tag.findall("CreditorsNonFromEntrepreneurship/MonetaryObligations/MonetaryObligation"):
            db_monet_obl = parser_xml.monet_obl(mon)
            for k in range(0, len(db_monet_obl)):
                post_monet(db, monet=db_monet_obl[k])

        for mon in tag.findall("CreditorsFromEntrepreneurship/MonetaryObligations/MonetaryObligation"):
            db_monet_obl = parser_xml.monet_obl(mon)
            for m in range(0, len(db_monet_obl)):
                post_monet(db, monet=db_monet_obl[m])

        for obl in tag.findall("CreditorsNonFromEntrepreneurship/ObligatoryPayments/ObligatoryPayment"):
            db_obl_pay = parser_xml.obl_payment(obl)
            for o in range(0, len(db_obl_pay)):
                post_obligation(db, obligation=db_obl_pay[o])

        for obl in tag.findall("CreditorsFromEntrepreneurship/ObligatoryPayments/ObligatoryPayment"):
            db_obl_pay = parser_xml.obl_payment(obl)
            for ob in range(0, len(db_obl_pay)):
                post_obligation(db, obligation=db_obl_pay[ob])
    print("Done")
    return {"Good job": "success"}

if __name__ == "__main__":
    exe(tree, db)




