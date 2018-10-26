# -*- coding: utf-8 -*-

import sys
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration
from geopy.distance import geodesic

@Configuration()
class GeodistCommand(StreamingCommand):
    def stream(self, records):
        src_lat_field = 'start_station_latitude'
        src_lon_field = 'start_station_longitude'
        dst_lat_field = 'end_station_latitude'
        dst_lon_field = 'end_station_longitude'
        dist_field = 'geodist'
        for record in records:
            src_point = (record[src_lat_field], record[src_lon_field])
            dst_point = (record[dst_lat_field], record[dst_lon_field])
            record[dist_field] = geodesic(src_point, dst_point).km
            yield record

if __name__ == "__main__":
    dispatch(GeodistCommand, sys.argv, sys.stdin, sys.stdout, __name__)

