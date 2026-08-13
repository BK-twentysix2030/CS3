Annex A

Computational Thinking Exercise: "Smart School Canteen Queue"

Section: Balingkilat                      Score:____________

C# / Name: #26 Caelyn Arabelle Maglaya    Date: Aug 12, 2026


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

1. Some students take too long to decide what to order.

2. The cashier has to manually calculate totals and give change.

3. There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

 Main Problem: The school canteen becomes crowded during lunch breaks, causing long and slow-moving queues.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

 1. Slow Ordering -> Students take a long time deciding what to order.
 2. Manual Payment Calculation -> The cashier has to manually calculate totals and give change.
 3. Lack of Supply Tracker -> There is no system to check whether food items are running out.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

 Sub-Problem                  CT Skill              Example Solution
 Slow Ordering                Decomposition         Pre-orders
 Manual Payment Calculation   Algorithm             Register for payment calculation      
 Lack of Supply Tracker       Pattern Recognition   Spreadsheet Menu Tracker

 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
  Pseudocode for Sub-Problem 2
  
START
Display food menu
Take order
    Ask if customer would like meal
         IF customer says YES
              Ask for meal choice (choices depend on availability on the day)
              Identify price of meal choice
         ELSE: price is 0Php
    Ask if customer would like rice
        IF customer says YES
              Ask for rice portion (whole, half, double serving, etc)
              Identify price of portion
         ELSE: price is 0Php
   Ask if customer would like side
        IF customer says YES
              Ask for choice of side (fruit, turon, etc)
              Identify price of side
         ELSE: price is 0Php
Enter price of meal, price of rice portion, price of side and calculate sum
Display order summary and cost
Ask customer for payment
Calculate Change
     IF payment > total cost
          Payment - total cost = change
          Give change to customer
     ELIF payment < total cost
          Ask customer for additional money
          Add additional money to payment
          Calculate change again
     ELSE: change = 0, customer finished
END

Group Reflection: 
Decomposition is an essential process when solving problems, as it breaks down the whole concept or problem into smaller, more manageable parts. It is used to understand a complex problem and to solve it more effectively.

Firstly, for the problem of slow ordering, we used the skill of decomposition. We used decomposition because we planned to break down the ordering process into smaller steps; thus, our solution was to initiate pre-orders to minimize the waiting time in the queue and to divide the ordering process into sections or segments.

Secondly, for the manual payment collection, we decided to use algorithmic thinking (Algorithm). To avoid the struggle of manually calculating totals and change, a mechanism that does repetitive calculations can really be a life-changer. Our solution for this problem was to use a cash register for payments, as it is already designed to compute the cost of products and make change.

Lastly, to fix the lack of a system to track supply shortages, we used the critical thinking skill of pattern recognition. An apparatus that could analyze and structure data about the products for organization is appropriate. Therefore, we decided to use spreadsheets as a solution because they can hold data, store data, and perform arithmetic operations to track the depletion of an item's supply.
