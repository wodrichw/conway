class Table:
  def __init__(self, size, start=[1]):
    self.generateTable(size, start)

  def generateRow(self, prevRow):
    row = []
    count = 1
    for i in range(len(prevRow)):
      if i < len(prevRow) - 1 and prevRow[i] == prevRow[i + 1]:
        count += 1
      else:
        row.append(count)
        row.append(prevRow[i])
        count = 1
    return row

  def generateTable(self, size, start):
    self.table = [self.generateRow(start)]
    for i in range(0, size):
      self.table.append(self.generateRow(self.table[i]))

  def numVomit(self):
    for row in self.table:
      print (row)
        

class Row:
  def __init__(self, prevRow):
    self.generateRow(prevRow)
  
  def generateRow(self, prevRow):
    self.row = []
    count = 1
    for i in range(len(prevRow) - 1):
      if prevRow[i] == prevRow[i + 1]:
        count += 1
      else:
        self.row.append(count)
        self.row.append(prevRow[i])
        count = 1


t = Table(20, [3, 1, 1, 3])
t.numVomit()