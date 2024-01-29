import random

def coin_flip():
    return random.randint(0, 1)  
#  0 -Tails , 1 -Heads
def main():
        result = coin_flip()
        if result == 0:
            print("Tails!")
        else:
            print("Heads!")
if __name__ == "__main__":
    main()