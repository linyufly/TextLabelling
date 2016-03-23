import reader

def main():
  res = reader._parse_recipe('./raw_data/dataset.txt')
  print res
  print res.shape

if __name__ == '__main__':
  main()

