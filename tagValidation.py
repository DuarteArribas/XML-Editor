import re

def validateTag(tag):
  return bool(re.match(r"^[a-zA-Z_][a-zA-Z\d\s_.-]*$",tag))