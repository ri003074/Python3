default_data_before_scanconditioon = """
aaaaa
aaaaa
aaaaa
aaaaa
"""

default_data_after_scanconditioon = """
bbbb
bbbb
bbbb
bbbb
"""

shmoo_conditions = {
    "cond1": {
        "yscancond": {
            "step": 10,
            "displayvalue": ["voh1", "0.0mV", "2mV", "20.0mV"],
            "scandata": [
                ["voh1", "voh1", "0.0mV", "2mV", "20mV"],
                ["vol1", "vol1", "0.0mV", "2mV", "20.0mV"],
            ],
        },
        "xscancond": {
            "step": 10,
            "displayvalue": ["vih2", "0.0mV", "2mV", "20mV"],
            "scandata": [
                ["vih2", "vih2", "0.0mV", "2mV", "20mV"],
                ["vil2", "vil2", "0.0mV", "2mV", "20mV"],
                ["vtt", "vtt", "1.0mV", "3mV", "29mV"],
            ],
        },
    },
    "cond2": {
        "yscancond": {
            "step": 10,
            "displayvalue": ["voh1", "0.0mV", "2mV", "20mV"],
            "scandata": [
                ["voh1", "voh1", "0.0mV", "2mV", "20mV"],
                ["vol1", "vol1", "0.0mV", "2mV", "20mV"],
            ],
        },
        "xscancond": {
            "step": 10,
            "displayvalue": ["vih2", "0.0mV", "2mV", "20mV"],
            "scandata": [
                ["vih2", "vih2", "0.0mV", "2mV", "20mV"],
                ["vil2", "vil2", "0.0mV", "2mV", "20mV"],
            ],
        },
    },
}
