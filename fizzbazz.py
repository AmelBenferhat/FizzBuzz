def fizzbazz(n: int) -> str:
  if n % 3 == 0 and n % 5 == 0:
      return "fizzbazz"
  if n % 3 == 0:
      return "fizz"
  if n % 5 == 0:
      return "bazz"
  return str(n)
