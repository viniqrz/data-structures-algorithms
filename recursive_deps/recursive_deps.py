

def recursive_deps(task):
    
    output = []
    
    def dfs(task):
        name, deps = task
        
        for dep in deps:
            dfs(dep)

        if name not in output:
            output.append(name)

    dfs(task)
    
    return output


task1 = ('A', [])
task2 = ('B', [task1])
task3 = ('C', [task1, task2])
task4 = ('D', [task1, task2, task3])

print(recursive_deps(task3))