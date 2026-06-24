class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        stack = []
        cars.sort(reverse = True)
        for car in cars:
            dis = target-car[0]
            time = dis/car[1]
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)






        
