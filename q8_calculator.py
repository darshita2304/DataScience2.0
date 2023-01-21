## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q8: create a class to a calculator functionalities add, sub,mul,div, log, exponenet, power

import logging
import math

logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")


class q8_calculator:
    
    def addition(self, list_arg):

        logging.info("this is start of addition fn")
        try:
            logging.info("inside try block of addition fn")
            
            sum = 0
            for i in list_arg:
                sum = sum + i
            
            print(f"addition of list is {str(sum)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with addition fn")
            logging.error(e)

    def subtraction(self, no1, no2):
        no1 = int(no1)
        no2 = int(no2)
        logging.info("this is start of subtraction fn")
        try:
            logging.info("inside try block of subtraction fn")
            
            if no1>no2:
                ans = no1-no2
            else:
                print("Given number 1 is grater than 2")
                return
            
            print(f"subtraction of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with subtraction fn")
            logging.error(e)

    def multipy(self, list_arg):
        logging.info("this is start of multipy fn")
        try:
            logging.info("inside try block of multipy fn")
            
            ans = 1
            for i in list_arg:
                ans = ans * i
            
            print(f"multipy of given number is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with multipy fn")
            logging.error(e)

    def division(self, no1, no2):
        no1 = int(no1)
        no2 = int(no2)
        logging.info("this is start of division fn")
        try:
            logging.info("inside try block of division fn")
            
            if no1>no2:
                ans = no1/no2
            else:
                print("Given number 1 is grater than 2")
                return
            
            print(f"division of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with division fn")
            logging.error(e)
    
    def log(self, no1):
        no1 = float(no1)
        
        logging.info("this is start of logarithm fn")
        try:
            logging.info("inside try block of logarithm fn")
                     
            ans = math.log(no1)            
            print(f"log of {no1} is {ans}")
            return
            
            print(f"division of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with .logarithm fn")
            logging.error(e)
          

obj = q8_calculator()

obj.addition([1,2,3,4])
obj.subtraction(45, 5)
obj.multipy([1,2,3,4])
obj.division(45, 5)
obj.log(100.12)



