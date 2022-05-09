def SentenceValidator(string):
  length = len(string)
  #Start letter must be an uppercase letter
  if (string[0] < 'A' or string[0] > 'Z'):
    return False
  #last character of sentence must be  . (dot) ? (question mark) ! (exclamation mark)
  elif not(string[length-1] == '.' or string[length-1] == '?' or string[length-1] == '!'):
    return False
  #All letters in the sentence except the start letter must be in lowercase
  else:
    for ele in string[1:]:
      if ele.isupper():
        return False
  #Words must be separated with a single whitespace.
  #check for more than 2 consecutive whitespace
  for i in range(len(string)) :
    if (string[i]==' ' and string[i+1]==' ') :
      return False
  #If there is a hyphen between any two words then
  #there should be one whitespace before and after that hyphen.
  for i in range(len(string)) :
    if (string[i]=='-') :
      if not((string[i-1]==' ')and (string[i+1]==' ')):
        return False
  return string

def reducer(ValidOp) :
  #Removes terminal characters
  ValidOp=ValidOp[:-1]
  #Removes all leading and trailing whitespaces
  ValidOp=ValidOp.strip()
  #Removes all leading and trailing HYPHENS
  ValidOp=ValidOp.strip("-")
  #Removes all duplicated word groups  but keep its first occurence
  l = ValidOp.split()
  k = []
  for i in l:
    if (ValidOp.count(i)>=1 and (i not in k) or i =='-'):
      k.append(i)
  ValidOp=' '.join(k)
  return ValidOp

def check_and_clean() :
  stringcheck=str(input("Input String : "))
  if (SentenceValidator(stringcheck) != False ) :
    print("******** OUTPUT ***********************")
    return (reducer(SentenceValidator(stringcheck)))
  else :
    print("******** OUTPUT ***********************")
    return ("<invalid>")

#driverprogram
#test case 1 Melo diagnostics melo Labs
check_and_clean()