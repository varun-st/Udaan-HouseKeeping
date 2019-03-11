import sqlite3

conn = sqlite3.connect('udaandb.db')

"""
conn.execute('CREATE TABLE asset_details(assetId TEXT PRIMARY KEY, assetName TEXT, assetDetails TEXT)')
print("Asset Details Table created successfully")

conn.execute('CREATE TABLE task_details(taskId TEXT PRIMARY KEY, taskName TEXT, taskDetails TEXT)')
print("Task Details Table created successfully")

conn.execute('CREATE TABLE worker_details(workerId TEXT PRIMARY KEY, workerName TEXT, workerGender TEXT,workerDOB TEXT , workerDesignation TEXT, workerPhone TEXT, workerEmail TEXT)')
print("Worker Details Table created successfully")

conn.execute('CREATE TABLE allocated_tasks (assetId TEXT PRIMARY KEY, taskId TEXT, workerId TEXT, timeOfAllocation TEXT, taskToBePerformedBy TEXT, FOREIGN KEY (assetId) REFERENCES asset_details(assetId), FOREIGN KEY (taskId) REFERENCES task_details(taskId), FOREIGN KEY (workerId) REFERENCES worker_details(workerId))')
print("Allocated Tasks Table created successfully") """

"""
conn.execute('DROP TABLE asset_details')
conn.execute('DROP TABLE task_details')
conn.execute('DROP TABLE worker_details')
conn.execute('DROP TABLE allocated_tasks')"""

"""
conn.execute('DELETE FROM asset_details')
conn.execute('DELETE FROM task_details')
conn.execute('DELETE FROM worker_details')
conn.execute('DELETE FROM allocated_tasks')

conn.commit()"""

cur1 = conn.cursor()
cur1.execute('select * from asset_details')
rows = cur1.fetchall()
print(rows)

cur2 = conn.cursor()
cur2.execute('select * from task_details')
rows = cur2.fetchall()
print(rows)

cur3 = conn.cursor()
cur3.execute('select * from worker_details')
rows = cur3.fetchall()
print(rows)

cur4 = conn.cursor()
cur4.execute('select * from allocated_tasks')
rows = cur4.fetchall()
print(rows)


conn.close()

