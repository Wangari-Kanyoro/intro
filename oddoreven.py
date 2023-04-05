def main():
    x=int(input("what is the value of x"))
    if mod(x): 
      print("Even")
    else:
      print("Odd")
          


def mod(n):
   if n % 2==0: 
    return True
   else:
    return False
   


   def  mod(n):
     return n % 2 == 0
   
   main()