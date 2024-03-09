import numpy as np

def calculate(list):
      """ Calculates the mean, variance, standard deviation, max, min, and sum of the rows, columns from a list """

      # Raises an error if length of list is higher than 9
      if len(list) != 9:
          raise ValueError("List must contain nine numbers.")
        
      # Convert list to 3x3 numpy array
      arr = np.array(list).reshape(3, 3)

      # Calculate statistics
      stats = {
          'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).tolist()],
          'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).tolist()],
          'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).tolist()],
          'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).tolist()],
          'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).tolist()],
          'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).tolist()]
      }

      return stats