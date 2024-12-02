from platform import architecture
# from arepl_dump import dump


import os


def listSplit(givenList: list[str], key):
    list = []
    tempList = []
    for item in givenList:
        if item == key:
            list.append(tempList)
            tempList = []
        else:
            tempList.append(item.replace("\n", ""))
    list.append(tempList)
    return list


def part1():
    answer = ""

    keyMap = ["num", "soil", "fert", "water", "light", "temp", "humi", "loca"]
    with open("./day5.txt") as f:
        lines = list(f)
        lines = listSplit(lines, "\n")

        seeds = {}
        for i, map in enumerate(lines):
            if i == 0:  # seeds
                for seed in map[0].split(" ")[1:]:
                    seeds[int(seed)] = {"num": int(seed)}
                print(seeds)
                continue
            
            sourceKey = keyMap[i - 1]
            destKey = keyMap[i]
            print(f"destKey: {destKey}")
            print(f"sourceKey: {sourceKey}")
            
            content = map[1:]
            
            sources = [seeds[i][sourceKey] for i in seeds.keys()]
            print(f"sources: {sources}")
            
            for line in content:
                dest_start = int(line.split(" ")[0])
                source_start = int(line.split(" ")[1])
                length = int(line.split(" ")[2])
                for z, source in enumerate(sources):
                    if source >= source_start and source < source_start + length:
                        seeds[list(seeds.keys())[z]][destKey] = dest_start + (source - source_start)
            # print()

            print("i == " + str(i))
            
            print()
            # for z, source in enumerate(source_range):
            #     for seed in seeds.keys():
            #         if seeds[seed][destKey] == source:
            #             seeds[seed][sourceKey] = destination_range[z]
                        
            for seed in seeds.keys():
                if destKey not in seeds[seed].keys():
                    seeds[seed][destKey] = seeds[seed][sourceKey]
        
        lowest = seeds[list(seeds.keys())[0]]['loca']
        for seed in seeds.keys():
            if seeds[seed]['loca'] < lowest:
                lowest = seeds[seed]['loca']
        answer = lowest
        
        # print(seeds)
        # dump()
    print(seeds)
    # dump()
    return answer


def part2():
    answer = ""

    keyMap = ["num", "soil", "fert", "water", "light", "temp", "humi", "loca"]
    with open("./day5.txt") as f:
        lines = list(f)
        lines = listSplit(lines, "\n")

        seeds = {}
        seed_ranges = []
        for i, map in enumerate(lines):
            if i == 0:  # seeds
                seeds_raw = map[0].split(" ")[1:]
                for z in range(0, len(seeds_raw), 2):
                    print(f"{z}/{len(seeds_raw)-1}")
                    starting_index = int(seeds_raw[z])
                    ending_index = int(seeds_raw[z]) + int(seeds_raw[z+1])
                    seed_ranges.append([starting_index, ending_index])
                print(seed_ranges)
                exit()
                continue
            
            sourceKey = keyMap[i - 1]
            destKey = keyMap[i]
            print(f"destKey: {destKey}")
            print(f"sourceKey: {sourceKey}")
            
            content = map[1:]
            
            sources = [seeds[i][sourceKey] for i in seeds.keys()]
            print(f"sources: {sources}")
            
            
            # 3:51am
            for line in content:
                dest_start = int(line.split(" ")[0])
                source_start = int(line.split(" ")[1])
                length = int(line.split(" ")[2])
                for seed_range in seed_ranges:
                    if dest_start >= seed_range[0] and dest_start < seed_range[1]:
                        dest_position = dest_start - seed_range[0]
                        if "num" not in seeds.keys():
                            seeds[dest_start] = {"num": dest_start}
                        
                        
                for z, source in enumerate(sources):
                    if source >= source_start and source < source_start + length:
                        seeds[list(seeds.keys())[z]][destKey] = dest_start + (source - source_start)
            # print()

            print("i == " + str(i))
            
            print()
            # for z, source in enumerate(source_range):
            #     for seed in seeds.keys():
            #         if seeds[seed][destKey] == source:
            #             seeds[seed][sourceKey] = destination_range[z]
                        
            for seed in seeds.keys():
                if destKey not in seeds[seed].keys():
                    seeds[seed][destKey] = seeds[seed][sourceKey]
        
        lowest = seeds[list(seeds.keys())[0]]['loca']
        for seed in seeds.keys():
            if seeds[seed]['loca'] < lowest:
                lowest = seeds[seed]['loca']
        answer = lowest
        
        # print(seeds)
        # dump()
    # print(seeds)
    return answer


# print(part1())
print(part2())
