import osmnx as ox
place = ox.graph_from_point((12.964398125325351, 77.57567696953713), dist=20000, network_type='drive')
ox.plot_graph(place, figsize=(17, 24), dpi=400, edge_linewidth=0.2, bgcolor='#FFFFFF', node_color='none', edge_color='#FF0000', save=True, filepath='test.png', close=True)