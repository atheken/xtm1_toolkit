import sys

M1_GCODE_REPLACEMENTS = {
    b'G21': '',  # Switch to millimeter units. M1 is always in millimeter mode
    b'M05': '',
    b'M5': '',

    # Disable laser module. LightBurn uses G1/S0 or G0 for non-laser moves, so disabling serves no purpose.
    b'M4': '',
    b'M04': '',
    b'M3': '',
    b'M03': '',

    # Enabling the laser module serves no purpose because it should always be enabled during a job.
    b'M8': '',  # Start air assist. M1 does not have air assist.
    b'M9': '',  # Stop air assist. M1 does not have air assist.
    b'M114': '',

    # Get current position. Emitted by LightBurn when Framing. Not useful because M1 sends no replies to G-code.
    b'G00 G17 G40 G21 G54': '',  # Strange G-code emitted by LightBurn when Framing
}

LASERBOX_GCODE_REPLACEMENTS = {
    b'M8': 'M19 S1',
    b'M106': 'M4',
    b'M9': 'M19 S0'
}

def read_file(filename):
    with open(filename, 'r') as file:
        file_data = file.read()
    return file_data


def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def replace_text(content, replacements):
    for key in replacements:
        content = content.replace(key, replacements[key])
    return content


def make_replacements(source_file, replacements):
    write_file(source_file + '.replaced', replace_text(read_file(source_file), replacements))


if __name__ == '__main__':
    if len(sys.argv) < 3 or not sys.argv[1].endswith(".gc") and (sys.argv[2] == '-m' or sys.argv[2] == 'l'):
        print("usage: python swap_gcode.py file.gc -m|l")

    if sys.argv[2] == "-m":
        make_replacements(sys.argv[1], M1_GCODE_REPLACEMENTS)
    elif sys.argv[2] == "-l":
        make_replacements(sys.argv[1], LASERBOX_GCODE_REPLACEMENTS)




