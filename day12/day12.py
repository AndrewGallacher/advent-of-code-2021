# Day 12

def parse_input(filename):
    paths = {}
 
    input = open(filename, 'r')
      
    for path in input.readlines():
        caves = path.replace('\n', '').strip().split('-')

        if not caves[0] in paths:
            paths[caves[0]] = []
        paths[caves[0]].append(caves[1])

        if not caves[1] in paths:
            paths[caves[1]] = []
        paths[caves[1]].append(caves[0])

    return paths

def find_paths(heads, connections):
    """ TODO """
    #print()
    #print('heads', heads)

    paths = [] 
    for head in heads:

        #print('head', head)

        # Get the specific path we are working on 
        path = head[:]

        # Find its tail
        tail = path.pop()

        # Add it back on
        path.append(tail)
        
        #print('head', head, '- tail', tail, '- path', path)

        # If this path already leads to the end, just add it to the results
        if tail == 'end':
            paths.append(path)
        else:
            # print('tail', tail)
            new_paths = []
            for connection in connections[tail]:
                new_path = path[:]
                if (not connection in new_path) or connection == connection.upper():
                    #print('connection:', connection)
                    new_path.append(connection)
                    new_paths.append(new_path)
                    #print('new_paths', new_paths)

            for new_path in find_paths(new_paths, connections):
                paths.append(new_path)

    return paths

# ------------------------------------

connections = parse_input('test1.txt')
connections = parse_input('test2.txt')
connections = parse_input('input.txt')
print('connections', connections)
print('----------------------------------------------')

paths = find_paths([['start']], connections)

count = 0
for path in paths:
    print(path)
    count += 1

print('Count:', count)
