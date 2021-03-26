class UndergroundSystem:

    def __init__(self):
        self.checked_in = {}
        self.trips_time = {}  # key (stat_start, stat_end): (tot_time, trips_num)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_from, start_time = self.checked_in[id]
        trip_time = t - start_time
        curr_trip_total, curr_trip_num = self.trips_time.get((station_from, stationName), (0, 0))
        self.trips_time[(station_from, stationName)] = (curr_trip_total + trip_time, curr_trip_num + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip_total, trip_num = self.trips_time[(startStation, endStation)]
        return trip_total / trip_num

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
