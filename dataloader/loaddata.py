# Load food data into postgres

import csv
import psycopg2

conn = psycopg2.connect("dbname=fooddb user=foodcalcuser host=db password=0p9o8i7U")

def addFood(row):
    cur = conn.cursor()
    print('adding row %s, %s' % (row[0], row[1]))
    cur.execute(
    """INSERT INTO food_name (id, food_code, food_group_id, food_source_id, description )
    VALUES (%s, %s, %s, %s, %s);""",
    [int(row[0]), int(row[1]), int(row[2]), int(row[3]), row[4]])
    conn.commit()

firstRow = True

with open('/fooddata/FOOD NAME.csv', encoding="cp1252") as csvfile:
    foodNameCsv = csv.reader(csvfile)
    for row in foodNameCsv:
        if firstRow:
            # skip the first row
            firstRow = False
        else:
            addFood(row)


conn.close()
