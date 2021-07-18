   class logica:
      def _init_(selfself, datos):
          self.lista=datos

      def par (self,numero):
          rec = numero % 2
          return rec

      def sumapares(selfself):
          acu=0
          for num in lista:
              if self.par(num)== 0:
                  acu = acu+num

          return acu
      def perfecto(selfself,numero):
          acu=0
          for divisor in range(1,numero):
              rec = numero%divisor
              if rec ==0:
                  acu=acu+divisor

      def divisoresNumero(self,numero):
          divisores = []
          for divisor in range(1,numero):
              rec = numero%divisor
              if rec ==0:
                  divisores.append(divisor)
                  return divisores


      class ejercicios(logica):
          def_init_(self,numero,valor):
          super()._init_(numero)
              pass

      ejer= ejercicioc([2,3,4],20)
      print(ejer.par(4))
e