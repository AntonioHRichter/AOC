itinerary = {}
var_dict = {'result' : [0], 'small_dist' : -1, 'big_dist' : -1}

def addItinerary(place, to, dist):
    global itinerary
    if place in itinerary:
        itinerary[place][to] = dist
    else :
        itinerary[place] = {to : dist}

def allVisited(place):
    global itinerary
    for k in itinerary[place]:
        if k not in var_dict['result']:
            return False
    return True


def smallerPlaceInItinerary(place):
    global itinerary
    dist = ('', -1)
    for k, v in itinerary[place].items():
        if k not in var_dict['result']:
            if int(v) < dist[1] or dist[1] < 0:
                dist = k, int(v)
    return dist

def biggerPlaceInItinerary(place):
    global itinerary
    dist = ('', -1)
    for k, v in itinerary[place].items():
        if k not in var_dict['result']:
            if int(v) > dist[1]:
                dist = k, int(v)
    return dist

def searchSmallerRoute(place):
    global itinerary
    if place not in var_dict['result']:
        var_dict['result'].append(place)
        if not allVisited(place):
            place, dist = smallerPlaceInItinerary(place)
            var_dict['result'][0] += dist;
            searchSmallerRoute(place)

def searchBiggerRoute(place):
    global itinerary
    if place not in var_dict['result']:
        var_dict['result'].append(place)
        if not allVisited(place):
            place, dist = biggerPlaceInItinerary(place)
            var_dict['result'][0] += dist;
            searchBiggerRoute(place)

def startSearch():
    global itinerary
    for k in itinerary:
        searchSmallerRoute(k)
        print(var_dict['result'])
        if var_dict['result'][0] < var_dict['small_dist'] or var_dict['small_dist'] < 0:
            var_dict['small_dist'] = var_dict['result'][0]
        var_dict['result'] = [0]
    
    var_dict['result'] = [0]
    print(var_dict['small_dist'])

    for k in itinerary:
        searchBiggerRoute(k)
        print(var_dict['result'])
        if var_dict['result'][0] > var_dict['big_dist']:
            var_dict['big_dist'] = var_dict['result'][0]
        var_dict['result'] = [0]

for line in open('2015\\2015_9\\input.txt', 'r'):
    (start, end) = line.split('to')
    start = start.strip().replace(' ', '')
    (end, distance)= end.strip().replace(' ', '').split('=')
    addItinerary(start, end, distance)
    addItinerary(end, start, distance)


startSearch()
print(var_dict['big_dist'])