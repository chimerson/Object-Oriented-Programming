class Time:
    def __init__(self, time):
        self._time = time

    def convert_to_minutes(self,):
        in_minutes = self._time//60
        remaining_seconds = self._time % 60  
        return '{}:{}'.format(in_minutes, remaining_seconds)

    def convert_to_hours(self):
        in_hours = self._time//3600
        remaining_seconds = self._time % 3600
        the_minutes = remaining_seconds//60
        seconds = remaining_seconds % 60
        return '{}:{}:{}'.format(in_hours, the_minutes, seconds)

if __name__ == '__main__':

    time_calculator = Time(7000)
    print(time_calculator.convert_to_hours())
    print(time_calculator.convert_to_minutes())       
