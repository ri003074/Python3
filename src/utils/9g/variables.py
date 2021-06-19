CELL_WIDTH_BASE = 72
CELL_WIDTH_BASE_PIN = CELL_WIDTH_BASE * 0.9
CELL_WIDTH_BASE_VI = CELL_WIDTH_BASE * 2
CELL_WIDTH_BASE_RATE = CELL_WIDTH_BASE * 0.9
FREQ_YTICKS = [1.0, 5.0, 0.5]
# DUTY_YTICKS = [40.0, 60.0, 2.5]
DUTY_YTICKS = [41.0, 59.0, 3.0]
TRTF_YTICKS = [30.0, 70.0, 5]
EHEIGHT_YTICS = [350, 450, 20]
EWIDTH_YTICKS = [60, 120, 10]
PWIDTH_YTICKS = [100, 140, 10]
PP_YTICKS = [00, 50, 10]
OVERSHOOT_YTICKS_1V_0V = [-0.35, 0.8499, 0.15]
OVERSHOOT_YTICKS_0r5V_0V = [-0.485, 0.72499, 0.15]
CROSSTALK_YTICKS = [-350, 150, 50]
OVERVIEW_FILE_NAME = "result_overview.csv"
FREQ_DUTY_FILE_NAME = "result_freq_duty.csv"
OVERSHOOT_FILE_NAME = "result_overshoot.csv"
CROSSTALK_FILE_NAME = "result_crosstalk.csv"
EYE_FILE_NAME = "result_eye.csv"
EYE_HEIGHT_FILE_NAME = "result_eye_height.csv"
HISTOGRAM_FILE_NAME = "result_histogram.csv"
JITTER_FILE_NAME = "result_jitter.csv"
PWIDTH_FILE_NAME = "result_pwidth.csv"
TRTF_FILE_NAME = "result_trtf.csv"
VIH_DC_FILE_NAME = "result_vih_dc.csv"
VIL_DC_FILE_NAME = "result_vil_dc.csv"
VIHL_AC_FILE_NAME = "result_vihl_ac.csv"
DATA_GROUP = "Pin_kind_Vi"
DATA_INDEX = "Pin_Rate"


RENAME_CONDITIONS = {
    "Vih0r3V_Vil0r2V_Vt0r2V": "Vih/Vil=0.3V/0.2V",
    "Vih0r300V_Vil0r200V_Vt0r200V": "Vih/Vil=0.3V/0.2V",
    "Vih0r9V_Vil0r2V_Vt0r2V": "Vih/Vil=0.9V/0.2V",
    "Vih0r900V_Vil0r200V_Vt0r200V": "Vih/Vil=0.9V/0.2V",
    "Vih1r5V_Vil0r2V_Vt0r2V": "Vih/Vil=1.5V/0.2V",
    "Vih1r500V_Vil0r200V_Vt0r200V": "Vih/Vil=1.5V/0.2V",
    "Vih2r0V_Vil0r2V_Vt0r2V": "Vih/Vil=2.0V/0.2V",
    "Vih2r000V_Vil0r200V_Vt0r200V": "Vih/Vil=2.0V/0.2V",
    "Vih1r3V_Vil1r2V_Vt1r2V": "Vih/Vil=1.3V/1.2V",
    "Vih1r300V_Vil1r200V_Vt1r200V": "Vih/Vil=1.3V/1.2V",
    "Vih1r3V_Vil0r240V_Vt0r240V": "Vih/Vil=1.3V/0.24V",
    "Vih1r300V_Vil0r240V_Vt0r240V": "Vih/Vil=1.3V/0.24V",
    "Vih1r3V_Vil-0r05V_Vt-0r05V": "Vih/Vil=1.3V/-0.05V",
    "Vih1r300V_Vil-0r05V_Vt-0r05V": "Vih/Vil=1.3V/-0.05V",
    "Vih1r3V_Vil-0r50V_Vt-0r50V": "Vih/Vil=1.3V/-0.5V",
    "Vih1r300V_Vil-0r50V_Vt-0r50V": "Vih/Vil=1.3V/-0.5V",
    "Vih1r0V_Vil0r0V_Vt0r0V": "Vih/Vil=1.0V/0.0V",
    "Vih1r000V_Vil0r000V_Vt0r000V": "Vih/Vil=1.0V/0.0V",
    "Vih0r5V_Vil0r0V_Vt0r0V": "Vih/Vil=0.5V/0.0V",
    "Vih0r500V_Vil0r000V_Vt0r000V": "Vih/Vil=0.5V/0.0V",
    "Rate0r250ns": "Rate250ps",
    "Rate0r286ns": "Rate286ps",
    "Rate0r222ns": "Rate222ps",
    "Duty0r500": "",
    "vihl": "Vihl",
    "trtf": "TrTf",
    "freq": "Freq",
    "duty": "Duty",
    "jitter": "Jitter",
    "pwidth": "Pwidth",
    "overshoot": "Overshoot",
    "crosstalk": "Crosstalk",
    "eye": "Eye",
    "height": "Height",
    "_": " ",
}
