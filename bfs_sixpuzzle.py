# my_list = [1,2,2]
# print (my_list)
# print (my_list.index(2))
# str1 = ''.join(list1)


def compare_state(initial, goal):
    if (''.join(str(e) for e in initial)) == (''.join(str(e) for e in goal)) : return True
    else: return False


def list_tostring(my_list):
    return ''.join(str(e) for e in my_list)


def swap(list,ind1,ind2):
    temp = list[ind1]
    list[ind1] = list[ind2]
    list[ind2] = temp
    return list


def order_state2(state,ind0,ind1,ind2,queue,visited,path,parent):
    child1 = state.copy()
    swap(child1, ind0, ind1)
    child2 = state.copy()
    swap(child2, ind0, ind2)

    parent_index = path.index(state)
    if state[ind1] < state[ind2]:
        # add child1 to queue
        if list_tostring(child1) not in visited:
            queue.append(child1)
            parent.append(parent_index)
        if list_tostring(child2) not in visited:
            queue.append(child2)
            parent.append(parent_index)
    else:
        if list_tostring(child2) not in visited:
            queue.append(child2)
            parent.append(parent_index)
        if list_tostring(child1) not in visited:
            queue.append(child1)
            parent.append(parent_index)

    return queue


def order_state3(temp_state,ind0,ind1,ind2,ind3,queue,visited,path,parent) :
    child1 = temp_state.copy()
    child2 = temp_state.copy()
    child3 = temp_state.copy()
    swap(child1, ind1, ind0)
    swap(child2, ind2, ind0)
    swap(child3, ind3, ind0)

    parent_index = path.index(temp_state)
    minv=min(temp_state[ind1], temp_state[ind2], temp_state[ind3])
    if minv == temp_state[ind1]:
        if list_tostring(child1) not in visited:
            queue.append(child1)
            parent.append(parent_index)
        if temp_state[ind2] < temp_state[ind3]:
            if list_tostring(child2) not in visited:
                queue.append(child2)
                parent.append(parent_index)
            if list_tostring(child3) not in visited:
                queue.append(child3)
                parent.append(parent_index)
        else:
            if list_tostring(child3) not in visited:
                queue.append(child3)
                parent.append(parent_index)
            if list_tostring(child2) not in visited:
                queue.append(child2)
                parent.append(parent_index)
    elif minv == temp_state[ind2]:
        if list_tostring(child2) not in visited:
            queue.append(child2)
            parent.append(parent_index)
        if temp_state[ind1] < temp_state[ind3]:
            if list_tostring(child1) not in visited:
                queue.append(child1)
                parent.append(parent_index)
            if list_tostring(child3) not in visited:
                queue.append(child3)
                parent.append(parent_index)
        else:
            if list_tostring(child3) not in visited:
                queue.append(child3)
                parent.append(parent_index)
            if list_tostring(child1) not in visited:
                queue.append(child1)
                parent.append(parent_index)
    elif minv == temp_state[ind3]:
        if list_tostring(child3) not in visited:
            queue.append(child3)
            parent.append(parent_index)
        if temp_state[ind1] < temp_state[ind2]:
            if list_tostring(child1) not in visited:
                queue.append(child1)
                parent.append(parent_index)
            if list_tostring(child2) not in visited:
                queue.append(child2)
                parent.append(parent_index)
        else:
            if list_tostring(child2) not in visited:
                queue.append(child2)
                parent.append(parent_index)
            if list_tostring(child1) not in visited:
                queue.append(child1)
                parent.append(parent_index)
    return queue

# record parent in parent[] when enqueue, index in path and parent are consistent
def printsolution(goal,path,parent) :
    i = path.index(goal)
    li = []
    while i!=-1 :
        li.append(path[i])
        # print (path[i])
        i = parent[i]
    for x in list(reversed(li)):
        print(x)


def bfs():
    initial = [1,4,2,0,3,5]
    goal = [0,1,2,3,4,5]
    # initial = [1,0,2,3,4,5]
    visited, queue, path, parent = [],[initial], [],[]
    if compare_state(initial,goal) == True :return [initial]
    queue.append(initial)
    parent.append(-1)
    while queue:
        temp_state = queue.pop(0)
        if compare_state(temp_state,goal) :
            path.append(temp_state)
            printsolution(goal,path,parent)
            return path
        if list_tostring(temp_state) not in visited :
            visited.append(list_tostring(temp_state))
            path.append(temp_state)

            index_empty_cell = temp_state.index(0)
            if index_empty_cell==0:
                queue = order_state2(temp_state,0,5,1,queue,visited,path,parent)
            elif index_empty_cell==1 :
                queue = order_state3(temp_state,1,0,4,2,queue,visited,path,parent)
            elif index_empty_cell==2:
                queue = order_state2(temp_state,2,1,3,queue,visited,path,parent)
            elif index_empty_cell==3:
                queue = order_state2(temp_state,3,2,4,queue,visited,path,parent)
            elif index_empty_cell==4:
                queue = order_state3(temp_state,4,5,1,3,queue,visited,path,parent)
            elif index_empty_cell==5:
                queue = order_state2(temp_state,5,0,4,queue,visited,path,parent)
    return ['failed']


l = bfs()
# for x in l:
#     print (x)
