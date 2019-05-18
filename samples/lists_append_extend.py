attendees = ["me", "you", "someone"]
attendees.append("them")
attendees.extend(["him", "her"])
optional_invitees = ["us", "they"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently")
