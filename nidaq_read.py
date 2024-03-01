import nidaqmx as ni
import time

#Create a task to read the thermocouple data
#cDAQ NI9174, Mod2, AI0
with ni.Task() as DAQtask:         #create a task to read the thermocouple data
    DAQtask.ai_channels.add_ai_thrmcpl_chan("cDAQ1Mod2/ai0",name_to_assign_to_channel='TC_CH',thermocouple_type=ni.constants.ThermocoupleType.K,
    cjc_source=ni.constants.CJCSource.BUILT_IN)  #add the thermocouple channel
    DAQtask.start()             #start the task
    try:                        #try to read the data
        tl=time.time()          #get time before data read
        while True:
            data = DAQtask.read(number_of_samples_per_channel=1)   #read the task
            t=time.time()       #time at measurement
            dt=t-tl             #time since last measurement
            print(dt)           #print the delta time
            print(data)         #print the data
            tl=t                #set the last time to the current time for next measurement
            time.sleep(1)       #wait 1 second

    except ni.DaqError as e:    #if there is an error, print the error
        print(e)
    except ni.DaqWarning as w:  #if there is a warning, print the warning
        print(w)
    except KeyboardInterrupt:   #if the user interrupts the program, stop the task
        print("User stopped the program")
    DAQtask.stop()              #stop the task


