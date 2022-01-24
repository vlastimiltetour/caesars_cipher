import string

def caesars_cipher():

  keys = (" " + string.ascii_lowercase + string.punctuation)
  values = keys[3:-1] + keys[::3]
  
  ciphering_dict = dict(zip(keys,values))
  deciphering_dict = dict(zip(values,keys))

  msg = input("input your text here: ")
  mode = input("[c]ipher or [d]ecipher?")

  for letter in msg:
    if mode == "c":
      new_msg = "".join([ciphering_dict[letter] for letter in msg])
    elif mode == "d":
      new_msg = "".join([deciphering_dict[letter] for letter in msg])
    else:
      raise ValueError

  return new_msg

print(caesars_cipher())