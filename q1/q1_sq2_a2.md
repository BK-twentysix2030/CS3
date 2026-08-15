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
Which algorithm is faster when the list of numbers is very large? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| [] Does the algorithm use one loop or two nested loops?<br>[] Does the algorithm repeat work unnecessarily?<br>[] Which algorithm finishes in fewer steps? | [] Does the algorithm use one loop or two nested loops?<br>[] Does the algorithm repeat work unnecessarily?<br>[] Which algorithm finishes in fewer steps? |

**2. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| [] Are variable names meaningful (e.g., max vs. bigger)?<br>[] Is the logic simple or complicated?<br>[]  Are there fewer lines of code? | [] Are variable names meaningful (e.g., max vs. bigger)?<br>[] Is the logic simple or complicated?<br>[]  Are there fewer lines of code? |

<br>**3. Maintainability**

If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| [] Is the structure straightforward?<br>[] Would adding new steps break the code easily?<br>[]  Is there less chance of errors when updating? | [] Is the structure straightforward?<br>[] Would adding new steps break the code easily?<br>[]  Is there less chance of errors when updating? |

**4. Testability**

Which algorithm is easier to test with different inputs? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| [] Can you test with small lists easily?<br>[] Does the algorithm have fewer conditions to check?<br>[]  Is the output predictable and clear? | [] Can you test with small lists easily?<br>[] Does the algorithm have fewer conditions to check?<br>[]  Is the output predictable and clear? |

**5. Security**

Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

**Checklist to guide your answer:**
| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| [] Does the algorithm check if the list is empty?<br>[] Does it handle invalid inputs (like letters instead of numbers)?<br>[]  Does it avoid crashing when inputs are unusual? | [] Does the algorithm check if the list is empty?<br>[] Does it handle invalid inputs (like letters instead of numbers)?<br>[]  Does it avoid crashing when inputs are unusual? |

**6. Final Answer**

Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

 
