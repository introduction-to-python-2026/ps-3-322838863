def approximate_pi(n_terms: int)->float:
  pi_cal = 0.0
  for k in range(n_terms):
    pi_cal += ((-1) ** k) / (2 * k + 1)
  return 4 * pi_cal
  
def move(my_list, direction):

    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    elif direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
