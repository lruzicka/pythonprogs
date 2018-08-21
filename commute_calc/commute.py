#!/bin/env/python3

import itertools


class Route:
    def __init__(self, start, stop, vehicle, distance, price):
        
        self.type = vehicle
        self.start = start
        self.stop = stop
        self.cena = float(price)
        self.distance = float(distance)
        self.discount = 25
        self.carcost = 2.55

    def price(self):
        if self.cena == 0.0 and self.distance != 0.0: 
            price = round(self.distance * self.carcost)
        elif self.cena != 0 and self.distance == 0:
            coef = 100 - self.discount
            price = round((coef*self.cena)/100)
        else:
            price = None

        return price

    def text(self):
        return f"Start: {self.start}, Target: {self.stop}, Type: {self.type}"

class Routes:
    def __init__(self):
        self.routes = []

    def add_route(self, route):
        if route not in self.routes:
            self.routes.append(route)
            return 0
        else:
            return 1

    def show_all_routes(self):
        routes = []
        for route in self.routes:
            routes.append(route.text())
        return routes

    def show_options(self, start, stop):
        routes = []
        direct = []
        start_match = []
        stop_match = []
        for route in self.routes:
            if route.start == start and route.stop == stop:
                direct.append(route)
            elif route.start == start:
                start_match.append(route)
            elif route.stop == stop:
                stop_match.append(route)
        indirect = []
        for route1 in start_match:
            for route2 in stop_match:
                if route1.stop == route2.start:
                    indirect.append([route1, route2])
        routes = direct + indirect
        return routes

    def show_prices(self, start, stop):
        options = self.show_options(start, stop)
        result = []
        for option in options:
            cesty = {}
            if isinstance(option, list):
                cesta = {}
                total = 0
                for o in option:
                    total += o.price()
                    if not 'start' in cesta.keys():
                        cesta['start'] = o.start
                        cesta['via'] = o.stop
                    else:
                        cesta['stop'] = o.stop
                    cesta['price'] = total
                print(cesta)
                   
            else:
                print(f"{option.start}, {option.stop}, {option.type}, {option.price()}")
        

    



cesty = [
        'mikulov,brno,car,58.6,0',
        'mikulov,breclav,car,24,0',
        'mikulov,zajeci,car,18,0',
        'mikulov,sakvice,car,22.2,0',
        'mikulov,vranovice,car,22.4,0',
        'brno,mikulov,car,58.6,0',
        'vranovice,mikulov,car,22.4,0',
        'sakvice,mikulov,car,22.2,0',
        'zajeci,mikulov,car,18,0',
        'breclav,mikulov,car,24,0',
        'breclav,brno,car,69.8,0',
        'brno,breclav,car,69.8,0',
        'vranovice,brno,train,0,45',
        'brno,vranovice,train,0,45',
        'sakvice,brno,train,0,54',
        'brno,sakvice,train,0,54',
        'zajeci,brno,train,0,60',
        'brno,zajeci,train,0,60',
        'breclav,brno,train,0,80',
        'brno,breclav,train,0,80',
        'mikulov,breclav,train,0,33',
        'breclav,mikulov,train,0,33',
        ]



routes = Routes()

for cesta in cesty:
    c = cesta.split(',')
    route = Route(c[0], c[1], c[2], c[3], c[4])
    routes.add_route(route)
    

routes.show_prices('mikulov','brno')
