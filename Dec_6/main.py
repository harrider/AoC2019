from celestialmap import MapDataParser


if __name__ == '__main__':

    with open('MapData.txt', 'r') as map_data_file:
        map_data = map_data_file.read().split('\n')

    parser = MapDataParser()
    
    result1 = parser.num_orbits(map_data)
    print(f'Number of orbits: {result1}')

    result2 = parser.shortest_hop(map_data)
    print(f'Smallest Number of Hops: {result2}')
