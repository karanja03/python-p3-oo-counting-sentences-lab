#!/usr/bin/env python3
import re
class MyString:
   
   def __init__(self, value) :
      if type  (value) is str:
         self.value=value
      else:
         print("The value must be a string.")

   def is_sentence(self):
       if self.value.endswith('.'):
        return True
       else:
        return False
       
   def is_question(self):
      if self.value.endswith("?"):
         return True
      else:
         return False
      
   def is_exclamation(self):
       if self.value.endswith("!"):
         return True
       else:
         return False
       
    

   def count_sentences(self):
    sentences = re.split(r'[.!?]', self.value)
    non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(non_empty_sentences)


