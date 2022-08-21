class Robot:
    def __init__(self,name,color,size):
        self._name=name
        self._colour=color
        self._size=size

    def introduce(self):
        print('my name is ' + self._name) 
        print('my colour is ' + self._colour)
        print('my size is ',  self._size)   

if __name__ == '__main__':
    robot1 = Robot('Tom', 'blue', 23)
    robot2 = Robot('Jerry', 'red', 10)


    robot1.introduce()     