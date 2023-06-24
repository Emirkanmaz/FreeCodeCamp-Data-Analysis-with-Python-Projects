import numpy as np

def calculate(list):
  
  if len(list) < 9:
    raise ValueError ("List must contain nine numbers.")

  listArray = np.array(list).reshape(3,3)

  meanList = [(listArray.mean(axis=0).tolist()), (listArray.mean(axis=1).tolist()), (listArray.flatten().mean())]
  varianceList = [(listArray.var(axis=0).tolist()), (listArray.var(axis=1).tolist()), (listArray.flatten().var())]
  standardDeviationList = [(listArray.std(axis=0).tolist()), (listArray.std(axis=1).tolist()), (listArray.flatten().std())]
  maxList = [(listArray.max(axis=0).tolist()), (listArray.max(axis=1).tolist()), (listArray.flatten().max())]
  minList = [(listArray.min(axis=0).tolist()), (listArray.min(axis=1).tolist()), (listArray.flatten().min())]
  sumList = [(listArray.sum(axis=0).tolist()), (listArray.sum(axis=1).tolist()), (listArray.flatten().sum())]

  calculations = {
  'mean': meanList,
  'variance': varianceList,
  'standard deviation': standardDeviationList,
  'max': maxList,
  'min': minList,
  'sum': sumList
  }
  
  return calculations
