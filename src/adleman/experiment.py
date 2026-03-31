from graphs import create_vertex_strands, complement_strands, create_edge_strands, create_paths

import random


VERTS  = 7
LENGTH = 20
FACTOR = 100000
EDGES  = [
    (0, 1), (0, 3), (0, 6),
    (1, 2), (1, 3),
    (2, 1), (2, 3),
    (3, 2), (3, 4),
    (4, 1), (4, 5),
    (5, 1), (5, 2), (5, 6)
]


def main() -> None:
    print("\n")
    print("\tA Simulation of Adleman's Experiiment:")
    print("\n")
    print(f"  Original Vertices: {', '.join(str(i) for i in range(VERTS))}")
    print(f"     Original Edges: {', '.join(f"{i} -> {j}" for (i, j) in EDGES)}")
    print("\n")

    v_strands = create_vertex_strands(LENGTH, VERTS)
    c_strands = complement_strands(v_strands)
    e_strands = create_edge_strands(c_strands, EDGES, LENGTH)
    print(f"   Encoded Vertices: {', '.join(v_strands)}")
    print(f"        Complements: {', '.join(c_strands)}")
    print(f"      Encoded Edges: {', '.join(e_strands)}")
    print("\n")

    # Step 1: Create paths based on edges
    #         NOTE: exclude the first strand - which will be passed to 'create_paths'
    a_strands = v_strands[1:] * FACTOR
    random.shuffle(a_strands)
    paths = create_paths(a_strands, e_strands, v_strands[0], v_strands[-1], LENGTH)
    print(f"             Step 1: {len(paths):5d} Paths Found")

    # Step 2: Retain paths that begin and end with the start and end vertices
    #         NOTE: we don't need to check for the in and out - we use both in 'create_paths'
    paths = [path for path in paths if path[0] == v_strands[0] and path[-1] == v_strands[-1]]
    print(f"             Step 2: {len(paths):5d} Paths Found")

    # Step 3: Retain paths that contain the correct number of vertices
    paths = [path for path in paths if len(path) == VERTS]
    print(f"             Step 3: {len(paths):5d} Paths Found")

    # Step 4: Retain paths that include all vertices
    s_strands = set(v_strands)
    paths = [path for path in paths if set(path) == s_strands]
    print(f"             Step 4: {len(paths):5d} Paths Found")

    # Step 5: If paths exist then 'Yes' or else 'No'
    found = len(paths) > 0
    print(f"             Step 5: {'Yes' if found else 'No'}")
    print("\n")

    if found:
        print(f" Encoded Path Found: {' -> '.join(paths[0])}")
        print(f"         Path Found: {' -> '.join([str(v_strands.index(p)) for p in paths[0]])}")
        print("\n")
