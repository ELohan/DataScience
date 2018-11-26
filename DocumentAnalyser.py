class DocumentAnalyser:
    lines = 1
    words = 1
    chars = 1
    avg_CHRpL = 1
    avg_WpL = 1
    avg_CHRpW = 1
    file = 1
    f = 1

    def __init__(self, fname):
        self.f = open(fname) #opeing the file
        self.file = self.f.read() # reading a file as a string
        self.f.close()
        self.count_lines()
        self.count_words()
        self.num_of_chars()
        self.average_number_of_chars_per_line()
        self.average_number_of_words_per_line()

    def count_lines(self):
        self.lines = self.file.count("\n")  # number of lines = number of "\n" + 1 as the last line doesnt have a "\n"
        if len(self.file) > 0:
            self.lines += 1 # but only if theres at least one word

    def count_words(self):
        self.words = len(self.file.split()) # splitting the string and converting it to list , number of words  = length of the list

    def num_of_chars(self):
        return len(self.file.replace(" ", "").replace("\n", "")) # num of chars = length of the string without spaces and endlines

    def average_number_of_chars_per_line(self):
        return self.chars / max (1,self.lines) # max to avoid division by zero

    def average_number_of_words_per_line(self):
        return  self.words / max(self.lines,1)

    def average_number_of_chars_per_word(self):
        return  self.num_of_chars() / max(1,self.num_of_words())

    def num_of_words(self):
        return  self.words

    def num_of_lines(self):
        return self.lines


print("test 1\n")
test = DocumentAnalyser("hello.txt")
print("number of lines ",  test.num_of_lines())
print("number of chars ", test.num_of_chars())
print("number of words ", test.num_of_words())
print("average_number_of_words_per_line " , test.average_number_of_words_per_line())
print("average_number_of_chars_per_line ", test.average_number_of_chars_per_line())
print("average_number_of_chars_per_word ",test.average_number_of_chars_per_word())
print("\n------------------------------------------------------------------\n")
#----------------------------------



print("test 2\n")
test = DocumentAnalyser("one_line.txt")
print("number of lines ",  test.num_of_lines())
print("number of chars ", test.num_of_chars())
print("number of words ", test.num_of_words())
print("average_number_of_words_per_line " , test.average_number_of_words_per_line())
print("average_number_of_chars_per_line ", test.average_number_of_chars_per_line())
print("average_number_of_chars_per_word ",test.average_number_of_chars_per_word())
