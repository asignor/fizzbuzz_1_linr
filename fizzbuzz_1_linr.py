  print([(n%3 == 0)*'fizz' + (n%5 == 0)*'buzz' + str(n)*((n%3)*(n%5) != 0) for n in range(100)]) 
