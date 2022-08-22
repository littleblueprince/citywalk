
from collections import defaultdict
from heapq import *

def prim(vertexs, edges,start):
    adjacent_dict = defaultdict(list) # 注意：defaultdict(list)必须以list做为变量
    for weight,v1, v2 in edges:
        adjacent_dict[v1].append((weight, v1, v2))
        adjacent_dict[v2].append((weight, v2, v1))
    '''
    经过上述操作，将图转化为以下邻接表形式：
    {'A': [(7, 'A', 'B'), (5, 'A', 'D')], 
     'C': [(8, 'C', 'B'), (5, 'C', 'E')], 
     'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')], 
     'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')], 
     'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')], 
     'G': [(9, 'G', 'E'), (11, 'G', 'F')], 
     'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')]})
    '''
    minu_tree = []  # 存储最小生成树结果
    visited = [start] # 存储访问过的顶点，注意指定起始点
    adjacent_vertexs_edges = adjacent_dict[start]
    heapify(adjacent_vertexs_edges) # 转化为小顶堆，便于找到权重最小的边
    while adjacent_vertexs_edges:
        weight, v1, v2 = heappop(adjacent_vertexs_edges) # 权重最小的边，并同时从堆中删除。
        if v2 not in visited:
            visited.append(v2)  # 在used中有第一选定的点'A'，上面得到了距离A点最近的点'D',举例是5。将'd'追加到used中
            minu_tree.append((weight, v1, v2))
            # 再找与d相邻的点，如果没有在heap中，则应用heappush压入堆内，以加入排序行列
            for next_edge in adjacent_dict[v2]: # 找到v2相邻的边
                if next_edge[2] not in visited: # 如果v2还未被访问过，就加入堆中
                    heappush(adjacent_vertexs_edges, next_edge)
    return minu_tree

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [(7, 'A', 'B'),
         (5, 'A', 'D'),
         (8, 'B', 'C'),
         (9, 'B', 'D'),
         (7, 'B', 'E'),
         (5, 'C', 'E'),
         (15, 'D', 'E'),
         (6, 'D', 'F'),
         (8, 'E', 'F'),
         (9, 'E', 'G'),
         (11, 'F', 'G'),
         ]
print(prim(vertices, edges ,start='D'))




def prim(edges,start):
    minu_tree = []  # 存储最小生成树结果
    visited = [start] # 存储访问过的顶点，注意指定起始点
    adjacent_vertexs_edges = adjacent_dict[start]
    heapify(adjacent_vertexs_edges) # 转化为小顶堆，便于找到权重最小的边
    while adjacent_vertexs_edges:
        weight, v1, v2 = heappop(adjacent_vertexs_edges) # 权重最小的边，并同时从堆中删除。
        if v2 not in visited:
            visited.append(v2)  # 在used中有第一选定的点'A'，上面得到了距离A点最近的点'D',举例是5。将'd'追加到used中
            minu_tree.append((weight, v1, v2))
            # 再找与d相邻的点，如果没有在heap中，则应用heappush压入堆内，以加入排序行列
            for next_edge in adjacent_dict[v2]: # 找到v2相邻的边
                if next_edge[2] not in visited: # 如果v2还未被访问过，就加入堆中
                    heappush(adjacent_vertexs_edges, next_edge)
    return minu_tree
