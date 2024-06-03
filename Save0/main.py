# smart_farm_entry()
hay_target = 20
carrot_target = 2000
wood_target = 1
pumpkin_target = 3000


while True:
	if num_items(Items.Pumpkin) > 100:
		full_harvest()
		do_maze()
	
	goto(0, 0)
	wanted_hay = max(hay_target - num_items(Items.Hay), 0)
	wanted_carrot = max(carrot_target - num_items(Items.Carrot), 0)
	wanted_wood = max(wood_target - num_items(Items.Wood), 0)
	wanted_pumpkin = max(pumpkin_target - num_items(Items.Pumpkin), 0)
	wanted_total = wanted_hay + wanted_carrot + wanted_wood + wanted_pumpkin
	if wanted_total == 0:
		wanted_hay = 100
		wanted_carrot = 100
		wanted_wood = 100
		wanted_pumpkin = 100

	quick_print("Wanted Hay", wanted_hay)
	quick_print("Wanted Carrots", wanted_carrot)
	quick_print("Wanted Wood", wanted_wood)
	quick_print("Wanted Pumpkin", wanted_pumpkin)
	if wanted_carrot < wanted_pumpkin / 4:
		wanted_carrot = wanted_pumpkin / 4
		if num_items(Items.Carrot) < 100:
			wanted_carrot = wanted_pumpkin / 2
			
	if wanted_wood < wanted_carrot / 3:
		wanted_wood = wanted_carrot / 3

	if num_items(Items.Wood) < 100:
		wanted_wood *= 100

	smart_farm(wanted_hay, wanted_carrot, wanted_wood, wanted_pumpkin)