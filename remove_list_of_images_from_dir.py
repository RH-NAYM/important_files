import os
main_list = os.listdir("images") # list of main dir where all images and labels
old_del_list = os.listdir("xx") # list of dir of jfif and JPE

updated_del_list = []


# update del list to broken file
for new_item in old_del_list:
    if ".jfif" in new_item:
        n = new_item.replace(".jfif",".txt")
    elif ".JPE" in new_item:
        n = new_item.replace(".JPE",".txt")
    updated_del_list.append[n]



# del all broken items
for item in updated_del_list:
    if item in main_list:
        os.remove(f"images/{item}")
