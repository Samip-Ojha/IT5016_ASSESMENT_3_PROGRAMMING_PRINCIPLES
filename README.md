# IT5016_ASSESMENT_3_PROGRAMMING_PRINCIPLES

This program is based on class system which has a constructor so whenever an object is created requisition ID is automatically generated, a global counter is used to generate the requisition ID. Attributes that are required are also defined by the constructor such as the date of submission, the staff ID, the staff name, items, total cost, status, and approval reference number which all be stored in a list, and it is easy to trach everything in one location, this demonstrates the kiss principle, as there is just a list rather than complex storage system.

This program has various functions like, the staff_info collects data such as the date, staff ID, and staff name. This section is related to the requirement analysis since the system requires this information to operate correctly. Simultaneously, testing and validation is done here, since the program would ensure that the inputs are right, such as ensuring that the staff ID and the name are not blank and that the date is not a string. requisitions details () is another function that requests the number of items the staff requests. It implements validation to ensure that the number is not just an empty number hence YANGI as simple method is used to check the value i.e. integer. Then it requests the names and the prices of the items. Also, the cost is verified to ensure that it is not negative or non-numeric. Everything and its prices are placed on a list, and the final cost is determined at the bottom. This section is correlated with the detailed design phase, as the input was planned to be received in this function and the total was to be calculated in a simple manner. The requisition approval function determines the requisition status, if total cost is below $500, then the requisition is automatically approved, and a reference number is generated with the help of the staff ID and the last three digits of the requisition ID. When the total cost is equal or greater than 500 dollars, the status of requisition gets to be pending. It is also an illustration of the principle of CLEAN CODE> CLEVER CODE since it employs one and straightforward condition, rather than complicated reasoning. In the case of pending requisitions, the respond requisition () function allows the manager to make final decision. This system has a simple yes or no query and if the manager approves then the requisition is granted with a reference number. Otherwise, the status will be changed to Not approved and no reference number will be provided. This is again straight and forward and displays KISS.

display_requisitions() function simply displays information of the requisition like date, staff details and items and the total cost, status and the approval reference number. This would be equal to the SRP since the role (function) is tasked with presenting information and nothing more.

A loop is in the main part of the program which ensures that the user may input several requisitions until when the user decides to quit. All these functions are invoked sequentially to gather the data, process the requisition and approvals. This represents KISS as each function performs a simple task of its own and the loop continues occurring till the user leaves the system.

The final step is to print out all the requisitions that were made and present statistics. It records the total number of requisitions that were made, the number approved, those pending and those not approved. This is achieved using a basic loop and counters and once again, the KISS principle is in action.











