class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        stack = []
        cars.sort(reverse = True)
        for pos,speed in cars:
            distance = target-pos
            time = distance/speed
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)






        
