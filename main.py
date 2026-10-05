import krpc

conn = krpc.connect()
vessel = conn.space_center.active_vessel
flight_info = vessel.flight()

vessel.control.throttle = 1.0

vessel.control.activate_next_stage()

with conn.stream(getattr, flight_info, "mean_altitude") as altitude:
        while True:
            print(altitude())
