# requisitionsystem.py
"""
    Code for requisition system using class methods, constructor is created for
    creating variable and each time an object is created, value 
    is stored on those variables using the List that is there as global varaiable for class, after that fucntions are there from Part A and then
    new function is added for maagerial response and that is later counted on main function which is finally printed on statics.
"""


"""KISS is used here as simple counter system is used here"""

staff_counter = 10000  # global counter for requisition IDs , this is part of planning 

class RequisitionSystem:
    """store all requisitions here , this is part of designing; storage for all requisitions"""
    all_requisitions = []  
    """ KISS is used as using a single list for all requisitions instead of a database"""

    def __init__(self):  #constructor which calls everytime object is created 
        global staff_counter
        staff_counter += 1
        """this is part of the requirement, as system must auto generate requisition ID"""
        self.requisition_id = staff_counter   

        """these are part of designing as here required attributes are defined here"""
        self.date_submission = ""
        self.staff_id = ""
        self.staff_name = ""
        self.items = []
        self.total_cost = 0
        self.status = "Pending"
        self.approval_reference_number = "Not available"

        """this can be counted as part of solution design, as here solution is designed to store each created requisition into central list"""
        RequisitionSystem.all_requisitions.append(self)  #calling the class and assigning list properties of the .self
        """KISS used as simple append is used instead of complex storing"""
    
# a. collecting staff info
        """ this is part ofRequirement Analysis as the system needs staff information
        besides that Testing and Validation is done to ensure right data is inputted"""
    def staff_info(self): # function created to take information of the staffs
        while True:
            try:    #try and except used in this conditional statement to check error validation
                self.date = int(input("Enter Date of submission (DD MM YYYY): "))
                if self.date != "":
                    self.date_submission = self.date
                    break
                else:
                    print("Date cannot be empty Try again.")
            except ValueError:
                """ this is part of Testing as validation feedback can be checked here"""
                print("Date cannot be string Try again.") 

        while True:
            """this is also part of the Testing as this part ensures if the right data is inputted i.e. not empty string"""
            staff_id = input("Enter ID: ").strip() 
            if staff_id != "":
                self.staff_id = staff_id  
                break
            else:
                print(" Staff ID cannot be empty Try again.")

        while True:
            """this is also Testing similar to above"""
            staff_name = input("Enter Name: ").strip()
            if staff_name != "":
                self.staff_name = staff_name
                break
            else:
                print(" Name cannot be empty Try again.")

        return self.date_submission, self.staff_id, self.staff_name, self.requisition_id


# b. item infos 
    def requisitions_details(self):
        while True:    
            try:
                """this is part of Testing and Design as this part is designed to take number
                for the items to be taken and besides that it ensures that a valid number is inputted"""
                Number = int((input("Enter number of items you want: ")))
                """YANGI as simple method is used to check the value i.e. integer"""
                if Number!= "":
                    Number 
                    break
                else:
                    print("number cannot be empty, please try again.")
            except ValueError:
                    print("number cannot be letters,Please try again.")
    

        total_cost = 0
        items = [] 
        count = 0

        while count < Number:
            while True:
                name = input(f"Enter name of item : ").strip()
                if name != "":
                    {count+1}
                    break
                else:
                    print(" Item name cannot be empty Try again.")

            while True:
                """this is part of detailed design as this part is designed to take input cost which later would be addeed 
                for final which will be used for status """
                cost = input(f"Enter cost of {name}: ").strip()
                try:
                    cost = float(cost)
                    if cost >= 0:
                        break
                    else:
                        print("Cost cannot be in minus.")
                except ValueError:
                    print(" Invalid cost Please enter a valid number.")

            print(f"name of the item: {name}")
            print(f"cost: {cost}")

            items.append((name, cost))
            total_cost += cost
            count += 1

        self.items = items
        self.total_cost = total_cost
        return self.total_cost
# c. approval decision
    """ this is the part of Requirement as the system must auto approve if < $500 else set status to  pending"""
    def requisition_approval(self): # this funciton will check uf the total cost is more or
                                    # less than an specific amount to give it a status
        """Clean code> Clever code as it has single condition less than $500 gets approved, else pending keeping logic clear"""
        if self.total_cost < 500:
            self.status = "Approved"
            self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"  # generate reference number from staff id + 
                                                                                                #last 3 digits of requisition id
        else:
            self.status = "Pending"
        return self.status
    #response by manager
    def respond_requisition(self): # this is a function created for manager approval 
        """#this is part of the Requirement as system must ask manager to finalize pending requisitions status"""
        if self.status == "Pending":
            then = input("you want this to be approved? y/n:") 
            """kiss as normal yes no is asked"""
            then = then.lower()
            if then == "y":
                self.status = "Approved"
                self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            else:
                self. status = "Not approved"
                self.approval_reference_number = " not available"
        return self.status, self.approval_reference_number

    def display_requisitions(self): # each attributes are acccessed here to print 
        
        """SRP as only prints required things i.e one task"""
        
        print("\nRequisition Details:")
        print(f"Date of submission: {self.date_submission}")
        print(f"staff ID: {self.staff_id}")
        print(f"Staff name: {self.staff_name}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Total cost: ${self.total_cost}")
        print(f"Status: {self.status}")
        print(f"Approval reference number: {self.approval_reference_number}")
# d. main funciton
if __name__ == "__main__":
    while True: # here an object is created to invoke each function 
        caller = RequisitionSystem()
        
        """KISS, as each function does its own work making it simple"""
        
        caller.staff_info()  
        caller.requisitions_details()
        caller.requisition_approval()
        caller.respond_requisition()

        again = input("\nWanna enter another requisition? (y/n): ").lower()
        if again != "y":
            break

    print("\n response")
    i = 0
    while i < len(RequisitionSystem.all_requisitions): #hrere length for the list is invoked via calling through class 
        
        "KISS as simple looping system is used instead of complex count"
        RequisitionSystem.all_requisitions[i].display_requisitions()
        i += 1


    total = len(RequisitionSystem.all_requisitions)
    approved = 0
    pending = 0 
    not_approved = 0

    i = 0
    while i < len(RequisitionSystem.all_requisitions): 
        r = RequisitionSystem.all_requisitions[i]
        if r.status == "Approved":
            approved += 1
        elif r.status == "Pending":
            pending += 1
            not_approved += 1
        i += 1
    
    """KISS is used here for simple output for Statistics"""
    
    print("\nStatistics:")
    print("Displaying the requisition statistics")
    print(f" total number of requisitions submitted: {total}")
    print(f"total number of approved requisitions: {approved}")
    print(f"total number of pending requisitions: {pending}")
    print(f"total number of not approved requisitions: {not_approved}")