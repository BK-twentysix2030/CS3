# Annex C
## Code Quality Assessment Worksheet

Section: 9-Balingkilat &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Score:____________

C#/Name:#25/Allaina Maxene Leyran &emsp;&emsp;Date: 08/15/26<br>&emsp;&emsp;&emsp;&emsp;&emsp;#26/Caelyn Arabelle Maglaya<br>&emsp;&emsp;&emsp;&emsp;&emsp;#27/Trish Aubrey Malaca


### Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| Algorithm FindMax1(numbers)<br>&emsp;max ← numbers[0]<br>&emsp;For i from 1 to length(numbers)-1<br>&emsp;&emsp;If numbers[i] > max Then<br>&emsp;&emsp;&emsp;max ← numbers[i]<br>&emsp;&emsp;EndIf<br>&emsp;EndFor<br>&emsp;Return max<br>EndAlgorithm | Algorithm FindMax2(numbers)<br>&emsp;For i from 0 to length(numbers)-1bigger ← true<br>&emsp;&emsp;For j from 0 to length(numbers)-1<br>&emsp;&emsp;&emsp;If numbers[j] > numbers[i] Then<br>&emsp;&emsp;&emsp;&emsp;bigger ← false<br>&emsp;&emsp;&emsp;EndIf<br>&emsp;&emsp;EndFor<br>&emsp;&emsp;If bigger = true Then<br>&emsp;&emsp;&emsp;Return numbers[i]<br>&emsp;&emsp;EndIf<br>&emsp;EndFor<br>EndAlgorithm |


#### Questions with Checklists
**1. Efficiency**

**Which algorithm is faster when the list of numbers is very large? Why?**
- The first pseudocode’s algorithm is more efficient when the list of numbers is huge because the list goes through a fewer processes. Additionally, the pseudocode itself is more straightforward as compared to the second one which has nested loops that makes it repeat work needlessly.

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| [/] Does the algorithm use one loop or two nested loops?<br>[] Does the algorithm repeat work unnecessarily?<br>[/] Which algorithm finishes in fewer steps? | [/] Does the algorithm use one loop or two nested loops?<br>[/] Does the algorithm repeat work unnecessarily?<br>[] Which algorithm finishes in fewer steps? |

**2. Readability**

**Which algorithm is easier to understand at first glance? What makes it clearer?**
- The first algorithm was considerably more understandable to read as it is written with a concise and straightforward approach to the problem. The second, on the other hand, contains a nested loop and multiple If-Else statements, requiring jumping between lines to understand the full flow of the program.

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| :--- | :--- |
| [/] Are variable names meaningful (e.g., max vs. bigger)?<br>[simple] Is the logic simple or complicated?<br>[/] Are there fewer lines of code? | [/] Are variable names meaningful (e.g., max vs. bigger)?<br>[complicated] Is the logic simple or complicated?<br>[] Are there fewer lines of code? |

**3. Maintainability**

**If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?**
- The first pseudocode’s algorithm is much more easier to modify compared to the second one as the latter has more parts, thus it is more fragile. For the second one, one has to work on the different parts of the algorithm for it to work with the alterations.
  
**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| :--- | :--- |
| [/] Is the structure straightforward?<br>[] Would adding new steps break the code easily?<br>[/] Is there less chance of errors when updating?<br> | [] Is the structure straightforward?<br>[/] Would adding new steps break the code easily?<br>[] Is there less chance of errors when updating? |

**4. Testability**

**Which algorithm is easier to test with different inputs? Why?**
- Which algorithm is easier to test with different inputs? Why?
The first algorithm since the program does not need to jump between many decisions, unlike the second algorithm. 

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| :--- | :--- |
| [/] Can you test with small lists easily?<br>[/] Does the algorithm have fewer conditions to check?<br>[/]  Is the output predictable and clear? | [/] Can you test with small lists easily?<br>[] Does the algorithm have fewer conditions to check?<br>[]  Is the output predictable and clear? |

**5. Security**

**Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?**
- The algorithm should check the list to see whether it is empty or not before finding the highest number. Additionally, it should check the user's input to verify whether it has valid numbers or invalid ones. Overall, it should be able to handle unusual inputs efficiently to prevent the program from having errors or crashing entirely.

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| :--- | :--- |
| [] Does the algorithm check if the list is empty?<br>[] Does it handle invalid inputs (like letters instead of numbers)?<br>[]  Does it avoid crashing when inputs are unusual? | [] Does the algorithm check if the list is empty?<br>[] Does it handle invalid inputs (like letters instead of numbers)?<br>[]  Does it avoid crashing when inputs are unusual? |

**6. Final Answer**

**Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer.**
- Based on our answers, PseudoCode 1 is the better algorithm to use to find the highest number. It is more efficient as it uses only one loop with no unnecessary repeated comparisons. It is also easier to understand, test, and debug if problems arise. Hence, we would choose PseudoCode 1 as the better solution.
_________________________________________________________________

_________________________________________________________________

 
