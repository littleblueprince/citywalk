import numpy as np
j=7
# ①构建地图
mapping_list = [[np.inf for i in range(0, j)] for i in range(0, j)]  # 构建全是无穷大的二维列表
for i in range(0, j):
    mapping_list[i][i] = 0  # 对角线处的值为0

mapping_list[0][1] = 2
mapping_list[0][2] = 3
mapping_list[0][3] = 1
mapping_list[1][4] = 2
mapping_list[2][3] = 1
mapping_list[2][4] = 1
mapping_list[2][5] = 1
mapping_list[3][5] = 3
mapping_list[4][5] = 2
mapping_list[5][6] = 2
mapping_list[1][0] = 2
mapping_list[2][0] = 3
mapping_list[3][0] = 1
mapping_list[3][2] = 1
mapping_list[4][1] = 2
mapping_list[4][2] = 1
mapping_list[4][6] = 1
mapping_list[5][2] = 1
mapping_list[5][3] = 3
mapping_list[5][4] = 2
mapping_list[6][5] = 2
mapping_list[6][4] = 1

mapping_list = np.array(mapping_list)  # 将mapping_list转换成数组形式
# print(mapping_list)
# ② 初始化
node_cost = [[np.inf for i in range(0, 3)] for i in range(0, 7)]  # 构建全是无穷大的二维列表
# arr这个数组用来表示每个节点的[节点名 node_cost 父节点]
for i in range(0, 7):
    node_cost[i][0] = i
# 计算A点与它相邻的节点，更新其node_cost和父节点,并且将A点放入close_list里面
node0 = 0
close_list = []
for i in range(0, 7):
    if mapping_list[int(node0)][i] < node_cost[i][1]:
        node_cost[i][2] = node0
        node_cost[i][1] = mapping_list[int(node0)][i]
close_list.append(int(node0))


# ③ 构建一系列函数以实现迭代功能

# 1、构建函数用来选择node_cost最小的节点
# 选择node_cost值最小的节点->node 0
def choose_min(node_cost, close_list):
    node_cost = np.array(node_cost)  # 将node_cost从list转换成array
    open_list = list(set(node_cost[:, 0].tolist()) - set(close_list))  # 建立一个open_list放入没有被遍历的点
    final_list = []
    for i in open_list:
        final_list.append(node_cost[int(i)].tolist())
    final_list = np.array(final_list)  # final_list转换成array，才可以利用np.where找最小值
    node0 = final_list[np.where(final_list[:, 1] == final_list[:, 1].min())][0][0]  # 将node_cost最小的点的节点名给node0
    return int(node0)


# -------------------------------------------------------------------------------------------------------
# 2、构建count_cost函数用来计算相邻节点的node_cost
# 计算node0邻节点的node_cost，此时的node_cost值就是地图上的代价值加上父节点的代价值，如果已经比原来小则更新node_cost和父节点
# 并将node0放入close_list里面
def count_cost(mapping_list, node_cost, close_list):
    for i in range(0, 7):
        if mapping_list[node0][i] + node_cost[node0][1] < node_cost[i][1]:
            node_cost[i][2] = node0
            node_cost[i][1] = mapping_list[node0][i] + node_cost[node0][1]
    close_list.append(node0)
    return [node_cost, close_list]


# ④ 开始迭代----->迭代中止的条件：终点在close_list里面
while 6 not in close_list:
    node0 = choose_min(node_cost, close_list)  # 找node_cost最小的节点
    [node_cost, close_list] = count_cost(mapping_list, node_cost, close_list)  # 计算邻节点
    # print(close_list)
xn = 6
x0 = 0
destination_list = [xn]
print("最短的路径代价为:", node_cost[xn][1])
while x0 not in destination_list:
    xn = node_cost[xn][2]
    destination_list.append(xn)
print("最短路径为：", destination_list)