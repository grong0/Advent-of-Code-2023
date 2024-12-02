from code import interact
from distutils.command.build_scripts import first_line_re
import os
from time import sleep
from typing import Optional
from colorama import Fore, Style

def part1():
    def getGrid():
        grid = []
        with open("./day10/day10.txt") as f:
            for line in f:
                row = []
                for col in line:
                    row.append(col)
                grid.append(row)
        return grid
    
    def getValue(coords: tuple[int, int]) -> str:
        return getGrid()[coords[0]][coords[1]]
    
    def getSPosition() -> tuple[int, int]:
        for y, row in enumerate(getGrid()):
            for x, col in enumerate(row):
                if col == "S":
                    return (y, x)
        return (-1, -1)

    def getNeighbors(coords: tuple[int, int]) -> dict:
        grid = getGrid()
        north = ""
        east = ""
        south = ""
        west = ""
        if coords[0] - 1 > -1:
            north = (coords[0] - 1, coords[1])
        else:
            north = None
        if coords[1] + 1 < len(grid[0]):
            east = (coords[0], coords[1] + 1)
        else:
            east = None
        if coords[0] + 1 < len(grid):
            south = (coords[0] + 1, coords[1])
        else:
            south = None
        if coords[1] - 1 > -1:
            west = (coords[0], coords[1] - 1)
        else:
            west = None
        return {
            "north": north,
            "east": east,
            "south": south,
            "west": west,
        }
        
    def getOpposite(direction: str) -> Optional[str]:
        match direction:
            case "north":
                return "south"
            case "east":
                return "west"
            case "south":
                return "north"
            case "west":
                return "east"
            case _:
                return None
            
    def getDirectionalCoords(coords: tuple[int, int], direction: str):
        match direction:
            case "north":
                return (coords[0]+1, coords[1])
            case "east":
                return (coords[0], coords[1]+1)
            case "south":
                return (coords[0]-1, coords[1])
            case "west":
                return (coords[0], coords[1]-1)
        
    def getConnectors(coords: tuple[int, int]) -> list[str]:
        if getValue(coords) == "S":
            neighbors = getNeighbors(getSPosition())
            directions = []
            if "south" in getDirections(getValue(neighbors["north"])):
                directions.append("north")
            if "west" in getDirections(getValue(neighbors["east"])):
                directions.append("east")
            if "north" in getDirections(getValue(neighbors["south"])):
                directions.append("south")
            if "east" in getDirections(getValue(neighbors["west"])):
                directions.append("west")
            return directions
            
        lookingAt = getDirections(getValue(coords))        
        connectors = []
        if getOpposite(lookingAt[0]) in getDirections(getValue(getNeighbors(coords)[lookingAt[0]])):
            connectors.append(lookingAt[0])
        if getOpposite(lookingAt[1]) in getDirections(getValue(getNeighbors(coords)[lookingAt[1]])):
            connectors.append(lookingAt[1])
        return connectors
        
    def getDirections(symbol: str) -> list[str]:
        match symbol:
            case "|":
                return ["north", "south"]
            case "-":
                return ["west", "east"]
            case "L":
                return ["north", "east"]
            case "J":
                return ["north", "west"]
            case "7":
                return ["west", "south"]
            case "F":
                return ["east", "south"]
            case ".":
                return []
            case "S":
                return getConnectors(getSPosition())
            case _:
                return []
            
    def getNextPosition(coords: tuple[int, int], prev_coords: Optional[tuple[int, int]]) -> tuple[int, int]:
        directions = getConnectors(coords)
        neighbors = getNeighbors(coords)
        if prev_coords == None:
            return neighbors[directions[0]]
        
        connectors = [neighbors[direction] for direction in directions]
        connectors.remove(prev_coords)
        return connectors[0]
    
    def printBoard(list_of_coords):
        os.system("cls")
        for y, row in enumerate(getGrid()):
            for x, col in enumerate(row):
                if (y, x) in list_of_coords:
                    print(Fore.GREEN + col, end="")
                    print(Style.RESET_ALL, end="")
                else:
                    print(col, end="")
                # if x == len(row)-1:
                #     print()'
                
    loop = []
    current_coords = getSPosition()
    prev_coords = None
    while True:
        loop.append(current_coords)
        if len(loop) % 100 == 0:
            print(len(loop))
        
        current_coords = getNextPosition(current_coords, prev_coords)
        prev_coords = loop[-1]
        if current_coords == loop[0]:
            break
    return len(loop)/2

print(part1())
