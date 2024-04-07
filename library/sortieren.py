class sortieren:
    """Klasse zum Sortieren von Listen"""
    def __init__(self, a):
        self.a = a

    def bubble_sort(self):
        n = len(self.a)
        for i in range(n-1):
            for j in range(n-1):
                if self.a[j]>self.a[j+1]:
                    self.a[j+1],self.a[j] = self.a[j],self.a[j+1]
                    print(i,j,self.a)
        return self.a
    
    def selectionSort(self):
        n = len(self.a)
        for i in range(n):
            k = i
            for j in range(i+1, n):
                if self.a[j]<self.a[k]:
                    k=j
                    self.a[i],self.a[k] = self.a[k],self.a[i]
                    print(i,j,self.a)
        return self.a
