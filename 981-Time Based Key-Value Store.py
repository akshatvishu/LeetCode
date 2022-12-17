class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            # if key does not exist then create a new dict!
            self.data[key]=[(timestamp,value)]
        else:
            # If the key exists then add the new value
            self.data[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.data:
            return ""
        
        values = self.data[key]
        left = 0
        right = len(values) - 1

        while left < right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid +1
            
            else:
                right = mid 
        if values[left][0] <= timestamp:
            return values[left][1]

        #  value at index left does not have a timestamp    less than or equal to the target timestamp.
        elif left > 0:

            """
            if left is greater than 0. If it is, then the method returns the value at the previous index, because it is the most recent value with a timestamp less than or equal to the target timestamp that the method has encountered so far
            """

            return values[left-1][1]
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp) # obj.set("foo", "bar", 1) # {'foo': [(1, 'bar')]}
# param_2 = obj.get(key,timestamp) # param_2 = obj.get("foo", 1) # 'bar'
