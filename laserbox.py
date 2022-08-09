import sys

replacements = {
  'G21': '',  # mm coordinates
  'G90': '',  # absolute coordinates
  'M8': '',  # air assist on
  'M05': 'M4 S0',  # laser off
  'M03': 'M4',  # laser on
  'M9': '',  # air assist off
  'X': 'X-',  # negate x coordinates
  'Y': 'Y-',  # negate y coordinates
  'Z': 'Z-'  # negate z coordinates
}


def read_file(filename):
  with open(filename, 'r') as file:
    file_data = file.read()
  return file_data


def write_file(filename, data):
  with open(filename, 'w') as file:
    file.write(data)


def replace_text(content, replace):
  for key in replace:
    content = content.replace(key, replace[key])
  return content


def to_fixed(content):
  """
  Laserbox software sends all floating point values padded to 3 decimal places.
  This may not be necessary
  """
  return content


def set_height(content, thickness):
  thickness = float(thickness)
  height = 21 - thickness
  content = replace_text(content, {
    ";USER START SCRIPT": f";USER START SCRIPT\nG0 Z{height}"
  })
  return content


def make_replacements(source_file, thickness):
  content = read_file(source_file)  # read input gcode file
  content = set_height(content, thickness)  # set height
  content = replace_text(content, replacements)  # make gcode replacements as per map above
  content = replace_text(content, {'X-0 ': 'X0 '})  # replace negative zeros
  content = replace_text(content, {'Y-0 ': 'Y0 '})  # replace negative zeros
  content = replace_text(content, {'Z-0 ': 'Z0 '})  # replace negative zeros
  content = to_fixed(content) # pad to 3 decimal places
  write_file(source_file + '.replaced', content)  # write out updated gcode file


if __name__ == '__main__':
  make_replacements(sys.argv[1], sys.argv[2])
