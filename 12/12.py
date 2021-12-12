import time
from collections import Counter


def find_paths_small_cave_once(edges, cur_path):
    paths = []
    last_node = cur_path[-1]
    possible_next_nodes = [edge[1] for edge in edges if edge[0] == last_node] + \
                          [edge[0] for edge in edges if edge[1] == last_node]
    for node in possible_next_nodes:
        if node == 'end':
            paths.append(cur_path + ['end'])
            continue
        if node.islower() and node not in cur_path:
            paths += find_paths_small_cave_once(edges, cur_path + [node])
            continue
        if node.isupper():
            paths += find_paths_small_cave_once(edges, cur_path + [node])
    return [path for path in paths if path[-1] == 'end']


def find_paths_small_cave_twice(edges, cur_path, has_small_cave_duplicate):
    paths = []
    last_node = cur_path[-1]
    possible_next_nodes = [edge[1] for edge in edges if edge[0] == last_node] + \
                          [edge[0] for edge in edges if edge[1] == last_node]
    for node in possible_next_nodes:
        if node == 'end':
            paths.append(cur_path + ['end'])
            continue
        if node.islower():
            if node == 'start':
                continue
            if node not in cur_path:
                paths += find_paths_small_cave_twice(edges, cur_path + [node], has_small_cave_duplicate)
                continue
            if not has_small_cave_duplicate:
                paths += find_paths_small_cave_twice(edges, cur_path + [node], True)
                continue
        if node.isupper():
            paths += find_paths_small_cave_twice(edges, cur_path + [node], has_small_cave_duplicate)
    return [path for path in paths if path[-1] == 'end']


def main():
    with open("input_12.txt", 'r') as in12:
        lines = [line.strip() for line in in12.readlines()]
    s = time.time()

    edges = [[line.split('-')[0], line.split('-')[1]] for line in lines]
    paths = find_paths_small_cave_once(edges, ['start'])
    print("Part 1:", len(paths))
    paths = find_paths_small_cave_twice(edges, ['start'], False)
    print("Part 2:", len(paths))
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()