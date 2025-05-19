#Conditionals

motion_detected = handle_event.get("motion_detected")
temperature_rise = handle_event.get("temperature")

motion = False
temp = True
if motion:
    print(f"Suspicious motion detected at {location} inform {motion_detected} ")


if temp:
    print(f"Warning, temperature at {location} is high inform {temperature_rise} ")


