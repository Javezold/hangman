import re
import random

def run():
    elegidas = []
    
    for i in range(10):
        letra = input("Dame una palabra: ")
        elegidas.append(letra)
        elegidas = list(dict.fromkeys(elegidas))

if __name__ == "__main__":
    run()