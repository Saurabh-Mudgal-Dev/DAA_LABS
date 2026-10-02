'''
Job Scheduling system
'''

def job_sequencing_deadlines(jobs):

  jobs = sorted(jobs, key = lambda x: (-x[2], x[1], x[0]))
  max_deadline = max(job[1] for job in jobs) if jobs else 0
  slots = [None]*(max_deadline+1)
  total_profit = 0
  total_jobs = 0
  for job_id, deadline, profit in jobs:
    for slot in range(deadline, 0, -1):
      if slots[slot] is None:
        slots[slot] = (job_id, profit)
        total_profit += profit
        total_jobs += 1
        break
  lines = []
  lines.append("Job Sequencing Report")
  lines.append("Scheduled Jobs")
  lines.append("Slot Job Profit")
  for slot in range(1, max_deadline+1):
    if slots[slot] is not None:
      job_id, profit = slots[slot]
      lines.append(f"{slot} {job_id} {profit}")
  lines.append(f"Total Jobs Scheduled: {total_jobs}")
  lines.append(f"Total Profit: {total_profit}")
  lines.append("Strategy: Schedule highest profit jobs before their deadlines")
  
  return lines