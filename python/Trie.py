# Trie (Prefix Tree) is a tree like data strucure which is generally used to store words and retrieve. It branches the words based on existing.
# Initiating a tree with hashmap
class TrieNode:
	def __init__(self):
		self.children = {}
		self.endOfWord = False # This end of word is used to denote wheather the word is ended with respect to tree and is useful in search operations

class Trie:
	def __init__(self):
		self.root = TrieNode() # Initializing a empty root

	def insert(self,word):
		cur = self.root

		for ch in word:
			if ch not in cur.children:
				cur.children[ch] = TrieNode()
			cur = cur.children[ch]
		cur.endOfWord = True # Marking the word as ended

	def search(self,word):
		cur = self.root

		for ch in word:
			if ch not in cur.children:
				return False
			cur = cur.children[ch]
		return cur.endOfWord # if the word is not ended it should return false

	def startsWith(self,prefix): # Only check if there is a word that starts with the given word
		cur = self.root

		for ch in prefix:
			if ch not in cur.children:
				return False
			cur = cur.children[ch]
		return True # Same as search but instead return True as we only need to find if the prefix is present.

	def printTrie(self,cur,word = ""):
		for key,value in cur.children.items():
			word = word + key
			if value.endOfWord:
				print(word)
			self.printTrie(value,word)
			word = ""


if __name__ == '__main__':
	trie = Trie()
	trie.insert("apple")
	print(trie.search("apple"))
	print(trie.search("app"))
	print(trie.startsWith("app"))
	trie.insert("app")
	trie.insert("ball")
	print(trie.search("app"))
	trie.printTrie(trie.root)


