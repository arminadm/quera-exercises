# 200/200
#Armin Darabi Mahboub

matrix = []
toolMatris = input()
toolMatris = int(toolMatris)
for iIndex in range(toolMatris):
    temp = input().split()
    matrix.append(temp)
for iIndex in range(toolMatris):
    for jIndex in range(toolMatris):
        matrix[iIndex][jIndex] = int(matrix[iIndex][jIndex])
class Geraf:
   def yal_vaslShode(self):
      found = []
      yal_vasl = []
      for iIndex in range(self.V):
         found.append(False)
      for v in range(self.V):
         if found[v] == False:
            temp = []
            yal_vasl.append(self.something(temp, v, found))
      return yal_vasl
   def yal_ezaf(self, v, w):
      self.adj[v].append(w)
   def something(self, temp, v, found):
      found[v] = True
      temp.append(v)
      for iIndex in self.adj[v]:
         if found[iIndex] == False:
            temp = self.something(temp, iIndex, found)
      return temp
   def _init_(self, V):
      self.V = V
      self.adj = [[] for iIndex in range(V)]
matrisGeraf = Geraf(int(toolMatris)*int(toolMatris))
for iIndex in range(toolMatris):
    for jIndex in range(toolMatris):
        if matrix[iIndex][jIndex] == 1:
            if iIndex-1 >= 0 and matrix[iIndex-1][jIndex] == 1:
                matrisGeraf.yal_ezaf(iIndex*toolMatris+jIndex, (iIndex-1)*toolMatris+jIndex)
            if iIndex+1 < toolMatris and matrix[iIndex+1][jIndex] == 1:
                matrisGeraf.yal_ezaf(iIndex*toolMatris+jIndex, (iIndex+1)*toolMatris+jIndex)
            if jIndex-1 >= 0 and matrix[iIndex][jIndex-1] == 1:
                matrisGeraf.yal_ezaf(iIndex*toolMatris+jIndex, (iIndex)*toolMatris+jIndex-1)
            if jIndex+1 < toolMatris and matrix[iIndex][jIndex+1] == 1:
                matrisGeraf.yal_ezaf(iIndex*toolMatris+jIndex, (iIndex)*toolMatris+jIndex+1)
geraf = matrisGeraf.yal_vaslShode()
biggestTresure = 0
for iIndex in range(len(geraf)):
    if len(geraf[iIndex])>biggestTresure:
        biggestTresure = len(geraf[iIndex])
print(biggestTresure)