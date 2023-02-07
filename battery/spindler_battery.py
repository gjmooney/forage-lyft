from battery.battery import Battery
from utils import add_years_to_date

# Service every 2 years
class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = add_years_to_date(self.last_service_date, 3)

        if service_threshold_date < self.current_date:
            return True
        else:
            return False

