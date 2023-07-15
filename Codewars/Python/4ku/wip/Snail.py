# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]





class Snail():
    def __init__(self,arr) -> None:
        self.arr = arr
        self.position = [0,0]
        self.length = len(arr[0])
        self.height = len(arr)
        self.direction = 0
        self.distance = self.length
        self.output = []
        
    def single_traverse(self) -> None:
        if self.direction == 0: # right
            for x in range(self.distance):
                if x != 0:
                    self.position[1] += 1
                self.add_target()
            self.distance -= 1

        elif self.direction == 1: #down
            for x in range(self.distance):
                self.position[0] += 1
                self.add_target()

        elif self.direction == 2: #left
            for x in range(self.distance):
                self.position[1] -= 1
                self.add_target()

        elif self.direction == 3: #up
            self.distance -= 1
            for x in range(self.distance):
                self.position[0] -= 1
                if x != self.distance-1:
                    self.add_target()


        self.direction = (self.direction+1) % 4

    def full_traverse(self):
        while self.distance > 0:
            self.single_traverse()
            # print(self.distance)
        return self.output
        
    def target(self):
        return self.arr[self.position[0]][self.position[1]]
    
    def add_target(self):
        self.output.append(self.target())

def snail(snail_map):
    return Snail(snail_map).full_traverse()

print(snail(array))

# expected = [1,2,3,6,9,8,7,4,5]
# print(snail(array), expected)



# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# expected = [1,2,3,4,5,6,7,8,9]
# print(snail(array), expected)
