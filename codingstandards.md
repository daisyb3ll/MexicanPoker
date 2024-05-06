These Are the Coding Standards!!

Author: Daisy Fernandez-Reyes <@daisyb3ll on github, daisy.fernandez.zr@gmail.com >
Status: Active
Created: 05-06-24

Ground Rules: 
    1. Use meaningful variable and function names.
    2. Write clear and concise comments where necessary.
    3. Before each function, comment a brief description of the function
    4. Avoid redundant or unnecessary code please!
    5. Keep the codebase clean and organized.
    6. Class names should use the camelCase;  for example, "red crayon" would be redCrayon
    7. Functions, variables, and attributes should be in lowercase, with words separated by underscores: my_variable.

Code Layout (referenced from https://peps.python.org/pep-0008/):

    Indentation: 
        Use 4 spaces per indentation level.
        Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces, or using a hanging indent [1]. When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line:

            # Correct:

            # Aligned with opening delimiter.
            foo = long_function_name(var_one, var_two,
                                    var_three, var_four)

            # Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
            def long_function_name(
                    var_one, var_two, var_three,
                    var_four):
                print(var_one)

            # Hanging indents should add a level.
            foo = long_function_name(
                var_one, var_two,
                var_three, var_four)

            # Wrong:

            # Arguments on first line forbidden when not using vertical alignment.
            foo = long_function_name(var_one, var_two,
                var_three, var_four)

            # Further indentation required as indentation is not distinguishable.
            def long_function_name(
                var_one, var_two, var_three,
                var_four):
                print(var_one)
                
    Maximum Line Length:
        Limit all lines to a maximum of 79 characters.

    Binary Operations: 
        Donald Knuth (King Comp Sci) explains the traditional rule in his Computers and Typesetting series: “Although formulas within a paragraph always break after binary operations and relations, displayed formulas always break before binary operations” [3].

            Following the tradition from mathematics usually results in more readable code:

            # Correct:
            # easy to match operators with operands
            income = (gross_wages
                    + taxable_interest
                    + (dividends - qualified_dividends)
                    - ira_deduction
                    - student_loan_interest)
            
            # Wrong:
            # operators sit far away from their operands
            income = (gross_wages +
                    taxable_interest +
                    (dividends - qualified_dividends) -
                    ira_deduction -
                    student_loan_interest)
    Imports: 
        Imports should always be on seperate lines. 
            # Correct:
            import os
            import sys

            # Wrong:
            import sys, os
    
    Pet Peeves (violators will be sent straight to mega-coding-jail):
        1.extraneous white spaces
            #wrong
                spam( ham[ 1 ], { eggs: 2 } )
            #correct 
                spam(ham[1], {eggs: 2})
    