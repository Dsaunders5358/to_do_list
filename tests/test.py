def strike(text):
    return text + u'\u2713'

print(strike("Testing A sentence to see what happens"))
#update test
#notes to self, have every string end with some characters aka dn or pr and have the propram read that to decide what state the task on the list is. Could possible add a date to the list to keep track of dates so we can then persist completed task and track how many completed per month etc