#date:1/5/2022
#comments: the algorithim uses brute force to determine which pairs are the closest_pair to each other. as it uses brute force we use two nested for loops which means the time complexity is O^2 meaning its pretty darn slow


def closest_pair(list_cords):
  if len(list_cords) < 2:
    return None
  else:
    distance_dict = dict()
    for i in range(len(list_cords)):
        x1 = list_cords[i][0]
        y1 = list_cords[i][1]
        dist_list = list()
        dist_list_cords = list()
        for x in range(len(list_cords)):
          if i == x:
            pass
          else:
            x2 = list_cords[x][0]
            y2 = list_cords[x][1]
            dist_list.append((((x2-x1)**2)+((y2-y1)**2))**(1/2))
            dist_list_cords.append((x2,y2))
        distance_dict[((x1,y1),dist_list_cords[dist_list.index(min(dist_list))])] = min(dist_list)
    return min(distance_dict,key=distance_dict.get)

print(closest_pair([(1, 1), (2,2), (10, 10), (20, 20)]))
#expected: ((1,1),(2,2))
