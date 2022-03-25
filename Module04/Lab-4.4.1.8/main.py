import os

def find(base, dirToFind):
    data = []
    for dir in os.listdir(base):
        if dir == dirToFind:
            data.append(base+'/'+dir)
        if os.path.isdir(base+'/'+dir):
            data += find(base+'/'+dir, dirToFind)

    return data



for routes in find("./tree", "python"):
    print(routes)