# • Input String (s): "catsandog"
# • Dictionary (wordDict): ["cats", "dog", "sand", "and", "cat"]


def wordBreak(text: str, dic: list):

  tree = {}

  currNode = tree

  for word in dic:
    for i in range(len(word)):
      currNode[word[i]] = {
        'end': True if (currNode.get(word[i]) and currNode.get(word[i]).get('end'))
          or (i == len(word) - 1)
        else False
      }
      currNode = currNode[word[i]]

  print(tree)

  def dfs(currNode, word, i):
    # if not currNode:
      # raise Exception

    print('\n')
    print(currNode,word, i, word[i])

    if i + 1 > len(word) - 1:
      return currNode.get(word[i]).get('end')

    if currNode.get(word[i]).get('end'):
      currNode = tree
      return dfs(currNode, word, i+1)
    else:
      return dfs(currNode[word[i]], word, i+1)

  # try:
  currNode = tree
  dfs(currNode, text, 0)
  return True
  # except Exception:
  #   print(Exception.args)
  #   return False

print(wordBreak("catsand", ["cats", "dog", "sand", "and", "cat"]))