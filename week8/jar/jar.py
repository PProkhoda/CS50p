class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def withdraw(self, n):
        if n < 0 or n > self._size:
            raise ValueError
        else:
            self._size -= n
        

    def deposit(self, n):
        if n > self.capacity or (n + self._size) > self.capacity:
            raise ValueError
        else:
            self._size += n


    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if  capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        return self._size

# // Testing the jar class
def main():
    jar = Jar()
    print(jar.capacity)
    print(jar.size)
    print(str(jar))
    
   
    jar.deposit(5)
    print(jar.capacity)
    print(jar.size)
    print(str(jar))
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.size)
    print(str(jar))
    # jar.capacity = 17
    # student = Student("Harry", "Gryffindor")
    # print(student)
        

if __name__ == "__main__":
    main()