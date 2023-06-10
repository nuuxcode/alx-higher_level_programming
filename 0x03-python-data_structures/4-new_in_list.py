#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	if idx < 0 or idx >= len(my_list):
		return my_list
	new_list = []
	for i in range(len(my_list)):
		new_list.append(my_list[i])
		if i == idx:
			new_list[i] = element
	return new_list
