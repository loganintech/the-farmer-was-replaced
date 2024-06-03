def auto_farm():
	while True:
		while get_pos_x() > 0:
			move(West)
		while get_pos_y() > 0:
			move(South)
	
		for x in range(get_world_size()):
			for i in range(get_world_size()):
				if can_harvest():
					if get_entity_type() == Entities.Carrots:
						harvest()
						plant(Entities.Carrots)
					else:    
						harvest()
						if get_pos_y() % get_world_size() != 2:    
							till()
							plant(Entities.Carrots)
				else:
					if get_pos_y() % get_world_size() != 2:    
						plant(Entities.Carrots)
			
				if i < get_world_size() - 1:
					if get_pos_x() % 2 == 1:
						move(South)
					else:
						move(North)
	            
			move(East)
	            
		if num_items(Items.Carrot_Seed) < 10:
			for i in range(10 - num_items(Items.Carrot_Seed)):
				trade(Items.Carrot_Seed)