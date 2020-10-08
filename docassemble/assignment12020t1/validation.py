import re
from docassemble.base.util import *

def last_char_for_ST(val):
  switch = {
    0: 'J',
    1: 'Z',
    2: 'I',
    3: 'H',
    4: 'G',
    5: 'F',
    6: 'E',
    7: 'D',
    8: 'C',
    9: 'B',
    10: 'A'
  }
  return switch.get(val)
  
def last_char_for_FG(val):
  switch = {
    0: 'X',
    1: 'W',
    2: 'U',
    3: 'T',
    4: 'R',
    5: 'Q',
    6: 'P',
    7: 'N',
    8: 'M',
    9: 'L',
    10: 'K'
  }
  return switch.get(val)
	
def check_nric(nric):
  nric = nric.upper()
  if valid_format(nric) and valid_checksum(nric):
    return True  

def valid_format(nric):
  if not re.match(r'[STFG][0-9]{7}[A-Z]',nric):
    validation_error('Invalid NRIC format! Please check and enter again.')
  return True

def valid_checksum(nric):
  x = (int(nric[1]) * 2) + (int(nric[2]) * 7) + (int(nric[3]) * 6) + (int(nric[4]) * 5) + (int(nric[5]) * 4) + (int(nric[6]) * 3) + (int(nric[7]) * 2)

  if nric[0] == 'T' or nric[0] == 'G':
    x = x + 4 
   
  y = x % 11
	
  if nric[0] == 'S' or NRIC[0] == 'T':
    z = last_char_for_ST(y)
		
    if nric[8] != z:
      validation_error('Invalid NRIC format! Please check and try again.')
    return True
  
  elif nric[0] == 'F' or nric[0] == 'G':
    z = last_char_for_FG(y)

    if nric[8] != z:
      validation_error ('Invalid NRIC format! Please check and try again.')
    return True
            
