from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home_page():
    return "<h1>Welcome</h1>"

@app.route('/add-asset')
def add_asset():
    return render_template("add_asset.html")
    
@app.route('/add-asset-entry', methods=['GET','POST'])
def add_asset_entry():
    if request.method == 'POST':
      result = request.form
      asset_id = result["asset-id"]
      asset_name = result["asset-name"]
      asset_details = result["asset-description"]
      conn = sqlite3.connect('udaandb.db')
      try:
          cur = conn.cursor()
          cur.execute("INSERT INTO asset_details (assetID, assetName, assetDetails) VALUES (?,?,?)",(asset_id, asset_name, asset_details))
          conn.commit()
          return "<h1>Asset Details Added Successfully</h1>"
      except Exception as e:
          conn.rollback()
          print(e)
          return "<h1>Error Occured in Insertion</h1>"
      finally:
          conn.close()
      
@app.route('/add-task')
def add_task():
    return render_template("add_task.html")

@app.route('/add-task-entry', methods=['GET','POST'])
def add_task_entry():
    if request.method == 'POST':
      result = request.form
      task_id = result["task-id"]
      task_name = result["task-name"]
      task_details = result["task-description"]
      conn = sqlite3.connect('udaandb.db')
      try:
          cur = conn.cursor()
          cur.execute("INSERT INTO task_details (taskID, taskName, taskDetails) VALUES (?,?,?)",(task_id, task_name, task_details))
          conn.commit()
          return "<h1>Task Details Added Successfully</h1>"
      except Exception as e:
          conn.rollback()
          print(e)
          return "<h1>Error Occured in Insertion</h1>"
      finally:
          conn.close()

@app.route('/add-worker')
def add_worker():
    return render_template("add_worker.html")

@app.route('/add-worker-entry', methods=['GET','POST'])
def add_worker_entry():
    if request.method == 'POST':
      result = request.form
      worker_id = result["worker-id"]
      worker_name = result["worker-name"]
      worker_gender = result["worker-gender"]
      worker_dob = result["worker-dob"]
      worker_designation = result["worker-designation"]
      worker_phone = result["worker-phone"]
      worker_email = result["worker-email"]
      
      conn = sqlite3.connect('udaandb.db')
      try:
          cur = conn.cursor()
          cur.execute("INSERT INTO worker_details (workerId, workerName, workerGender, workerDOB, workerDesignation, workerPhone, workerEmail) VALUES (?,?,?,?,?,?,?)",(worker_id, worker_name, worker_gender, worker_dob, worker_designation, worker_phone, worker_email ))
          conn.commit()
          return "<h1>Worker Details Added Successfully</h1>"
      except Exception as e:
          conn.rollback()
          print(e)
          return "<h1>Error Occured in Insertion</h1>"
      finally:
          conn.close()

@app.route('/assets/all')
def assets_all():
    conn = sqlite3.connect('udaandb.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM asset_details')
    rows = cur.fetchall()
    conn.close()
    return render_template("all_assets.html",rows = rows)

@app.route('/allocate-task')
def allocate_task():
    return render_template("allocate_task.html")

@app.route('/allocate-task-entry', methods=['GET','POST'])
def allocate_task_entry():
    if request.method == 'POST':
      result = request.form
      asset_id = result["asset-id"]
      task_id = result["task-id"]
      worker_id = result["worker-id"]
      time_alloc = result["time-alloc"]
      task_deadline = result["task-deadline"]
      conn = sqlite3.connect('udaandb.db')
      try:
          cur = conn.cursor()
          cur.execute("INSERT INTO allocated_tasks (assetId, taskId, workerId, timeOfAllocation, taskToBePerformedBy) VALUES (?,?,?,?,?)",(asset_id, task_id, worker_id, time_alloc, task_deadline))
          conn.commit()
          return "<h1>Task Allocated Successfully</h1>"
      except Exception as e:
          conn.rollback()
          print(e)
          return "<h1>Error Occured in Insertion</h1>"
      finally:
          conn.close()

@app.route('/get-tasks-for-worker/<workerId>')
def task_for_worker(workerId):
    conn = sqlite3.connect('udaandb.db')
    cur1 = conn.cursor()
    cur1.execute('SELECT taskName FROM task_details where taskID in (SELECT taskID from allocated_tasks WHERE workerID = ?)',(workerId))
    rows = cur1.fetchall()
    
    cur2 = conn.cursor()
    cur2.execute('SELECT workerName FROM worker_details WHERE workerId = ?',(workerId))
    
    temp = cur2.fetchall()
    
    if len(temp) > 0 and len(temp[0]) > 0:
        name = temp[0][0].title()
    else:
        name=""
        return "<h1>Invalid Worker Id</h1>"
    
    conn.close()
    return render_template("task_worker.html",rows=rows,name=name)


if __name__ == '__main__':
   app.run()

