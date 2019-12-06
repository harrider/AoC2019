class MapDataParser:

    def __init__(self):
        self


    def num_orbits(self, map_data):
        orbiting_objects = self._generate_map(map_data)

        number_of_orbits = 0
        for orbiting_object in orbiting_objects.values():
            while orbiting_object != '':
                number_of_orbits += 1

                orbiting_object = orbiting_objects[orbiting_object]

        return number_of_orbits


    def shortest_hop(self, map_data):
        orbiting_objects = self._generate_map(map_data)

        you_to_com_hops = self._generate_hops('YOU', 'COM', orbiting_objects)
        san_to_com_hops = self._generate_hops('SAN', 'COM', orbiting_objects)

        hops_intersections = [
            ((you_to_com_hops[x] + san_to_com_hops[x]), x) 
            for x in you_to_com_hops.keys() & san_to_com_hops.keys()
        ]

        smallest_num_hops, location = min(hops_intersections)

        return smallest_num_hops


    def _generate_map(self, map_data):
        orbiting_objects = {'COM' : ''}
        
        for orbit_data in map_data:
            parent, child = orbit_data.split(')')
            orbiting_objects[child] = parent

        return orbiting_objects


    def _generate_hops(self, start_location, stop_location, orbiting_objects):
        curren_location_to_com_hops =  {}
        current_location = orbiting_objects[start_location]
        num_hops = 0
        while current_location != stop_location:
            curren_location_to_com_hops[current_location] = num_hops
            num_hops += 1
            current_location = orbiting_objects[current_location]

        return curren_location_to_com_hops