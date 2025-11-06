import random
num_points = 100000
in_or_out = []
for i in range(num_points):
  in_or_out.append((((random.random()-0.5)**2) + (random.random()-0.5)**2)**0.5 <= 0.5)
  tozaa = sum(in_or_out)/num_points*4
print(tozaa)
