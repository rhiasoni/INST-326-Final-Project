from spacex import SpaceX, UpcomingLaunches

upcoming_launches = UpcomingLaunches()
launches = upcoming_launches.get_upcoming_launches()

payloads = upcoming_launches.get_payloads(launches)
print ("Payloads:")
for p in payloads:
	print ("\t" + p)

print ("\n\n")

payload_counts = upcoming_launches.get_payload_count(payloads)
print ("Payload Counts:")
for p in payload_counts:
	print ("\t %s \t %d" %(p, payload_counts[p]))
