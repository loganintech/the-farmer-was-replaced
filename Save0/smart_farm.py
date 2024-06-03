def get_plot(target, target_total):
	total_plots = get_world_size() ** 2
	percent = target / target_total
	return max(1, (percent * total_plots) // 1)

def smart_farm(target_hay, target_carrots, target_wood, target_pumpkins):
	target_total = target_hay + target_carrots + target_wood + target_pumpkins
	hay_plots = get_plot(target_hay, target_total)
	carrot_plots = get_plot(target_carrots, target_total)
	wood_plots = get_plot(target_wood, target_total)
	pumpkin_plots = get_plot(target_pumpkins, target_total)
	sunflower_plots = get_sunflower_plots(get_world_size() ** 2)
	quick_print("Wanted Sunflower", sunflower_plots)
	
	quick_print("Wanted Hay Plots", hay_plots)
	quick_print("Wanted Carrots Plots", carrot_plots)
	quick_print("Wanted Wood Plots", wood_plots)
	quick_print("Wanted Pumpkin Plots", pumpkin_plots)
	
	reset_loc()
	buy_supplies(carrot_plots, pumpkin_plots, 10)
	

	prev_move = North
	square = 0
	has_sunflower = False
	while True:
		square+=1
		has_sunflower = plant_harvest(square, hay_plots, carrot_plots, wood_plots, pumpkin_plots - 1, sunflower_plots) or has_sunflower
		prev_move = smart_move(prev_move)
		if square % get_world_size()**2 == 0:
			reset_loc()
			break
	if has_sunflower:
		harvest_sunflower()	
	
	
def reset_loc():
	goto(0, 0)

def goto(x, y):
	while get_pos_x() < x:
		move(East)
	while get_pos_x() > x:
		move(West)
	while get_pos_y() > y:
		move(South)
	while get_pos_y() < y:
		move(North)	

def smart_move(prev_move):
	row = get_pos_y()
	col = get_pos_x()
	if row <= get_world_size() - 1:
		if prev_move == North and row == get_world_size() - 1:
			move(East)
			return East
		if prev_move == South and row == 0:
			move(East)
			return East
		
		if col % 2 == 0:
			move(North)
			return North
		else:
			move(South)
			return South
			