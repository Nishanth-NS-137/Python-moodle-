def count_pairs(activities, k):
    activity_count = {}
    pairs_count = 0
    
    # Count the occurrences of each activity
    for activity in activities:
        if activity in activity_count:
            activity_count[activity] += 1
        else:
            activity_count[activity] = 1
    
    # Iterate through the activities and check for pairs
    for activity in activities:
        if k == 0:
            # For k=0, count occurrences where there are at least 2 of the same activity
            if activity_count[activity] >= 2:
                pairs_count += 1
                activity_count[activity] -= 2
        else:
            # Check if activity + k exists in the hash map
            if activity + k in activity_count:
                pairs_count += activity_count[activity + k]
            # Check if activity - k exists in the hash map
            if activity - k in activity_count:
                pairs_count += activity_count[activity - k]
        
        # Decrement the count of the current activity
        activity_count[activity] -= 1
    
    return pairs_count

# Input handling
n = int(input())
activities = list(map(int, input().split()))
k = int(input())

# Output the result
print(count_pairs(activities, k))
