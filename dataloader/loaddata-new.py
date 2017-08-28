# Load food data into postgres

import csv
import psycopg2

conn = psycopg2.connect("dbname=fooddb user=foodcalcuser host=db password=0p9o8i7U")

def addFood(row):
    cur = conn.cursor()
    # print('adding row %s, %s' % (row[0], row[1]))
    cur.execute(
    """INSERT INTO food_name (id, food_code, food_group_id, food_source_id, description )
    VALUES (%s, %s, %s, %s, %s);""",
    [int(row[0]), int(row[1]), int(row[2]), int(row[3]), row[4]])
    conn.commit()

def addNutrient(row):
    cur = conn.cursor()
    print('adding nutrient %s, %s' % (row[0], row[1]))
    cur.execute(
    """INSERT INTO nutrient_name (id, nutrient_code, symbol, nutrient_unit, name, nutrient_decimals )
    VALUES (%s, %s, %s, %s, %s, %s);""",
    [int(row[0]), row[1], row[2], row[3], row[4], int(row[7])])
    conn.commit()

def addNutrientAmount(row):
    cur = conn.cursor()
    cur.execute(
    """INSERT INTO nutrient_amount (food_id, nutrient_id, nutrient_value )
    VALUES (%s, %s, %s);""",
    [int(row[0]), int(row[1]), float(row[2])])
    conn.commit()

def addMeasureName(row):
    cur = conn.cursor()
    cur.execute(
    """INSERT INTO measure_name (id, measure_name )
    VALUES (%s, %s);""",
    [int(row[0]), row[1]])
    conn.commit()

def addConversionFactor(row):
    cur = conn.cursor()
    cur.execute(
    """INSERT INTO conversion_factor (food_id, measure_id, conversion_factor)
    VALUES (%s, %s, %s);""",
    [int(row[0]), row[1], float(row[2])])
    conn.commit()

def loadData(filename, addFunction):
    firstRow = True
    with open(filename, encoding="cp1252") as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            if firstRow:
                # skip the first row
                firstRow = False
            else:
                addFunction(row)

def main():
    loadData('/fooddata/NUTRIENT NAME.csv', addNutrient)
    loadData('/fooddata/FOOD NAME.csv', addFood)
    loadData('/fooddata/NUTRIENT AMOUNT.csv', addNutrientAmount)
    loadData('/fooddata/MEASURE NAME.csv', addMeasureName)
    loadData('/fooddata/CONVERSION FACTOR.csv', addConversionFactor)

main()

conn.close()
