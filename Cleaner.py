x = open("Assignment 4 Text File.txt")
file = x.read()
x.close()
file = (file.split("------------------------------------------------------------------------")) #splitting the file
file = file[1:len(file)-1] # removing the first and the last blank lines
name_avg = {}  # a dictionary to count the number occurences of each name

# #--------------------------------------
# #--------------------------------------
# first statistic average occurunces of each name
all_names = []

for i in file:
    a = i.split("|")
    a = a[1]
    if a in name_avg:
        name_avg[a] += 1
    else:
        all_names.append(a)
        name_avg[a] = 1
statistics = open("statistics.txt", "w")
statistics.write("Number of commit objects  = " + str(len(file)) + "\n")
statistics.write("---------------------------------\n")
statistics.write("Average user occurrences\n")
to_sort = []
for i in all_names:
    to_sort.append((name_avg[i] , i) )
to_sort.sort(reverse= True) # # sorting in reverse accoring to the number of contributions

statistics.write("\nNumber of active contributors = " + str(len(to_sort)) + "\n\n")
for i  in to_sort:
    tmp = "Average of " + i[1] + str(i[0] / len(to_sort))
    statistics.write(tmp + "\n")
statistics.write( str("\nMost contributor is " + to_sort[0][1]+"\n") )
# average number of lines for each commit
tot_lines = 0
for i in file:
    tmp = i.split("paths:\n")
    tot_lines += tmp[1].count("\n")-2 # number of lines in each commit
statistics.write("---------------------------------------------------------------")
statistics.write("\n\nAverage number of lines per commit = ")
statistics.write(str(tot_lines/422))
# ----------------------------------
# average commits each month
avg_month = {} # dictionary to count the occurrences of each month

statistics.write("\n---------------------------------------------------------------")
statistics.write("\n\nAverage months \n")
# splitting the commit to get to the month
for i in file:
    # ------ splitting the commit to get to the month
    month  = i.split("|")
    month= month[2].split(",")
    month = month[1].split()
    month = month[1]
    # ------------
    if month in avg_month:
        avg_month[month] += 1
    else:
        avg_month[month] = 1
months = [
'Jan',
'Feb',
'Mar',
'Apr',
'May',
'Jun',
'Jul',
'Aug',
'Sep',
'Oct',
'Nov',
'Dec'
]

for i in months:
    if i in avg_month:
        tmp = "Average occurrences of " + i + " is " + str(avg_month[i] / 12)+ "\n"
    else:
        tmp = "Average occurrences of " + i + " is " + str(0) + "\n"

    statistics.write(tmp)

print("All statistics saved to", statistics.name)
