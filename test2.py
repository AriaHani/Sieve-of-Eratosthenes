print("Aria Hani\nSieve of Eratosthenes")
print("\nit returns all the prime numbers smaller then your stop point.")
endPoint = int(input("what is the stop point? "))+1
myList = list(range(2, endPoint))
for myNumber in range(2, int(endPoint**0.5)):
    for number in range(2 , 1+(endPoint//myNumber)):
        if myNumber*number in myList:
            myList.remove(myNumber*number)
print(myList)