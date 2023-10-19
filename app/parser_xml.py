from natasha import AddressExtractor


import schemas


message = schemas.EJBMessage_schema
debtor = schemas.Debtor_schema
bank = schemas.Bank_schema
monet = schemas.MonetaryObligation_schema
payment = schemas.ObligatoryPayment_schema
publisher =schemas.Publisher


def ExtrajudicialBankruptcyMessage(tag):
    c = []
    d = debtor

    message.id = tag.find("Id").text
    message.Number = tag.find("Number").text
    message.Type = tag.find("Type").text
    message.PublishDate = tag.find("PublishDate").text
    try:
        message.FinishReason = tag.find("FinishReason").text
    except:
        message.FinishReason = ''

    d.Name = tag.find("Debtor/Name").text
    d.BirthDate = tag.find("Debtor/BirthDate").text
    d.BirthPlace = tag.find("Debtor/BirthPlace").text
    try:
        d.Inn = tag.find("Debtor/Inn").text
    except:
        d.Inn = ''
    d.owner_id = message.id

    publisher.Name = tag.find("Publisher/Name").text
    publisher.Inn = tag.find("Publisher/Inn").text
    publisher.Ogrn = tag.find("Publisher/Ogrn").text
    publisher.owner_id = message.id

    t = tag.find("Debtor/Address").text.strip().splitlines()
    extractor = AddressExtractor()
    for address in t:
        matches = extractor(address)
        for match in matches:
            lst = match.fact.parts            
    try:
        d.Region = ''
        d.City = ''
        d.Index = ''
        d.Street = ''
        d.Home = ''
        d.Apartment = ''
        for i in lst:
            try:
                if i.value:
                    index = i.value
                    d.Index = index
            except:
                pass
            try:
                if i.type == "область" or i.type == "республика" or i.type == "край" or i.type == None:
                    region = i.name + " " + i.type
                    d.Region = region
                if i.type == "район":
                    region += ", " + i.name + " " + i.type
                    d.Region = region
                if i.type == "город" or i.type == "село" or i.type == "посёлок":
                    city = i.type + " " + i.name
                    d.City = city
                if i.type == "улица" or i.type == "проспект" or i.type == "переулок":
                    street = i.name + " " + i.type
                    d.Street = street
                if i.type == "дом":
                    home = i.number
                    d.Home = home
                if i.type == "квартира":
                    apart = i.number
                    d.Apartment = apart
            except:
                pass
    except:
        d.Region = 'NatashaError'
        d.City = 'NatashaError'
        d.Street = 'NatashaError'
        d.Home = 'NatashaError'
        d.Apartment = 'NatashaError'


    m = message
    p = publisher
    c.append(m)
    c.append(d)
    c.append(p)

    return c


def banks(tg):
    c = []
    bank.Name = tg.find("Name").text
    bank.owner_id = message.id
    try:
        bank.Bik = tg.find("Bik").text
    except:
        bank.Bik = ''
    b = bank
    c.append(b)
    return c


def monet_obl(tg):
    c = []
    monet.CreditorName = tg.find("CreditorName").text
    monet.Content = tg.find("Content").text
    monet.Basis = tg.find("Basis").text
    monet.TotalSum = tg.find("TotalSum").text
    try:
        monet.DebtSum = tg.find("DebtSum").text
    except:
        monet.DebtSum = 0.0
    try:
        monet.PenaltySum = tg.find("PenaltySum").text
    except:
        monet.PenaltySum = 0.0
    monet.owner_id = message.id
    mo = monet
    c.append(mo)
    return c

def obl_payment(tg):
    c = []
    payment.Name = tg.find("Name").text
    payment.Sum = tg.find("Sum").text
    try:
        payment.PenaltySum = tg.find("PenaltySum").text
    except:
        payment.PenaltySum = 0.0
    payment.owner_id = message.id
    pa = payment
    c.append(pa)
    return c