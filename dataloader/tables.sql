

-- NutrientID,NutrientCode,NutrientSymbol,NutrientUnit,NutrientName,NutrientNameF,Tagname,NutrientDecimals
-- 203,203,PROT,g,PROTEIN,PROT�INES,PROCNT,2

CREATE TABLE nutrient_name
(
    id integer PRIMARY KEY NOT NULL,
    nutrient_code text NOT NULL,
    symbol text NOT NULL,
    nutrient_unit text NOT NULL,
    name text NOT NULL,
    nutrient_decimals integer NOT NULL
);

-- FoodID,FoodCode,FoodGroupID,FoodSourceID,FoodDescription,FoodDescriptionF,FoodDateOfEntry,FoodDateOfPublication,CountryCode,ScientificName
-- 501681,6463,11,0,"Mustard spinach (tendergreen), boiled, drained, with salt","Moutarde jonc�e, bouillie, �goutt�e, sel ajout�",2009-03-17,,11801,

CREATE TABLE food_name
(
  id integer PRIMARY KEY NOT NULL,
  food_code integer NOT NULL,
  food_group_id integer NOT NULL,
  food_source_id integer NOT NULL,
  description text NOT NULL --,
  -- date_of_entry text
);


-- FoodID,NutrientID,NutrientValue,StandardError,NumberofObservations,NutrientSourceID,NutrientDateOfEntry
-- 2,203,9.54,0,0,102,2010-04-16
CREATE TABLE nutrient_amount
(
  food_id integer NOT NULL REFERENCES food_name(id),
  nutrient_id integer NOT NULL REFERENCES nutrient_name(id),
  nutrient_value decimal NOT NULL
  -- source_id?
);

CREATE TABLE measure_name
(
  id integer PRIMARY KEY NOT NULL,
  measure_name text NOT NULL
);

CREATE TABLE conversion_factor
(
  food_id integer NOT NULL REFERENCES food_name(id),
  measure_id integer NOT NULL REFERENCES measure_name(id),
  conversion_factor decimal NOT NULL
);
