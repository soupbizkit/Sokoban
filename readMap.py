import sys 

def leerMapa():
    mapa = []
    cajasPos = []
    for line in sys.stdin:
        line = line.rstrip()
        if line.startswith('W'):
            print(line)
            #map.append(line)

    #if line.startswith("X-DSPAM-Confidence:"):
     #       count += 1
      #      valor += float(line[20:])
 #           average = valor/count

#    print("Average spam confidence:","{0:.12f}".format(average))