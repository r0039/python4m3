"""
Just as we learned to insert elements at specific indices, Python gives us a method to remove elements at a specific index using a method called .pop().
"""

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
data_science_topics.pop()
data_science_topics.pop(3)
data_science_topics.pop(-1)
print(data_science_topics)
