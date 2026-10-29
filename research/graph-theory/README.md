# Layered DAGs

 - an ordered layered DAG naturally induces a strict partial ordering on its set of vertices
 - a DAG and a partial order are structurally equivalent
 - a DAG defines a poset (partially ordered set)
 - any finite poset can be represented as a DAG

## Partial Ordering

 - a DAG consists of a set of vertices V and directed edges E
 - define a binary relation \(\prec \) on the vertices based on reachability:
    - \(u \prec v\) iff there exists a directed edge from u to v
 - this relation satisfies the three axioms of a strict partial order:
    - irreflexivity: \(u\not{\prec }u\) 
    - asymmetry: if \(u \prec v\), then \(v\not{\prec }u\) 
    - transitivity: if \(u \prec v\) and \(v \prec w\), then \(u \prec w\) 

## Layered DAGs

 - vertices are partitioned into discrete, ordered subsets called layers (\(L_1, L_2, \dots, L_k\))
 - edges from layer \(L_{i}\) to layer \(L_{i+1}\) (or to any \(L_{j}\) where j > i)
 - this guarantees a coarser, structural partial ordering based purely on the layers

## Ordered DAGs

 - when a layered DAG is ordered, it usually implies two things depending on the context:
    - total order of layers - \(L_1 \prec L_2 \prec \dots \prec L_k\)
    - intra-layer ordering
