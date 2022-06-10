# 60/150
#Armin Darabi Mahboub

def main():
    string = input()
    only_numbers = filterToNumber(string)
    couples = makeCoupleNumbers(only_numbers)
    only_primes = givePrimes(couples)
    if only_primes:
        for i in only_primes:
            print(i)

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def givePrimes(couples):
    result = []
    for couple in couples:
        couple = int(couple)
        if is_prime(couple):
            result.append(couple)
    return result

def makeCoupleNumbers(nums):
    result = []
    for i in range(len(nums) - 1):
        result.append(f'{nums[i]}{nums[i + 1]}')
    return result

def filterToNumber(string):
    result = ''
    for s in string:
        if s.isdigit():
            result = result + s
    return result
    

if __name__ == '__main__':
    main()