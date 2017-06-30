# NextPax - AI_student_group
# JUN 2017

import os
import hashlib
import sys
import glob


def dupCheck(path_prefix, paths, remove="on"):
    """
    Check for duplicates, and optionally remove them

    Input:
    - path_prefix: "root" folder of other paths
    - paths      : list of paths to folders that contain images
    - Remove     : Remove images, on or off

    Output:
    - No return value
    """
    nDups = 0
    total = 0

    for path in paths:
        image_names = os.listdir(path_prefix + "/" + path)
        hash_name_dict = {}

        counter = 0


        name_hash_tuples = [(fname, hashlib.sha256(open(path_prefix + "/" + path + "/"
            + fname, 'rb').read()).digest()) for fname in image_names]

        total += len(name_hash_tuples)

        for name_hash_tuple in name_hash_tuples:
            # total += 1
            (imgname, hash) = name_hash_tuple
            if(hash in hash_name_dict.keys()):
                hash_name_dict[hash] = hash_name_dict[hash] + [imgname]
            else:
                hash_name_dict[hash] = [imgname]

        for key in hash_name_dict.keys():
            if len(hash_name_dict[key]) > 1:
                files = hash_name_dict[key]
                if (remove == 'on'):
                    for i in range(1, len(files)):
                        try:
                            os.remove(path_prefix + "/" + path + "/" + files[i])
                            nDups += 1
                        except:
                            print("Error while removing a duplicate image. Cannot remove", files[i], "at location", path)
                            print("Now exiting the program")
                            os.exit()
                else:
                    counter += 1
                    print(hash_name_dict[key])
                    for i in hash_name_dict[key]:
                        nDups += 1

    print("The total amount of duplicates is", nDups, " out of", total, ".")
    # if (remove == "on"):
    #     print("Removed all duplicates.")
