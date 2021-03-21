import re
import sys
from shm_condition_data import default_data_before_scanconditioon
from shm_condition_data import default_data_after_scanconditioon
from shm_condition_data import shmoo_conditions

for shmoo_condition in shmoo_conditions:
    f = open(shmoo_condition + ".txt", "w")
    f.write(default_data_before_scanconditioon)
    for axis in shmoo_conditions[shmoo_condition]:
        if axis == "yscancond" or axis == "xscancond":
            f.write("<{0}>\n".format(axis))

        step = 0
        for param in shmoo_conditions[shmoo_condition][axis]:
            step = shmoo_conditions[shmoo_condition][axis]["step"]
            # print(step)
            if param == "step":
                f.write(
                    "{0}<step>{1}</step>\n".format(
                        " " * 4, shmoo_conditions[shmoo_condition][axis][param]
                    )
                )
                step = float(shmoo_conditions[shmoo_condition][axis][param])
            elif param == "displayvalue":
                f.write("{0}<{1}>\n".format(" " * 4, param))
                f.write(
                    "{0}<unit>{1}</unit>\n".format(
                        " " * 8, shmoo_conditions[shmoo_condition][axis][param][0]
                    )
                )
                f.write(
                    "{0}<start>{1}</start>\n".format(
                        " " * 8, shmoo_conditions[shmoo_condition][axis][param][1]
                    )
                )
                f.write(
                    "{0}<index>{1}</index>\n".format(
                        " " * 8, shmoo_conditions[shmoo_condition][axis][param][2]
                    )
                )
                f.write(
                    "{0}<stop>{1}</stop>\n".format(
                        " " * 8, shmoo_conditions[shmoo_condition][axis][param][3]
                    )
                )
                f.write("{0}</{1}>\n".format(" " * 4, param))

                start_num = re.sub(
                    "[a-zA-Z]", "", shmoo_conditions[shmoo_condition][axis][param][1]
                )
                index_num = re.sub(
                    "[a-zA-Z]", "", shmoo_conditions[shmoo_condition][axis][param][2]
                )
                stop_num = re.sub(
                    "[a-zA-Z]", "", shmoo_conditions[shmoo_condition][axis][param][3]
                )
                if (float(start_num) + float(stop_num)) / float(index_num) != step:
                    print "{0} {1} step error!!!".format(shmoo_condition, axis)
                    sys.exit()

            elif param == "scandata":
                for index, data in enumerate(
                    shmoo_conditions[shmoo_condition][axis][param]
                ):
                    f.write("{0}<{1}>\n".format(" " * 4, param))
                    f.write("{0}<datanum>{1}</datanum>\n".format(" " * 8, index))
                    f.write("{0}<unit>{1}</unit>\n".format(" " * 8, data[0]))
                    f.write("{0}<func>{1}</func>\n".format(" " * 8, data[1]))
                    f.write("{0}<start>{1}</start>\n".format(" " * 8, data[2]))
                    f.write("{0}<index>{1}</index>\n".format(" " * 8, data[3]))
                    f.write("{0}<stop>{1}</stop>\n".format(" " * 8, data[4]))
                    f.write("{0}<chkbtn>{1}</chkbtn>\n".format(" " * 8, "TRUE"))
                    f.write("{0}</{1}>\n".format(" " * 4, param))

                start_num = re.sub(
                    "[a-zA-Z]", "", data[2]
                )
                index_num = re.sub(
                    "[a-zA-Z]", "", data[3]
                )
                stop_num = re.sub(
                    "[a-zA-Z]", "", data[4]
                )
                if (float(start_num) + float(stop_num)) / float(index_num) != step:
                    print "{0} {1} step error!!!".format(shmoo_condition, axis)
                    sys.exit()

        if axis == "yscancond" or axis == "xscancond":
            f.write("</{0}>\n".format(axis))

    f.write(default_data_after_scanconditioon)
    f.close()
