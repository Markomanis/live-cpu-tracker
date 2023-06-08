import psutil
import math
import speedtest

print(psutil.cpu_count())
# while(1):
#     print(psutil.cpu_percent(1))
print("Total system memory is: ",math.floor(psutil.virtual_memory()[0]/1000000000), "Gb")
print("Available memory is: ",math.floor(psutil.virtual_memory()[1]/1000000000), "Gb")
print("Percent memory used is: ",psutil.virtual_memory()[2], "Gb")
print("Used memory is: ",math.floor(psutil.virtual_memory()[3]/1000000000), "Gb")
print("Free memory is: ",math.floor(psutil.virtual_memory()[4]/1000000000), "Gb")

# Network speed:
st = speedtest.Speedtest()
print("Download speed: ",math.floor(st.download()/1000000), "Mb/s")
print("Upload speed: ",math.floor(st.upload()/1000000), "Mb/s")
print("Ping is: ", st.results.ping)