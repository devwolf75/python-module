from os import path, pardir, getcwd
from dotenv import dotenv_values

def main(self):
  VARS = dotenv_values(path.abspath(path.join(getcwd(), ".env")))
  print(VARS["ENV_VARIABLE"))

if __name__ == "__main__":
  main()
