import numpy as np

def fpb(a,b):
  return np.gcd(a,b)

def kpk(a,b):
  return np.lcm(a,b)


if __name__ == "__main__":
  a = int(input("masukkan inputan integer pertama : "))
  b = int(input("masukkan inputan integer kedua : "))

  print(f"fpb dari {a} dan {b} adalah : {fpb(a,b)}")
  print(f"kpk dari {a} dan {b} adalah : {kpk(a,b)}")
