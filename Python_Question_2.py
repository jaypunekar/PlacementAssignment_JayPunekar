class VaildString:
    def __init__(self, given_string):
        self.given_string = given_string

    def check_validity(self) -> bool:
        try:
            #Created empty dict for storing character and its frequency
            char_dict = dict()

            #Initialized all values to 0
            for char in self.given_string:
                char_dict[char] = 0

            #Counted all the character frequency
            for char in self.given_string:
                char_dict[char] = char_dict[char] + 1

            #char_freq contains the frequency of first character
            first_char_freq = char_dict[self.given_string[0]]

            #Compared all frequencies to the frequency of first character
            is_same = True
            for char, freq in char_dict.items():
                if freq != first_char_freq:
                    is_same = False
            #If is_same is False then we remove the first character and check again
            #(Note:- The code is written differently but we get correct answer)
            if not is_same:
                is_same = True
                del char_dict[self.given_string[0]]
                for char, freq in char_dict.items():
                    if freq != first_char_freq - 1:
                        is_same = False
            
            return is_same

        except Exception:
            raise Exception
            print("There was an Error")

    def print_validity(self, result:bool):
        try:
            if result == 1:
                print("YES")
            else:
                print("NO")
        except Exception:
            print("Something went wrong")


string = input("Enter a string: ")

string_validity = VaildString(string)
string_validity.print_validity(string_validity.check_validity())

"""
Test Case 1:

Input: aabc
Output: YES

Explaination: if we remove the first character the condition for validity is met.
"""

"""
Test Case 2:

Input: abbc
Output: NO

Explaination: Deletion of only first character is allowed. So we get NO.
"""
