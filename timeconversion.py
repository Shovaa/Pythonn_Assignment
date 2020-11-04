
# for converting given time in second and converting that into minutes and seconds.
time_insec = float(input("Input time in seconds: "))
minutes = time_insec // 60
sec = time_insec % (24 * 3600)
time_insec %= 60
seconds = time_insec

print("minutes:%d" % (minutes))
print("seconds:%d" % (seconds))