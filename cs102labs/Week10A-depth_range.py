#   Maggie Henry
#  ​ CSCI 102 – Section G
#   Week 10 Lab
#   References: shown below
#   Time: 40 minutes

# Sites I used:
# https://www.w3schools.com/python/python_file_open.asp
# https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place

file_in = open("formations.csv", "r")
file_out = open("formations_parsed.csv", "w")

file_out.write("Depth,Start Depth,End Depth,Average Depth,Formation\n")

for i, line in enumerate(fin):
    if i == 0: 
        pass
    else:
        depth_range = line.split(",")[0]
        name  = line.split(",")[1]
    
        start_depth = float(depth_range.split("-")[0])
        end_depth = float(depth_range.split("-")[1])

        avg_depth = (start_depth + end_depth) / 2
        avg_depth = round(avg_depth, 1)

        line_out = depth_range + "," + str(start_depth) + "," + str(end_depth) + "," + str(avg_depth) + "," + name
        file_out.write(line_out)

