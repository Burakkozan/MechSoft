def tersçevir(s):
    c= eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
    words = c.split(' ') 
    reverse_sentence = ' '.join(reversed(words)) 
    return reverse_sentence 
print(tersçevir("(nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon ,tsilanruoj (and) laicos .tsivitca )"))