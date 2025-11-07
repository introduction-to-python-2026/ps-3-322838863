def approximate_pi(n_terms) -> float:
  pi_estimate = 0.0
  for k in range(n_terms):
    term = ((-1) ** k) / (2 * k + 1)
    pi_estimate += term
  return 4 * pi_estimate
   
