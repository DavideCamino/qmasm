import os


class Preprocess:

    def __init__(self):
        self.name = {}
        self.new_lines = []

    def preprocess(self, args): 
        file = args[-1]

        old = open(file, 'r').read()
        open(file+".old", 'w').write(old)
        
        with open(file, 'r') as input:
            first_row = input.readline()
            second_row = input.readline()
            while(second_row != ""):
                if first_row.startswith("#") and second_row.startswith("!begin_macro"):
                    self.name[first_row[2:-1]] = second_row[len("!begin_macro "):-1]
                first_row = second_row
                second_row = input.readline()

        with open(file, 'r') as input:
            doc = input.read()
            lines = doc.splitlines()
            for line in lines:
                for word in line.split():
                    if word in self.name.keys():
                        line = line.replace(word, self.name[word])
                self.new_lines.append(line)

        with open(file, 'w') as output:
            for line in self.new_lines:
                output.write(line+"\n")