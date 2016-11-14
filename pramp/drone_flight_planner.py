def min_fuel(route):
  start_height = route[0]['z']
  max_height = max(route, key=lambda coord:coord['z'])['z']
  
  return max_height - start_height


if __name__ == '__main__':
	print(min_fuel( [{'x':0, 'y':2, 'z':10}, 
		{'x':3, 'y':5, 'z':0}, {'x':9, 'y':20, 'z':6}, 
		{'x':10, 'y':12, 'z':15}, {'x':10, 'y':10, 'z':8}] ))
