# Subdomain Click Counts (String Parsing & Hash Maps)

# Difficulty: Medium (Typical CodeSignal Q2/Q3).

# Problem: You are given an array of strings cpdomains where each string represents a count and a domain name separated by a space (e.g., "900 google.com"). 
# A click on a subdomain (like mail.google.com) also counts as a click for all parent domains (google.com and com).
# Return an array of the aggregated click counts for all subdomains and parent domains.

# Input: cpdomains = ["900 google.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

# Output: ["901 com", "900 google.com", "50 yahoo.com", "1 intel.mail.com", "1 mail.com", "5 org", "5 wiki.org"] (Order does not matter).

## SOLUTION

## We have a tree of domains:
#              com _______mail.com
#            /     \        
#   (900) google.com  yahoo.com   (1)
#         /
#  (2)   mail.google.com

# our goal is to basically traverse through the multiple trees
# summing up all the values in each node and returning back to the parent
# order of traversal doesn't matter, we must stack weights of node
# we can either perform BFS or DFS

# 1) we can build the tree from list of strings using:

# option A) a hashmap * (let's pick hashmap as our first approach!)
# option B) a node class
# option C) edge list

# 2) in order to convert strings of list into a hashmap, we must iterate, split
# every string by a '.' character, then iterate through each of the domains while
# inserting into tree with their number of clicks

def solution(cpdomains):
    # 900 google.com

    tree = {}

    for cpdomain in cpdomains:
        weight = int(cpdomain.split(' ')[0])
        domain = cpdomain.split(' ')[1]

        subdomains = domain.split('.')

        subdomain = ''

        for index in reversed(range(len(subdomains))):
            subdomain = subdomains[index] + ('.' + subdomain if subdomain else '')
            tree[subdomain] = (tree.get(subdomain) or 0) + weight

    print(tree)

    return None


solution(["900 google.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])