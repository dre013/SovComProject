import psycopg2
from psycopg2 import Error


con = psycopg2.connect(dbname="test_DB", user="postgres",
                       password="111", port="5433")
cur = con.cursor()

try:
    cur.execute(
        'SELECT "Name", "Inn", COUNT(*) AS count_obligation FROM "MonetaryObligation" mo JOIN "Debtor" de ON mo.owner_id = de.owner_id GROUP BY "Name", "Inn", de.owner_id ORDER BY count_obligation DESC limit 10')
    fill = cur.fetchall()
    print("Задание 2.a:\n")
    for i in fill:
        print(i)
    print("______________________________________\n")

    cur.execute(
        'SELECT "Name", "Inn", SUM("DebtSum") AS sum_debt_sum FROM "MonetaryObligation" mo JOIN "Debtor" de ON mo.owner_id = de.owner_id GROUP BY "Name", "Inn", de.owner_id ORDER BY sum_debt_sum DESC limit 10')
    fill = cur.fetchall()
    print("Задание 2.b:\n")
    for i in fill:
        print(i)
    print("______________________________________\n")

    cur.execute(
        'SELECT "Name", "Inn", "CreditorName", ROUND((SUM("TotalSum") - SUM("DebtSum")) / (SUM("TotalSum") + SUM("PenaltySum")) * 100, 2) AS Procent FROM "MonetaryObligation" mo JOIN "Debtor" de ON mo.owner_id = de.owner_id GROUP BY "Name", "Inn", "CreditorName", "TotalSum", "PenaltySum", "DebtSum", de.owner_id ORDER BY Procent ASC;')
    fill = cur.fetchall()
    print("Задание 2.c:\n")
    for i in fill:
        print(i)
    
except (Exception, Error) as e:
    print("Error", e)
finally:
    if con:
        cur.close()
        con.close()
        print("Done, data has been selected")
