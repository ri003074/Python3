from data_summarize import WaveData
import time
import os
from icecream import ic
from logging import Formatter
from logging import INFO
from logging import StreamHandler
from logging import getLogger
import win32com
from variables import DATA_GROUP
from variables import DATA_INDEX

from pptx import Presentation


if __name__ == "__main__":
    start = time.time()

    # logging setup
    handler = StreamHandler()
    handler_format = Formatter(
        "%(asctime)s - %(name)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(handler_format)
    handler.setLevel(INFO)
    logger = getLogger("main_9g_sk").getChild("data_summarize")
    logger.setLevel(INFO)
    logger.addHandler(handler)
    logger.propagate = False
    ic.configureOutput(includeContext=True)
    # ic.disable()

    DATA_START_COLUMNS = 10
    FOLDER_PATH = os.getcwd() + "/test_data/"
    PPTX_FILE_NAME = "8GPE_TEST.pptx"

    PE = "8GPE_"
    # PIN_KINDS = ["IO", "WCK", "CK", "CA", "CS"]
    PIN_KINDS = ["IO"]
    pin_kind_for_pptx = "IO"
    PPTX_LIB = "win32com"
    # PPTX_LIB = "python-pptx"

    if PPTX_LIB == "win32com":
        pptx = win32com.client.Dispatch("PowerPoint.Application")
        pptx.Visible = True
        active_presentation_object = pptx.Presentations.Open(
            os.getcwd() + "/advtemplate_mini.pptx"
        )

    else:
        active_presentation_object = Presentation(
            os.getcwd() + "/advtemplate_mini.pptx"
        )

    pkind = "WCK"

    wave_data_overview = WaveData(
        active_presentation=active_presentation_object,
        file_name="io_result_overview.csv",
        folder_path=FOLDER_PATH,
        group_by=DATA_GROUP,
        index=DATA_INDEX,
        pptx_lib=PPTX_LIB,
    )
    wave_data_overview.make_graph(
        df_columns_list=["Frequency"],
        file_name=PE + "Frequency",
        digit_format="%.2f",
        legends={"Frequency": "Freq(GHz)"},
        ax_h_lines=[4.0],
        y_ticks=[0, 6, 1],
        y_label="GHz",
        pin_kind=pin_kind_for_pptx,
        ax_h_lines_per_condition={"IO_Vih1r3V_Vil-0r50V_Vt-0r50V": [2.0, 3.0]},
        y_ticks_per_condition={"CS_Vih1r0V_Vil0r0V_Vt0r5V": [0, 2, 0.2]},
        spec=True,
        additional_information=True,
        info="Spec: less than 60ps (@1.0Vp-p/20% to 80%)",
    )
    # wave_data_overview.add_summary_table_to_pptx(
    #     title="overview_" + pin_kind_for_pptx,
    #     cell_width=[
    #         CELL_WIDTH_BASE_PIN * 1.1,
    #         CELL_WIDTH_BASE_VI * 2.0,
    #         CELL_WIDTH_BASE_RATE * 1.1,
    #         CELL_WIDTH_BASE * 1.1,
    #     ],
    #     items=["Pin", "Vi", "Rate", "Frequency"],
    #     pin_kind=pin_kind_for_pptx,
    # )
    wave_data_overview.make_vix_graph(
        item_name="vix",
        positive_pin_file=FOLDER_PATH
        + "data1/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data1/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        y_ticks=[0, 2, 0.2],
    )
    wave_data_overview.make_vix_graph(
        item_name="vix",
        positive_pin_file=FOLDER_PATH
        + "data1/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data1/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        y_ticks=[0, 2, 0.2],
        reference_level=1.2,
    )
    wave_data_overview.make_vix_graph(
        item_name="vix",
        reference_level=1,
        positive_pin_file=FOLDER_PATH
        + "data2/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data2/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        y_ticks=[0, 2, 0.2],
    )
    wave_data_overview.make_vix_graph(
        item_name="vix",
        reference_level=1,
        positive_pin_file=FOLDER_PATH
        + "data6/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data6/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        y_ticks=[0, 2, 0.2],
    )
    wave_data_overview.make_vix_graph(
        item_name="vix",
        reference_level=1,
        positive_pin_file=FOLDER_PATH
        + "data3/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data3/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        y_ticks=[0, 2, 0.2],
    )
    wave_data_overview.make_differential_waveform(
        item_name=PE + "_" + "differential waveform",
        positive_pin_file=FOLDER_PATH
        + "data1/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data1/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        reference_level=0,
        y_label="V",
        additional_information=True,
        info="Target: less than ±2%, Need double check diff duty value!!!",
    )
    wave_data_overview.make_differential_waveform(
        item_name=PE + "_" + "differential waveform",
        positive_pin_file=FOLDER_PATH
        + "data2/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data2/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        reference_level=0,
        y_label="V",
        additional_information=True,
        y_ticks=[-2, 2, 0.2],
        info="Target: less than ±2%, Need double check diff duty value!!!",
    )
    wave_data_overview.make_differential_waveform(
        item_name=PE + "_" + "differential waveform",
        positive_pin_file=FOLDER_PATH
        + "data3/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data3/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        reference_level=0,
        y_label="V",
        additional_information=True,
        y_ticks=[-2, 2, 0.2],
        info="Target: less than ±2%, Need double check diff duty value!!!",
    )
    wave_data_overview.make_differential_waveform(
        item_name=PE + "_" + "differential waveform",
        positive_pin_file=FOLDER_PATH
        + "data4/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data4/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        reference_level=0,
        y_label="V",
        additional_information=True,
        y_ticks=[-2, 2, 0.2],
        info="Target: less than ±2%, Need double check diff duty value!!!",
    )
    wave_data_overview.make_differential_waveform(
        item_name=PE + "_" + "differential waveform",
        positive_pin_file=FOLDER_PATH
        + "data5/"
        + "P1857A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        negative_pin_file=FOLDER_PATH
        + "data5/"
        + "P1858A1_overview_Vih1r000V_Vil0r000V_Vt0r500V_Rate0r286ns_Duty0r500.txt",
        reference_level=0,
        y_label="V",
        additional_information=True,
        y_ticks=[-2, 2, 0.2],
        info="Target: less than ±2%, Need double check diff duty value!!!",
    )

    wave_data_overview.save_pptx(file_name=PPTX_FILE_NAME, folder_name=FOLDER_PATH)
    elapsed_time = time.time() - start
    print(f"exec time:{elapsed_time:.1f}[sec]")
