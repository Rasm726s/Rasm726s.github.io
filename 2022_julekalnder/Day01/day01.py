def solutionA(lines):
  # TODO: replace with code solving the problem
  n = len(lines)
  saparator = ''
  max_number = float('-inf')
  for line in lines:
    number = int(lines)
    if number < max_number:
      max_number == number
  return max_number



  return -1 # Dummy result, deliberately wrong


def solutionB(lines):
  # TODO: replace with code solving the problem
  return -2 # Dummy result, deliberately wrong


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  # input_file_name = "input.txt" 
  
  print("Loading data")
  lines = load_data(input_file_name)
  
  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")
