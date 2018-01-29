# test the current state with the goal
def goal_test(state,goal):
    if (''.join(str(e) for e in state)) == (''.join(str(e) for e in goal)):
        return True
    else: return False


def swap(list,ind1,ind2):
    temp = list[ind1]
    list[ind1] = list[ind2]
    list[ind2] = temp
    return list


def neighbors(state):
    emp = state.index(0)
    li = []

    child1 = swap(state.copy(),emp,(emp+1)%6)
    child2 = swap(state.copy(),emp,(emp-1)%6)

    # if in the middle
    child3 = []

    if emp == 0 or emp == 2 or emp==3 or emp==5 :
      if state[(emp+1)%6] > state[(emp-1)%6]:
          # child2 has priority, child2 is smaller, push child1 first
          return [child1, child2]
      else: return [child2, child1]
    else:
        num_order = [state[(emp+1)%6],state[(emp-1)%6],state[(emp+3)%6]]
        num_order = sorted(num_order)
        ind1 = state.index(num_order[2])
        ind2 = state.index(num_order[1])
        ind3 = state.index(num_order[0])

        child1 = swap(state.copy(), emp, ind1)
        child2 = swap(state.copy(), emp, ind2)
        child3 = swap(state.copy(), emp, ind3)

        li.append(child1)
        li.append(child2)
        li.append(child3)
        # print(li)
        return li


def printsolution(goal,push_order,parent) :
    i = push_order.index(goal)
    li = []

    while i!=-1 :
        li.append(push_order[i])
        # print (path[i])
        i = parent[i]
    # for x in li:
    #     print(x)


    count = 0
    for x in list(reversed(li)):
        print(x)
        count=count+1
    # print(count)



def dfs():
    # initial state and goal state
    initial = [1, 4, 2, 0, 3, 5]
    goal = [0, 1, 2, 3, 4, 5]
    frontier, explored, parent,push_order = [initial],[],[-1],[initial]

    # the reason that it does not print correct value is becoz the time we add explored and the time we add parent is different, maybe use hash
    while frontier:
        state = frontier.pop()
        explored.append(state)

        if goal_test(state,goal):
            printsolution(goal, push_order, parent)
            return explored

        # every time when i push, i record the parent of each node

        parent_index = push_order.index(state.copy())

        # get neighbors , returned value from biggest to smallest
        for neighbor in neighbors(state.copy()):
            if neighbor not in explored:
                push_order.append(neighbor)
                parent.append(parent_index)
                # print(neighbor)
                frontier.append(neighbor)
    return False

# dfs()
# ini = [1,4,0,2,3,5]
# print(neighbors(ini))
dfs()