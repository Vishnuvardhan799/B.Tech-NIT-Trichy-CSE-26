type vertexId = Long

class Edge[ED] (
    val srcId: vertexId,
    val dstId: vertexId,
    val attr: ED
)

class EdgeTriplet[ED,VD] (
    val srcId: vertexId,
    val dstId: vertexId,
    val attr: ED,
    val srcAttr: VD,
    val dstAttr: ED
)

class Graph[VD,ED] {
    def vertices: RDD[(VertexID,VD)]
    def edges: RDD[Edge[ED]]
    def triplets: RDD[EdgeTriplet[VD,ED]]
    
    def subgraph(
        epred: EdgeTriplet[ED,VD] => Boolean,
        vpred: (VertexId,VD) => Boolean
    ):
        Graph[VD, ED]
}

val vertices: RDD[(VertexId, String)] = sc.parallelize(List(
    (1L, "Alice"), (2L, "Bob"), (3L, "Charlie")
))

val edges: EDD[Edge[String]] = sc.parallelize(List(
    Edge(1L, 2L, "Coworker"), Edge(2L, 3L, "Friend")
))

val graph = Graph(vertices, edges)

val subgraph: graph.subgraph(epred = (edge) => edge.attr != "relative")