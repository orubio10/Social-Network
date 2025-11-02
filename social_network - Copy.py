


class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []  

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)



class SocialNetwork:
    def __init__(self):
        self.people = {}  

    def add_person(self, name):
        
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people don't exist.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

      
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")



network = SocialNetwork()

# Add people
network.add_person("Chase")
network.add_person("Marc")
network.add_person("Joseph")
network.add_person("Nate")
network.add_person("Alberto")
network.add_person("Westin")

# Create friendships
network.add_friendship("Chase", "Marc")
network.add_friendship("Chase", "Joseph")
network.add_friendship("Chase", "Nate")
network.add_friendship("Chase", "Alberto")
network.add_friendship("Chase", "Westin")
network.add_friendship("Marc", "Chase")
network.add_friendship("Marc", "Joseph")
network.add_friendship("Joseph", "Chase")
network.add_friendship("Joseph", "Marc")
network.add_friendship("Joseph", "Nate")
network.add_friendship("Joseph", "Alberto")
network.add_friendship("Nate", "Chase")
network.add_friendship("Nate", "Joseph")
network.add_friendship("Alberto", "Chase")
network.add_friendship("Alberto", "Joseph")
network.add_friendship("Alberto", "Westin")
network.add_friendship("Westin", "Chase")
network.add_friendship("Westin", "Alberto")
network.add_friendship("Westin", "Joseph")  


network.add_friendship("Chase", "John")  
network.add_person("Chase")  

print("\n--- Social Network Connections ---")
network.print_network()

""" In this project, I used a graph data structure with an adjacency list to model a social network. Each person is a node, and each friendship is an edge that connects two nodes. Kinda how in real life, friendships are scattered or bidirectional, if one person is friends with another, it goes both ways. Lists or trees wouldn’t work well here, since trees have one-way or top-down relationships, and lists only show one direction.

Using an adjacency list keeps the design simple and memory-efficient, especially since not everyone is friends with everyone else. The dictionary inside the SocialNetwork class acts as a quick lookup for each person, and the friends list stores only real connections instead of all possible ones. This helps make adding people and friendships fast and easy.

One downside I noticed is that while adjacency lists are good for sparse networks, it takes a bit longer to check if two people are already connected. Still, for a social network with many users and fewer mutual friendships, this method works well.

Overall, this structure models how social media platforms store friend connections in a clear, flexible, and realistic way thats easy to expand."""