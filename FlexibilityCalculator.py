import random
from datetime import datetime

class FlexibilityCalculator:
    @staticmethod
    def calculate_flexibility_contribution(request):
        """ Calculate the flexibility score based on request parameters """
        weights = {
            'time_flexibility': 0.4,
            'power_flexibility': 0.3,
        }

        time_flexibility = (request.requested_leave_time - request.charging_start_time).total_seconds() / 3600  # Hours    
        power_flexibility = request.car_specs.battery_capacity_in_kwh - request.requested_energy
        ### rename the time_flexibility to remianing_time
        ### rename the power_flexibility to energy_to_be_charged

        flexibility_score = (time_flexibility * weights['time_flexibility']) + (power_flexibility * weights['power_flexibility'])
        

        return flexibility_score
