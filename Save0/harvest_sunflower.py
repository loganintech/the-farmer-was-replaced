def get_sunflower_plots(want_power):
	have_power = num_items(Items.Power)
	plots = 0
	while have_power < want_power:
		plots += 1
		have_power += (plots ** 0.5) # SQRT 
	return plots
	 
def harvest_sunflower():
	found_sunflowers = []

	square = 0
	reset_loc()
	prev_move = North
	while True:
		square += 1
		if get_entity_type() != Entities.Sunflower:
			break

		size = measure()
		new_sunflower = [get_pos_x(), get_pos_y(), size]
		found_sunflowers.append(new_sunflower)

		if square % get_world_size() ** 2 == 0:
			break

		prev_move = smart_move(prev_move)

	for sunflower in sort_sunflowers(found_sunflowers):
		goto(sunflower[0], sunflower[1])
		harvest()

def sort_sunflowers(found_sunflowers):
	sorted_sunflowers = []
	for x in range(len(found_sunflowers)):
		max = 0
		for i in range(len(found_sunflowers)):
			flower = found_sunflowers[i]
			if flower[2] > max:
				max = flower[2]
				max_index = i
		sorted_sunflowers.append(found_sunflowers.pop(max_index))

	return sorted_sunflowers