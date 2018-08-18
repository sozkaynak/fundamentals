from __future__ import print_function


class Node(object):
   
    def __init__(self, data):
        
        self.left = None
        self.right = None
        self.data = data

     #insert methodu, yeni düğüm ekledikçe özyinelemeli(recursively) olarak çağırılır.   
    def insert(self, data):
        
        if self.data:
            if data < self.data: #eklenecek veri,düğümdeki veriden küçükse:
                if self.left is None:  #düğümdeki verinin solunda düğüm yoksa:
                    self.left = Node(data)#soluna ekle.
                else:#düğümdeki verinin solunda veri varsa:
                    self.left.insert(data)#insert methodunu düğümdeki verinin solundaki veri için tekrarla.
            elif data > self.data: #eklenecek veri,düğümdeki veriden büyükse:
                if self.right is None:#düğümdeki verinin sağında düğüm yoksa:
                    self.right = Node(data)#sağına ekle
                else:#düğümdeki verinin sağında veri varsa:
                    self.right.insert(data)#insert methodunu düğümdeki verinin sağındaki veri için tekrarla.
        else: #en son ihtimal olarak, düğümdeki veri aranan veriye eşitse:
            self.data = data#düğümde değişim olmaz.


    #Ağaçtaki belirli bir düğümü aramak için lookup() methodunu kullanıcaz. özyinelemeli(recursively) olarak çağırılır.  
    #Bir düğümün verilerini argüman olarak alan ve bulduğunda döndüren yada yok ise None olarak döndürüren bir arama yöntemi ekleriz.
    #Ayrıca kolaylık sağlamak için ebeveyninide iade ediyoruz.
    def lookup(self, data, parent=None):
    
        if data < self.data:#aranan veri,düğümdeki veriden küçükse:
            if self.left is None:# solunda bir düğüm yoksa:
                return None, None #boş olarak döndür.
            return self.left.lookup(data, self)#solundaki düğümden arama methoduyla devam et.
        elif data > self.data: #aranan veri, düğümdeki veriden büyükse:
            if self.right is None:#sağında bir veri yoksa:
                return None, None  #boş olarak döndür.
            return self.right.lookup(data, self) #sağındaki düğümden arama methoduyla aramaya devam et.
        else: #en son ihtimal olarak, düğümdeki veri aranan veriye eşitse:
            return self, parent  #veriyi ve ebeveynini döndür.

    def delete(self, data):
       
        node, parent = self.lookup(data) # silinecek düğüm hakkındaki bilgileri getir.
        if node is not None: #düğüm varsa:
            children_count = node.children_count() # düğümün çocuk sayısını bul.
            #bu durumda 3 olasılık vardır
            # hiç çocuğu yoksa,
            #1 tane çocuğu varsa,
            #ya da 2 çocuğu varsa.
            if children_count == 0:  #Eğer hiç çocuğu yoksa:
               
                if parent: #ailesi varsa:
                    if parent.left is node: # ebeveyninin solundaki düğüm ise
                        parent.left = None  #değeri none yap.(kaldır)
                    else: #ebeveynin sağındaki düğüm ise:
                        parent.right = None #değeri none  yap. (kaldır)
                else:  #ailesi yoksa, kök düğümse:
                    self.data = None # kök düğüm değerini o yap.
            elif children_count == 1:  
                # eğer 1 tane çocuğu varsa
                # çocuğu ile değiştir.
                if node.left: #düğümün solunda çocuk varsa:
                    n = node.left#n, solundaki çocuğun verisi.
                else: #düğümün sağında çocucuk varsa:
                    n = node.right #n, sağındaki çocuğun verisi.
                if parent:#düğümün ebeveyni varsa:
                    if parent.left is node: # düğüm, ebeveyninin soludaki düğümse:
                        parent.left = n # ebeveynin solundaki düğüme, n'i ata.
                    else: # düğüm, ebeveyninin sağındaki düğümse:
                        parent.right = n # ebeveynin sağındaki düğüme, n'i ata.
                else: #düğümün ebeveyni yoksa:
                    self.left = n.left #n'nin solundaki düğüm aynı kalıyor.
                    self.right = n.right #n'nin sağındaki düğüm aynı kalıyor.
                    self.data = n.data#n'nin verisi aynı kalıyor.
            else:
                # eğer 2 tane çocuğu varsa
                # varisi bulunuyor.
                parent = node # node=silinecek düğüm, parent olarak atanıyor.
                successor = node.right# silinecek düğümü sağındaki veri, varis seçiliyor.
                while successor.left:  #varisin solundaki her veri için(yaprağa ulaşana kadar):
                    parent = successor #varisi parent için ata.
                    successor = successor.left #varisin solundaki düğümüde, varis olarak ata.
                
                node.data = successor.data #silinecek düğümün verisini, varisin verisiyle değiştir.
                #silinecek düğümün yerine getirdiğimiz düğümün(successor) bir çocuğu olmadığı için, ebeveyninin solundaki düğümünün değerini yok olarak ayarladık.
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

   
    def print_tree(self):
        """Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

    
    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt# -*- coding: utf-8 -*-


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)    
root.print_tree()


