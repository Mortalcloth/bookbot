def get_book_text(book):
    with open(book) as j:
        contents = j.read()
    return contents



def count_words(book_path):
    text_output = get_book_text(book_path)
    text_list = text_output.split()
    counter = 0
    for i in range(0,len(text_list)):
        counter += 1
    print(f"{counter} words found in the document")



def count_characters(string):
    lowercase = f"{string}".lower()
    counter_dic = {}
    for i in lowercase:
        if i in counter_dic:
            counter_dic[i] += 1
        else:
            counter_dic[i] = 1
    print(counter_dic)

def 
