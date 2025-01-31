# Authors : Jerry Chen
# Emails : yanzhechen@umass.edu
# Spire IDs : 34835664
class Thermostat:
    def __init__(self,temp=68):
        self.temp = temp
        self.schedule = {}
    def add_schedule(self,time,temp):
        self.schedule.update({time:temp})
    def __str__(self):
        my_str = [f"Default temperature: {self.temp} degrees"]
        for time in sorted(self.schedule):
            my_str.append(f"\n{time} {self.schedule[time]} degrees")
        return "".join(my_str)
    def get_target_temperature(self,time):
        schedule = sorted(self.schedule)
        counter = 0
        if not schedule:
            return self.temp
        while counter < len(schedule):
            if(time < schedule[counter]):
                if(counter == 0):
                    return self.temp
                else:   
                    return self.schedule[schedule[counter-1]]
            counter+=1
        return self.schedule[schedule[-1]]