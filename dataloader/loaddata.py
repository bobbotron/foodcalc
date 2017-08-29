# Load food data into postgres

import csv
import psycopg2

conn = psycopg2.connect("dbname=fooddb user=foodcalcuser host=db password=0p9o8i7U")

def addToDbGeneric(row, insertMethod, name):
    cur = conn.cursor()
    try:
        insertMethod(row, cur)
        conn.commit()
        return True
    except psycopg2.IntegrityError as inst:
        print('Could not add %s %s, %s' % (name, row[0], row[1]) )
        cur.close()
        conn.rollback()
        return False

def addFood(row):
    def addFoodToDb(row, cur):
        cur = conn.cursor()
        # print('adding row %s, %s' % (row[0], row[1]))
        cur.execute(
        """INSERT INTO food_name (id, food_code, food_group_id, food_source_id, description )
        VALUES (%s, %s, %s, %s, %s);""",
        [int(row[0]), int(row[1]), int(row[2]), int(row[3]), row[4]])
    return addToDbGeneric(row, addFoodToDb, "Food Name")

def addNutrient(row):
    def addNutrientToDb(row, cur):
        cur.execute(
        """INSERT INTO nutrient_name (id, nutrient_code, symbol, nutrient_unit, name, nutrient_decimals )
        VALUES (%s, %s, %s, %s, %s, %s);""",
        [int(row[0]), row[1], row[2], row[3], row[4], int(row[7])])
    return addToDbGeneric(row, addNutrientToDb, "Nutrient Name")

def addNutrientAmount(row):
    def addNA(row, cur):
        cur.execute(
        """INSERT INTO nutrient_amount (food_id, nutrient_id, nutrient_value )
        VALUES (%s, %s, %s);""",
        [int(row[0]), int(row[1]), float(row[2])])
    return addToDbGeneric(row, addNutrientAmount, "Nutrient Amount")

def addMeasureName(row):
    cur = conn.cursor()
    cur.execute(
    """INSERT INTO measure_name (id, measure_name )
    VALUES (%s, %s);""",
    [int(row[0]), row[1]])
    conn.commit()

def addConversionFactor(row):
    def addCF(row, cur):
        cur.execute(
        """INSERT INTO conversion_factor (food_id, measure_id, conversion_factor)
        VALUES (%s, %s, %s);""",
        [int(row[0]), int(row[1]), float(row[2])])
    return addToDbGeneric(row, addCF, "Conversion Factor")

def loadData(filename, addFunction):
    firstRow = True
    with open(filename, encoding="cp1252") as csvfile:
        csvReader = csv.reader(csvfile)
        rowCount = 0
        successCount = 0
        for row in csvReader:
            if firstRow:
                # skip the first row
                firstRow = False
            else:
                if addFunction(row):
                    successCount = successCount + 1
                rowCount = rowCount + 1
        print("Added %s of %s rows from %s" % (successCount, rowCount, filename));

def main():
    loadData('/fooddata/NUTRIENT NAME.csv', addNutrient)
    loadData('/fooddata/FOOD NAME.csv', addFood)
    loadData('/fooddata/NUTRIENT AMOUNT.csv', addNutrientAmount)
    loadData('/fooddata/MEASURE NAME.csv', addMeasureName)
    loadData('/fooddata/CONVERSION FACTOR.csv', addConversionFactor)

main()

conn.close()
