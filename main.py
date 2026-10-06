import krpc

TARGET_ALTITUDE = 100_000.0

APOAPSIS_TOLERANCE = 500.0
PERIAPSIS_TOLERANCE = 500.0

CONTROL_FREQ = 100.0 #Hz

PHASE = "SRB_ASCENT"

conn = krpc.connect(name = "Orbital Guidance")
sc = conn.space_center
vessel = sc.activate_vessel
flight_info = vessel.flight()



def guidence_srb():
     
    return pitch, roll, yaw

def srb_burnout():
    pass

def guidance_lp():
    pass

def apoapsis_traj_achieved():
    pass

def coast_to_apoapsis_guidance():
    pass

def apoapsis_achieved():
    pass





while True:
    
    if PHASE == "SRB_ASCENT":
        
        pitch, roll, yaw = guidence_srb()

        if srb_burnout():
            vessel.control.activate_next_stage()
            vessel.control.throttle = 0.5
            PHASE = "LP_ASCENT"
            
    elif PHASE == "LP_ASCENT":
        
        pitch, roll, yaw = guidance_lp()
        
        if apoapsis_traj_achieved():
            vessel.control.throttle = 0.0
            PHASE = "COAST_TO_A"
            
    elif PHASE == "COAST_TO_A":
        
        pitch, roll, yaw = coast_to_apoapsis_guidance()
        
        if apoapsis_achieved():
            PHASE = "PERIAPSIS_BURN"
            
    elif PHASE == "PERIAPSIS_BURN":
        pass
            
        
        
        
        


