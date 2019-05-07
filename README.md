# Text_cleaning_arabic_TCAR
Text cleaning for arabic tweets in python



Description:

Text cleaning for Arabic tweets (or any kind of social media platforms) that will manage Harakat,suffix and prefix and similar letters like (آ ا) or (ي ى) and solve emoji's split too [😷😷😷] = [😷,😷,😷] insted of making them as one [😷😷😷].


prerequisite:

install:

    emoji
    pyarabic





Example:
    
    import TCAR
    word = 'وأعجبُ كيف يُغريني طريقي، وموتِي فيهِ أقربُ من نجاحي😷😷😷 .'
    
Functions: 

1- clean(): 
clean the sentence from Harakat, one letters and punctuation.
    
    TCAR.clean(word)
    
Result:

    'وأعجب كيف يغريني طريقي وموتي فيه أقرب من نجاحي 😷😷'
    
2- split_emoji():
splitting the sentence and managing the emoji splitting part.

    TCAR.split_emoji(word)
    
Result:

    ['وأعجبُ','كيف','يُغريني','طريقي،','وموتِي','فيهِ','أقربُ','من','نجاحي','😷','😷','😷','.']
     
     
     
3- TCAR.norm(): 
manage the similar letters.


    TCAR.norm(word)

Result:

    'واعجبُ كيف يُغريني طريقي، و موتِي فيهِ اقربُ من نجاحي😷😷😷 .'



4- TCAR.numb():
handale arabic number and switch them to english + split the numbers from text.

    word = 'وأعجبُ١ كيف1 يُغريني طريقي، و موتِى فيهِ أقربُ من نجاحي😷😷😷 .'
    TCAR.numb(word)
    
Result:

    'وأعجبُ 1 كيف 1 يُغريني طريقي، و موتِى فيهِ أقربُ من نجاحي😷😷😷 .'



