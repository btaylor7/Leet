#class Solution(object):
 #   def isPalindrome(self, x):
  #      x_backwards = []
   #     for item in x[::-1]:
    #        x_backwards.append(item)
     #   for i in range(len(x)):
      #      if x[i] != x_backwards[i]:
       #         return False
        #return True
#If the input is a list [1,2,1]

class Solution(object):
    def isPalindrome(self, x):
        x_string = str(x)
        x_backwards=[]
        for item in x_string[::-1]:
            x_backwards.append(item)
        x_backwards = ''.join(x_backwards)
        return x_string == x_backwards
    
#str()works for single objects, like an integer or other type.
#x_backwards is a list, so str() does not work here.
#It would return something like "['1', '2', '4']"
#Hence we use .join() which can turn lists of strings into a single list.
#without including the commas or '' between them.