from forbiddenfruit import curse



#============================  LIST
def group(self,n):
    return [self[x:x+n] for x in range(0, len(self), n)]

def ungroup(self):
    return [item for sublist in self for item in sublist]


curse(list, "group", group)
curse(list, "ungroup", ungroup)