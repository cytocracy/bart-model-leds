import CronTab

cron = CronTab(user='pi')
job = cron.new(command='python update.py')
job.second.every(30)

cron.write()

