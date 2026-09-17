class Heavyhex(Layout):
    def __init__(self):
        super().__init__()


    graph = Graph() #make a heavy hex graph
    # Add nodes and edges to form the heavy hex structure
    # Example (replace with actual heavy hex structure):
    for i in range(6):
        graph.add_node(f"Q{i}")
    graph.add_edge(("Q0", "Q1"))
    graph.add_edge(("Q1", "Q2"))
    graph.add_edge(("Q2", "Q3"))
    graph.add_edge(("Q3", "Q4"))
    graph.add_edge(("Q4", "Q5"))
    graph.add_edge(("Q5", "Q0"))




