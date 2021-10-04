---
layout: post
title:  "Road Network"
date:   2021-10-06 09:38:00 +0200
categories: general python
---

**The Gist:** I was inspired to create a poster that was based on reddit post. I document the process here.

<img src="{{site.url}}/assets/images/road_network_low.png" alt="Road Network">

Some time ago, I came across a [post](https://www.reddit.com/r/dataisbeautiful/comments/lnlkp5/mapping_the_main_roads_of_the_world_oc/) on the subreddt r/dataisbeautiful and liked the aesthetics of the visualization. I thought this would make for a very good poster especially if the location meant something to the owner. Therefore, I started digging into how I could make one for myself. Using data sets form governmental agencies seemed too time consuming. However while I was mindlessly searching the internet, I came across the python library called [OSMNX](https://osmnx.readthedocs.io/en/stable/) that directly accesses data from OpenStreetMap and can fetch the data directly. This seemed to be the method with the least hassle. However installing this package took me quite sometime to figure out mainly because of dependencies. I am not used to working with such libraries. Luckily this [blog](https://geoffboeing.com/2016/11/osmnx-python-street-networks/) post helped me quite a bit. 

```
import osmnx as ox

centerPoint = (12.964398125325351, 77.57567696953713)

place = ox.graph_from_point(centerPoint, dist=20000,
                            network_type='drive')
ox.plot_graph(
    place,
    figsize=(17, 24),
    dpi=400,
    edge_linewidth=0.2,
    bgcolor='#FFFFFF',
    node_color='none',
    edge_color='#FF0000',
    save=True,
    filepath='roadNetwork.png',
    close=True,
    )
```

With this and very few lines of code, I was able to make my own road network image of my favourite city Bengaluru. The first line imports the library. Based on the *centerPoint* and the *dist* variable that decides the radius from the center, the roads that allow for driving are fetched. This is then plotted with a specification of color, quality and size. I then used Canva to add the title and frame and voila. Please note that the code takes some time to run because of the huge amount of data it needs to fetch. I am sure there is a better way to accomplish what I wanted to do. Please do reach out to me using the links in the header if you have any constructive criticism. Thanks!