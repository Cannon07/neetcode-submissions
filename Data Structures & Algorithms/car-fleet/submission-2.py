class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pos_speed = []

        for i in range(len(position)):
            car_pos_speed.append([position[i], speed[i]])
        car_pos_speed.sort(reverse=True)
        
        stack = []

        for i in car_pos_speed:
            if len(stack) == 0:
                stack.append(i)
                continue
            
            top = stack[-1] 
            top_time = (target - top[0]) / top[1]
            i_time = (target - i[0]) / i[1]

            if i_time > top_time:
                stack.append(i)
                
        return len(stack)
        