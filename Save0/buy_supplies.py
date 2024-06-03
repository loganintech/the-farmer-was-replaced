def buy_supplies(carrot_plots, pumpkin_plots, tank_goal):
	if num_items(Items.Carrot_Seed) < carrot_plots:
		trade(Items.Carrot_Seed, min(carrot_plots - num_items(Items.Carrot_Seed), num_items(Items.Wood)))

	if num_items(Items.Sunflower_Seed) < carrot_plots:
		trade(Items.Sunflower_Seed, min(carrot_plots - num_items(Items.Sunflower_Seed), num_items(Items.Carrot)))

	if num_items(Items.Pumpkin_Seed) < pumpkin_plots:
		trade(Items.Pumpkin_Seed, min(pumpkin_plots - num_items(Items.Pumpkin_Seed), num_items(Items.Carrot)))

	total_tanks = num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)
	if total_tanks < tank_goal or num_items(Items.Water_Tank) == 0:
		trade(Items.Empty_Tank, max(tank_goal - total_tanks, 1))
		
	if num_items(Items.Fertilizer) < 2:
		trade(Items.Fertilizer, 2)
	