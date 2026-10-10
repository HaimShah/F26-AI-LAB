import heapq

GRAPH = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)],
         "C": [("G", 3)], "G": []}
H = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
TRUE_REMAINING = {"S": 6, "A": 5, "B": 5, "C": 3, "G": 0}


def search(graph, h, start, goal, verbose=False):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    trace, expanded, stale = [], [], 0
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            stale += 1
            continue
        trace.append(node)
        if verbose:
            frontier = sorted((e[0], e[1], e[2]) for e in pq if e[1] == best[e[2]])
            print(f"  pop {node}: g={g} h={h[node]} f={f}  "
                  f"remaining frontier={[(n, gg, ff) for ff, gg, n in frontier]}")
        if node == goal:
            return {"path": path, "cost": g, "trace": trace,
                    "expanded": expanded, "count": len(expanded), "stale": stale}
        expanded.append(node)
        for nxt, w in graph.get(node, []):
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))
    return None


def path_cost(graph, path):
    total = 0
    for u, v in zip(path, path[1:]):
        total += dict(graph[u])[v]
    return total


def report(name, res, graph=GRAPH):
    print(f"{name}: path={'-'.join(res['path'])} reported_cost={res['cost']} "
          f"summed_cost={path_cost(graph, res['path'])} trace={res['trace']} "
          f"expanded={res['expanded']} count={res['count']} stale_skipped={res['stale']}")


def audit():
    print("Admissibility:")
    for n in H:
        print(f"  {n}: h={H[n]} true={TRUE_REMAINING[n]} ok={H[n] <= TRUE_REMAINING[n]}")
    print("Consistency h(u) <= c(u,v) + h(v):")
    for u, edges in GRAPH.items():
        for v, c in edges:
            print(f"  {u}->{v}: {H[u]} <= {c}+{H[v]}={c + H[v]} ok={H[u] <= c + H[v]}")


if __name__ == "__main__":
    audit()
    print("\nTask 1/2 - A* with supplied heuristic (verbose):")
    astar = search(GRAPH, H, "S", "G", verbose=True)
    report("A*", astar)
    print("\nUCS control (all h = 0):")
    ucs = search(GRAPH, {n: 0 for n in H}, "S", "G", verbose=True)
    report("UCS", ucs)
    print("\nTask 3 - overestimate h(C) 2 -> 10:")
    h2 = dict(H)
    h2["C"] = 10
    over = search(GRAPH, h2, "S", "G", verbose=True)
    report("A* h(C)=10", over)
    print("\nSweep of h(C) (other values unchanged):")
    for val in range(2, 12):
        hh = dict(H)
        hh["C"] = val
        r = search(GRAPH, hh, "S", "G")
        print(f"  h(C)={val:2d}: cost={r['cost']} path={'-'.join(r['path'])} count={r['count']}")
