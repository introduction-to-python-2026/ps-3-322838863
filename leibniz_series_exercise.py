def approximate_pi(n_terms):
  pi_cal = 0
  for k in range(n_terms):
    pi_cal +=(-1)**k / (2*k+1)
  return 4*pi_cal
print (approximate_pi(10))
print (approximate_pi(100))
print (approximate_pi(1000))
