import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from string import punctuation

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
print()

# creating set of stop words
stop_words = set(stopwords.words("english"))

# using a word lemmatizer to group together different types of similar word
lemmatizer = WordNetLemmatizer()


# this converts a text to lower case
def get_lower_case(text):
	return text.lower()

# this replaces the punctuations in a text with a space
def get_non_punctuated_words(text):
	output = ""
	for ch in text:
		if ch in punctuation:
			output += ' '
		else:
			output += ch
	return output


# this generates a tokenized list from a text
def get_tokenized_list(text):
	return word_tokenize(text)


# this removes the stopwords present in the list arr
def get_non_stopword_list(arr):
	# arr is tokenized already
	l = []
	for word in arr:
		if word not in stop_words:
			l.append(word)
	return l

# this lemmatizes the words present in the list arr
def get_lemmatized_wordlist(arr):
	# arr is tokenized already
	l = []
	for word in arr:
		l.append(lemmatizer.lemmatize(word))
	return l


f = open("facts.pl", "w")

# read input for the branch/department of student, then preprocess it
inp1 = input("What is your branch/department ?\n: ")
text = get_lower_case(inp1)
text = get_non_punctuated_words(text)
l = get_tokenized_list(text)
l = get_non_stopword_list(l)
l = get_lemmatized_wordlist(l)


# write down the fact of department/1 in the prolog file facts.pl
if 'cse' in l:
	f.write("department('CSE').\n")
else:
	f.write("department('Non-CSE').\n")


# read the input for all the interest areas of the student, then preprocess it
inp2 = input("What are your interest areas ?\n: ")
text = get_lower_case(inp2)
text = get_non_punctuated_words(text)
l = get_tokenized_list(text)
l = get_non_stopword_list(l)
l = get_lemmatized_wordlist(l)


# write down the fact of interest/1 in the prolog file facts.pl
if ('machine' in l) or ('learning' in l) or ('ml' in l) or ('ai' in l) or ('artificial' in l) or ('intelligence' in l):
	f.write("interest('Machine Learning').\n")
if ('networking' in l) or ('network' in l) or ('security' in l):
	f.write("interest('Networking').\n")
if ('database' in l) or ('dbms' in l) or ('information' in l):
	f.write("interest('Databases').\n")
if ('algorithm' in l) or ('structure' in l) or ('dsa' in l) or ('coding' in l):
	f.write("interest('Algorithms').\n")
if ('biology' in l) or ('gastronomy' in l) or ('medicine' in l) or ('doctor' in l):
	f.write("interest('Biology').\n")
if ('designing' in l) or ('animation' in l) or ('graphics' in l):
	f.write("interest('Design').\n")
if ('social' in l) or ('politics' in l) or ('ssh' in l) or ('ev' in l) or ('environmental' in l) or ('sociology' in l):
	f.write("interest('Social Science').\n")
if ('electronics' in l) or ('signal' in l) or ('digital' in l) or ('circuit' in l):
	f.write("interest('Electronics').\n")


# read the input for the grading policy the student prefers, then preprocess it
inp3 = input("Do you prefer relative grading or absolute grading ?\n: ")
text = get_lower_case(inp3)
text = get_non_punctuated_words(text)
l = get_tokenized_list(text)
l = get_non_stopword_list(l)
l = get_lemmatized_wordlist(l)


# write down the fact of relative/1 in prolog file facts.pl
if 'relative' in l:
	f.write("grading('relative').\n")
else:
	f.write("grading('absolute').\n")


# read all the courses the student has done previously, then preprocess it
all_prereqs = ['cse201', 'cse222', 'ece250', 'cse232', 'cse121', 'cse102', 'cse231', 'mth100', 'cse202', 'mth201', 'cse101']
inp4 = input("Enter the course-codes of the courses you have done\n: ")
text = get_lower_case(inp4)
text = get_non_punctuated_words(text)
l = get_tokenized_list(text)
l = get_non_stopword_list(l)
l = get_lemmatized_wordlist(l)

arr = []
for word in l:
	if word in all_prereqs:
		arr.append(word.upper())

# write down the fact of courses_done/1 in prolog file facts.pl
f.write('courses_done('+str(arr)+').')
f.close()