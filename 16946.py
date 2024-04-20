
def bfs(map, start_node):
    visit = []
    queue = []
    
    queue.append(start_node)
    
    while queue:
        node = queue.pop()
        if node in visit:
            continue
        
        # if not wall and close
        queue.append(map[node])
            
    return visit