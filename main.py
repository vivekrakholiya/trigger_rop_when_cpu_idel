import psutil
import time
import hou

cpu=0
seconds=0

cpu = int((hou.ui.readInput("Enter CPU Utilixation %", buttons=("OK", "Cancel"), initial_contents='20')[1]))
seconds = int((hou.ui.readInput("Enter After Secounds %", buttons=("OK", "Cancel"), initial_contents='30')[1]))

rop = hou.selectedNodes()[0]



def monitor_cpu(threshold=cpu, duration=seconds, check_interval=1):

    start_time = None
    
    while True:
        cpu_utilization = psutil.cpu_percent(interval=1)

        if cpu_utilization < threshold:
            if start_time is None:
                start_time = time.time()
            elapsed_time = time.time() - start_time

            if elapsed_time >= duration:
                
                break
        else:
            start_time = None
        
        time.sleep(check_interval)

def execute_task():
    r = rop.parm('execute').pressButton()

monitor_cpu()
execute_task()

