def approximate_pi(n_terms):
  pi_calculate = 0
  for k in range(n_terms):
    pi_calculate +=(-1)**k / (2*k+1)
  return 4*pi_calculate
print (approximate_pi(1000))
