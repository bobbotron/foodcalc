
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
