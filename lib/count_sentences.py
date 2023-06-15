#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self._value = value
  
  def get_value(self):
    return self._value

  def set_value(self, value):
    if isinstance(value, str):  
      self._value = value
    else:
      print("The value must be a string.")
      
  value = property(get_value, set_value)

  def is_sentence(self):
    if self.value[len(self.value)-1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[len(self.value)-1] == "?":
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[len(self.value)-1] == "!":
      return True
    else:
      return False
    
  def count_sentences(self):
      sentence_count = 0
      char_list = list(self.value)
      for i, char in enumerate(char_list):
          if char == "?" or char == "!" or char == ".":
              if i == len(char_list) - 1 or not (char_list[i + 1] == "?" or char_list[i + 1] == "!" or char_list[i + 1] == "."):
                  sentence_count += 1
      return sentence_count
      for char in char_list:
          if char == "?" or char == "!" or char == ".":
            if i == len(char_list) - 1 or not (char_list[i + 1] == "?" or char_list[i + 1] == "!" or char_list[i + 1] == "."):
                  sentence_count += 1

      for i in range(len(char_list)):
          char = char_list[i]
          if char == "?" or char == "!" or char == ".":
              # Check if the current punctuation mark is not followed by another punctuation mark
              if i == len(char_list) - 1 or not (char_list[i + 1] == "?" or char_list[i + 1] == "!" or char_list[i + 1] == "."):
                  sentence_count += 1
      for char in char_list:
          if char == "?" or char == "!" or char == ".":
              sentence_count += 1
      return sentence_count
