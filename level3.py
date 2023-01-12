import json
def solve(lst):
  dict = {}
  if lst[22] == '"-1"':
    dict = {
          "CHEMBLID" : lst[0],
          "Name" : lst[1],
          "Type" : lst[2],
          "MaxPhase" : lst[3],
          "Molecular target" : lst[4],
          "Bio Activity" : lst[5],
          "ALogP" : lst[6],
          "Polar Surface Area" : lst[7],
          "HBA" : lst[8],
          "HBD" : lst[9],
          "#RO5 Violations" : lst[10],
          "Rotatable bonds" : lst[11],
          "Passes ro3" : lst[12],
          "QED Weight" : lst[13],
          "Cx Acid pka" : lst[14],
          "Cx basic pka" : lst[15],
          "CX log P" : lst[16],
          "CX Log D" : lst[17],
          "Aromatic" : lst[18],
          "Structure" : lst[19],
          "Inorganic" : lst[20],
          "HBA(lipiski)" : lst[21],
          "HBD(lipiski)" : lst[22],
          "Molecular Formula" : lst[29],
          "Smiley" : lst[30]
      
    }
    with open('MyJson.json','w') as json_file:
      json.dump(dict,json_file)
  
    
    
def main():
  try:
    loc = input(">> Enter location : ")
    with open(loc) as file:
      lent = len(file.readlines())
    with open(loc) as fl:
      for i in range(lent ):
        data = fl.readline()
        solve(data)
  except Exception as e:
    print("OOPS :(",e)
  else:
    print("BYE BYe")
      
main()

