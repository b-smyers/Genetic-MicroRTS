import random
import os

# Function to read lines from file and strip newline characters
def parse_to_array(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Lists of functions
LasiFunctionsDir = "./LasiFunctions"

def clean_script():
    with open("Script.txt", 'r') as file:
        data = file.read()

    # Replace "for(u) ( )" with an empty string
    modified_data = data.replace("for(u) ( ) ", "").replace("then( )", "").replace(" else( )", "")

    with open("Script.txt", 'w') as file:
        file.write(modified_data)

class Program_Line:
    def __init__(self):
        self.line_type = "null"
        self.file_index = 0
        self.function_index = 0

    # Generates a random line based on line type
    def __init__(self, line_type):
        self.line_type = line_type # (e.g. Action, ForAction, Boolean, ForBoolean, null, For, Else,')', or '))')

        if self.line_type != "null" and self.line_type != "For" and self.line_type != ")" and self.line_type != "))" and self.line_type != "Else":
            # generate random file and function indexes
            files = [f for f in os.listdir(f'{LasiFunctionsDir}/{self.line_type}Functions') if os.path.isfile(os.path.join(f'{LasiFunctionsDir}/{self.line_type}Functions', f))]
            self.file_index = random.randint(0, len(files)-1) # Get random file

            directory = f'{LasiFunctionsDir}/{self.line_type}Functions/'

            functions = parse_to_array(os.path.join(directory, files[self.file_index]))
            self.function_index = random.randint(0, len(functions)-1) # Get random function
        else:
            self.file_index = 0
            self.function_index = 0

    # Reads in program line from gene string
    def load_gene_string(self, gene_string):
        params = gene_string.split(",")
        self.line_type = params[0]
        self.file_index = int(params[1])
        self.function_index = int(params[2])
    
    def mutate(self):
        pass
    
    def get_line(self):
        # Get the line
        if self.line_type != "null":
            if self.line_type == "ForBoolean" or self.line_type == "Boolean":
                files = [f for f in os.listdir(f'{LasiFunctionsDir}/{self.line_type}Functions') if os.path.isfile(os.path.join(f'{LasiFunctionsDir}/{self.line_type}Functions', f))]
                directory = f'{LasiFunctionsDir}/{self.line_type}Functions/'
                functions = parse_to_array(os.path.join(directory, files[self.file_index]))
                return "if(" + functions[self.function_index] + ") then("
            elif self.line_type == "Action" or self.line_type == "ForAction":
                files = [f for f in os.listdir(f'{LasiFunctionsDir}/{self.line_type}Functions') if os.path.isfile(os.path.join(f'{LasiFunctionsDir}/{self.line_type}Functions', f))]
                directory = f'{LasiFunctionsDir}/{self.line_type}Functions/'
                functions = parse_to_array(os.path.join(directory, files[self.file_index]))
                return functions[self.function_index]
            elif self.line_type == "For":
                return "for(u) ("
            elif self.line_type == "Else":
                return ") else("
            elif self.line_type == ")":
                return ")"
            elif self.line_type == "))":
                return "))"
        else:
            return "" # empty line

    def print_line(self):
        print(self.get_line())

    def print_gene(self):
        print(f'{self.line_type},{self.file_index},{self.function_index}')

    def get_gene(self):
        return f'{self.line_type},{self.file_index},{self.function_index}'


class RTS_Script:
    def __init__(self, line_limit):
        self.line_limit = line_limit
        self.Program_Lines = []

    def print_script(self):
        print("Script:\n```")
        for Line in self.Program_Lines:
            Line.print_line()
        print("```")

    def print_chromosomes(self):
        print("Chromosome:\n```")
        for Line in self.Program_Lines:
            print(Line.get_gene() + ' ')
        print("```")

    def log_script(self):
        with open("./Output/Script.txt", "w") as file:
            for Line in self.Program_Lines:
                file.write(Line.get_line() + ' ')
    
    def log_chromosomes(self):
        with open("Output/Chromosome.txt", "w") as file:
            for Line in self.Program_Lines:
                file.write(Line.get_gene() + ' ')
    
    def generate_random_script(self):
        # List of line options by scenario
        line_options          = ["ACTION", "for(u) (", "if("]
        for_line_options      = ["ACTION", "ACTION", "ACTION", "ACTION", "ACTION", "ACTION", ")", "if("]
        if_line_options       = ["ACTION", "ACTION", "ACTION", ")", ") else("]
        else_line_options     = ["ACTION", "ACTION", "ACTION", ")"]
        for_else_line_options = ["ACTION", "ACTION", "ACTION", "ACTION", "ACTION", ")", "))"]
        for_if_line_options   = ["ACTION", "ACTION", "ACTION", "ACTION", "ACTION", ")", ") else(", "))"]

        # Indicators to keep track of when we are in a loop, if, or both
        is_for = False
        is_if = False
        is_else = False
        for i in range(self.line_limit):
            # Make choice (Don't allow having nested loops or ifs)
            choice_options = line_options
            if is_for and is_if:
                choice_options = for_if_line_options
            elif is_for and is_else:
                choice_options = for_else_line_options
            elif is_for:
                choice_options = for_line_options
            elif is_if:
                choice_options = if_line_options
            elif is_else:
                choice_options = else_line_options

            choice = random.choice(choice_options)

            # Handle each choice
            if choice == "if(":
                if is_for:
                    self.Program_Lines.append(Program_Line("ForBoolean"))
                else:
                    self.Program_Lines.append(Program_Line("Boolean"))
                is_if = True
            elif choice == "ACTION":
                if is_for:
                    self.Program_Lines.append(Program_Line("ForAction"))
                else:
                    self.Program_Lines.append(Program_Line("Action"))
            elif choice == ") else(":
                self.Program_Lines.append(Program_Line("Else"))
                is_if = False
                is_else = True
            elif choice == "for(u) (":
                self.Program_Lines.append(Program_Line("For"))
                is_for = True
            elif choice == ")":
                self.Program_Lines.append(Program_Line(")"))
                if is_else:
                    is_else = False
                elif is_if:
                    is_if = False
                elif is_for:
                    is_for = False
            elif choice == "))":
                self.Program_Lines.append(Program_Line("))"))
                is_for = is_if = is_else = False
        
        # close up any loose ends
        if is_if and is_for:
            self.Program_Lines.append(Program_Line("))"))
        elif is_if or is_for:
            self.Program_Lines.append(Program_Line(")"))


def main():
    new_rts_script = RTS_Script(10)
    new_rts_script.generate_random_script()

    new_rts_script.print_script()
    new_rts_script.print_chromosomes()

    new_rts_script.log_script()
    new_rts_script.log_chromosomes()



    # Clean up stage (DSL compiler is very picky and doesn't like empty if's else's or for loops)
    # clean_script()




if __name__ == "__main__":
    main()