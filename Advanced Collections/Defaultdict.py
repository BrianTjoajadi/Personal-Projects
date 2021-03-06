from collections import defaultdict

def main():
    fruits = ["apple", "pear", "orange", "banana", "apple", "grape", "banana", "banana"]

    # use a dictionary to count each element
    fruitCounter = defaultdict(int) 
    #int represents a factory function

    #Count elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1
    
    for k, v in fruitCounter.items():
        print(k + ": " +str(v))

if __name__ == "__main__":
    main()
