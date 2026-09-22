'''
Activity Selection for meeting scheduling
'''

def select_meeting_activities(activities):

  activities.sort(key=lambda x:(x[2], x[1], x[0]))
  count = 0
  first = True
  last_finish = -1

  result = [
        "Activity Selection Report",
        "Selected Activities",
        "Activity Start Finish Reason"
    ]

  for act_id, start, finish in activities:
    if start >= last_finish:
        if first:
            reason = "Selected first because it finishes earliest"
            first = False
        else:
            reason = "Selected because start time is compatible"

        result.append(f"{act_id} {start} {finish} {reason}")
        last_finish = finish
        count += 1
  result.append(f"Total Selected: {count}")
  result.append("Justification: Greedy selection by earliest finish time maximizes compatible activities")
  
  return result