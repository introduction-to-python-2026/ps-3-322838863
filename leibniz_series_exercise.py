def approximate_pi(n_terms: int):
  pi_cal: int = 0
  for k in range(n_terms):
    pi_cal +=(-1)**k / (2*k+1)
  return 4*pi_cal

