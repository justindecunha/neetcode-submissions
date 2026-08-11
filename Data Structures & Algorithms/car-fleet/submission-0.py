class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        '''

        class car:
            position
            speed
            finish_time

        as long as car[i-1].finish_time > car[i].finish_time, car

        target 10

        position 0 speed 1 (10 - 0) / 1 = 10s
        position 1 speed 2 (10 - 1) / 2 = 5s
        position 4 speed 2 (10 - 4) / 2 = 3s
        position 7 speed 1 (10 - 7) / 1 = 3s
        position 8 speed 0.1 (10 - 8) / 0.1 = 20s

        sort by position

        current_max_finish_time = float('-inf')
        bucket_count = 0

        current_max_finish_time = 20
        bucket_count = 1

        for car in reversed(cars):
            if car.finish_time > current_max_finish_time:
                bucket_count += 1
                current_max_finish_time = car.finish_time
        
        return bucket_count
        '''

        cars = sorted(zip(position, speed))

        fleets, max_time = 0, 0

        for pos, spd in reversed(cars):
            time = (target - pos) / spd

            if time > max_time:
                fleets += 1
                max_time = time
        
        return fleets

        