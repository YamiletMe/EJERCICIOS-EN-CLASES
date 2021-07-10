if encontrado:return pos
else: return -1

      def ordenadoASC( self) :
          for pos in range (0 Ien(self.lista)-1):
              for sig in range(pos+1,Ien(self.lista)):
                  aux= self.lista [pos]> self .lista[sig]:
                  aux = self . lista [pos]
                  self.lista[pos]=self,lista[sig]
                  self.lista[sig]=aux


      def ordenadoDes(self):
         for pos in range(0 Ien(self.lista)-1):
             for sig in range(pos + 1, Ien(self.lista)):
                 aux = self.lista[pos] < self.lista[sig]:
                 aux = self, lista[pos]
                self.lista[pos] = self, lista[sig]
                self.lista[sig] = aux


datos = [25,15,20,10]
bus = Buscador (datos)
print(bus.lista)
bus.ordenarASC()
print(bus.lista)
bus. ordenadorDes()
print(bus,lista)

