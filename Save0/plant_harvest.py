def plant_harvest(plot, hay_plots, carrot_plots, wood_plots, pumpkin_plots, sunflower_plots):
	has_sunflower = False
	if can_harvest():
		if get_entity_type() != Entities.Sunflower:
			harvest()
		else:
			has_sunflower = True
	elif get_entity_type() != None:
		if get_water() < 0.5:
			use_item(Items.Water_Tank)
		quick_print("Water", get_water())
		return	
		
	if plot <= sunflower_plots:
		sunflower()
	elif plot <= hay_plots + sunflower_plots:
		hay()
	elif plot <= carrot_plots + hay_plots + sunflower_plots:
		carrots()
	elif plot <= carrot_plots + hay_plots + wood_plots + sunflower_plots:
		trees()
	elif plot <= carrot_plots + hay_plots + wood_plots + pumpkin_plots + sunflower_plots:
		pumpkin()
	else:
		quick_print("Unused")
	
	return has_sunflower		
		
def sunflower():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)	
		
def hay():
	if get_ground_type() != Grounds.Turf:
		till()
		
def carrots():
	if get_ground_type() != Grounds.Soil:
		till()

	plant(Entities.Carrots)

def trees():
	if get_ground_type() != Grounds.Turf:
		till()
	plant(Entities.Bush)
	
def pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)
	
