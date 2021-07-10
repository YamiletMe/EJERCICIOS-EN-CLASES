if encontrado:return pos
else: return -1

      def ordenadoASC( self) :
          for pos in range (0 Ien(self.lista)-1):
              for sig in range(pos+1,Ien(self.lista)):
                  aux= self.lista [pos]
                  self.lista[pos]=self,lista[sig]
                  self.lista[sig]=aux
      def primer(self)
          return self.lista[0]

      def primerElemento(self):
          primero=self.lista[0]
          auxlista=[]
          for pos in range(1,len(self.lista)):
              auxlista.append(self.lista[pos])
          self.lista = self.lista[1:]
          return primero


      def ultimo (self):
          retur self.lista[-1]


      def ultimoelEliminado(self):
          ultimp=self.lista[-1]
          self.lista = self . lista[:-1]
          return ultimo


      def ultimoelEliminado(self):
          ultimp = self.lista[-1]
          self.lista = self.lista[:-1]
          return ultimo


datos = [25,15,20,10]
#datos .sort()
print(datos)
bus = Buscador(datos)
print(bus , primerEliminado() , bus,lista)
bus = Buscador (datos)
print(bus.lista)
bus.ordenarASC()
print(bus.lista)


