#task2.1
rover_status= {
"battery":100,
"Heater":"off",
"camera":"standby"
}

print (rover_status["battery"])

#task2.2
rover_status.update({"battery":85})
rover_status.update({"heater":"on"})
rover_status.update({"speeed":5})
print(rover_status)

#task2.3
mission_log= [
{"Site": "Crater A", "Radiation": "Low", "Water": False},
{"Site": "Dune B", "Radiation": "High", "Water": True}
]
for i in len(mission_log):
    print("site", ["site"][i]," has", ["Radiation"][i], "Radiation")