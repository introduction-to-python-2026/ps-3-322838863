def approximate_pi(n_terms):
  pi_estimate = 0
  for k in range(n_terms):
    pi_estimate = ((-1) ** k) / (2 * k + 1)
  return 4 * pi_estimate
   
