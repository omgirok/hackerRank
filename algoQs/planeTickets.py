# method that takes an array of plane tickets and the starting point,
# return final destination

def planeTickets(arr, origin):
  
  # all starting locations will also be destinations except for one
  # we know the origin
  starting = [ y[0] for y in arr ]
  # flights stores all the starting locations
  flights = dict.fromkeys(starting, -1)
  # print flights


  ending = [ y[1] for y in arr ]
  current = origin
  # print "destinatinons are",ending
  trip = []
  trip.append(origin)

  # all destinations will also be departure points except for one,
  # need to find this
  try:
    for arrival in ending:
      # print "starting on",arrival
      if flights[arrival]:
        # print "deleting", arrival
        del flights[arrival]
  except KeyError:
      # print "Destination",arrival,"was not found as a starting point"
      trip.append(arrival)
      pass
  return trip[0] + "->" + trip[1]

arr = [["LAX","SFO"],
       ["JFK","TPE"],
       ["TPE","MXC"],
       ["LGA","TPE"],
       ["NYC","MEX"],
       ["MEX","ATL"],
       ["TEX","LAX"],
       ["SFO","TPE"]]

# method that takes a shitload of plane tickets, 
# you ask it the starting point,
# it returns the final destination

def planeTickets_2(arr, origin):
  flights = {}
  for x in arr:
    start,end = x[0],x[1]
    flights[start] = end

  current = origin
  try:
    while flights[current]:
      current = flights[current]
  except KeyError:
    return current

print planeTickets_2(arr,"NYC")




