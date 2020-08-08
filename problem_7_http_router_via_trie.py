"""
"""

#####################
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, path, handler=None):
        # Initialize the node with children as before, plus a handler
        self.path = path
        self.children = {}
        self.handler = handler

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode(path_part)

#####################
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, path, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(path, handler)

    def insert(self, split_path, path_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for part in split_path:
            node.insert(part)
            node = node.children[part]
        # insert handler at the end
        node.handler = path_handler

    def find(self, split_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for part in split_path:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler



#####################
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie('/', root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        split_path = self.split_path(path)
        self.route.insert(split_path, path_handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        split_path = self.split_path(path)
        parts_found = self.route.find(split_path)
        if parts_found is None:
            return self.not_found_handler
        return parts_found

    def split_path(self, path=''):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        split_path = path.rstrip('/').split('/')[1:]
        return split_path

#####################
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# test cases
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one