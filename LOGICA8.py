   class logica:
       def_init_(self):
       pass

   def perfecto(self, numero):
       rec = numero % 2
      return rec


   def perfecto(self, numero):
       acu=0
       for divisor in range(1,numero):
           rec = numero%divisor
           if rec == 0:
               acu=acu+divisor
           return acu
   ejer = logica ()
   if ejer.perfecto(5)== 5:
       print("perfecto")
        
e