# -*- coding: utf-8 -*-

import sys
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators
from geopy.distance import geodesic

@Configuration()
class GeodistCommand(StreamingCommand):
    src_lat_field = Option(require=False, default='start_station_latitude')
    src_lon_field = Option(require=False, default='start_station_longitude')
    dst_lat_field = Option(require=False, default='end_station_latitude')
    dst_lon_field = Option(require=False, default='end_station_longitude')
    dist_field = Option(require=False, default='geodist')

    def stream(self, records):
        for record in records:
            src_point = (record[self.src_lat_field], record[self.src_lon_field])
            dst_point = (record[self.dst_lat_field], record[self.dst_lon_field])
            record[self.dist_field] = geodesic(src_point, dst_point).km
            yield record

if __name__ == "__main__":
    dispatch(GeodistCommand, sys.argv, sys.stdin, sys.stdout, __name__)

