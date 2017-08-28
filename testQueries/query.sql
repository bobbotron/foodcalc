-- Food analysis for one food item

select fn.description, na.nutrient_value, n.*
from food_name fn
INNER JOIN nutrient_amount na ON fn.id = na.food_id
INNER JOIN nutrient_name n ON na.nutrient_id = n.id
WHERE fn.id = 5
