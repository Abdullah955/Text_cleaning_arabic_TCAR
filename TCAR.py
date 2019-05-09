import re
import string
import pyarabic.araby as araby
import functools
import operator
import re
import emoji


# Define the printable need to be removed from the text:
string.printable = string.printable + '١٢٣٤٥٦٧٨٩٠؟،؛' + '…' + '🇦' + '🇸' + '🇩' \
    + '🇫' + '🇰' + '🇷' + '🇼' + '🇦' + '🇭' + '🇲' + '🇹' + '🇾' + '٪'

string.punctuation = string.punctuation + '،؟،؛'


table_printable = str.maketrans(string.printable, ' ' * len(string.printable))
table_punctuation = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

# define the Harakat:
re_hamzated_alif = re.compile(r'[\u0622\u0623\u0625]')
re_alifMaqsura = re.compile(r'[\u0649]')
re_taaMarbota = re.compile(r'[\u0629]')
re_waw_hamzah = re.compile(r'[\u0624]')
re_alifMaqsurawithHamzah = re.compile(r'[\u0626]')




# norm will be used to clean similar letters that might be written in two different ways.
# Examples:
# آ ا
# ي ى

def norm(token):
    
    """
        normalize the word by replacing hamzated Alif
        with Alif replacing AlifMaqsura with Yaa and replacing Taa Marbota with Haa
        """
    
    # replace Hamzated Alif with Alif bare
    token = re_hamzated_alif.sub('\u0627', token)
    # replace alifMaqsura with Yaa
    token = re_alifMaqsura.sub('\u064A', token)
    # replace Taa Marbota with Haa
    token = re_taaMarbota.sub('\u0647', token)
    # replcae waw hamzah with normal waw
    token = re_waw_hamzah.sub('\u0648' , token)
    token = re_alifMaqsurawithHamzah.sub('\u064A' , token)
    
    return token





# clean function will clean the arabic text from any other characters ( punctuations , numbers or one letter words. ( wow letter will be removed too :( ! )
def clean(words,punctuations=False,printable=False,hashtag=True):
    
    #Split joins letters Hell4 to [Hello ,4]
    words = re.split(r'([a-zA-Z]+)', words)
    words = ' '.join(words)
    words = re.split('(\d+)',words)
    words = ' '.join(words)
    
    # Remove maddah
    words = araby.strip_tatweel(words)
        
        # Here we use (split) to split on spaces (tokenize will split the hashtag words)
    words = words.split()
        
    wordsCopy = words.copy()
            
    for word in wordsCopy:
        # Remove one letter
        if len(word.strip(string.printable)) == 1:
            if word.isalpha():
                words.remove(word)
        # Remove Hashtags.
        elif hashtag and ( word.startswith('#') or word.endswith('#') ):
                words.remove(word)

    words = ' '.join(words)
            # Remove redundant letters (more than 2)
    words = re.sub(r'(.)\1{2,}', r'\1\1', words)
            
            # Remove Harakat
    words = araby.strip_tashkeel(words)


    if printable:
        # Remove string.printable
        # string.printable = 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!
        #"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        words = words.translate(table_printable)

    if punctuations:
        # Remove  #"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
        words = words.translate(table_punctuation)
        

            # Here we should use tokenize to split emoji from words
    wordsafterclean = araby.tokenize(words)
    return ' '.join(wordsafterclean)







# remove emojis from text.
def remove_emoji(em):
    
    em_split_emoji = emoji.get_emoji_regexp().split(em)
    em_split_whitespace = [substr.split() for substr in em_split_emoji]
    em_split = functools.reduce(operator.concat, em_split_whitespace)
    for i in em_split.copy():
        if i in emoji.UNICODE_EMOJI:
            em_split.remove(i)

    return ' '.join(em_split)


# split emoji from text.
def split_emoji(em):
    
    em_split_emoji = emoji.get_emoji_regexp().split(em)
    em_split_whitespace = [substr.split() for substr in em_split_emoji]
    em_split = functools.reduce(operator.concat, em_split_whitespace)
    em_split = ' '.join(em_split)
    
    return em_split






# numb will split numbers from words and switch Arabic numbers to english.
def numb(word):
    
    word = re.split('(\d+)',word)
    word = ' '.join(word)
    words = word.split()
    for i, w in enumerate(words):
        if w == '١':
            words[i] = '1'
        elif w == '٢':
            words[i] == '2'
        elif w == '٣':
            words[i] == '3'
        elif w == '٤':
            words[i] == '4'
        elif w == '٥':
            words[i] == '5'
        elif w == '٦':
            words[i] == '6'
        elif w == '٧':
            words[i] == '7'
        elif w == '٨':
            words[i] == '8'
        elif w == '٩':
            words[i] == '9'

    word = ' '.join(words)
    
    return word



