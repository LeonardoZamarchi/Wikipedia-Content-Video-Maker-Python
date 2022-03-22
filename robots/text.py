import wikipedia
import pysbd


def bot(cont):
    def get_from_wikipedia(term):
        conteudo = wikipedia.page(term, auto_suggest=False)
        return conteudo.content

    def sanitize_content(text):
        text = text.split('\n')        
        for i in text:
            i = i.replace('\\','')
            if len(i.replace(' ','')) <= 1:
                text.remove(i)   
            if i.find('==')>0:
                text.remove(i)
        sanitized = []     
        for i in text:
            seg = pysbd.Segmenter(language='en',clean=False)
            sanitized.append(seg.segment(i))
        return sanitized
    wiki_ret = get_from_wikipedia(cont)
    sanitize_ret = sanitize_content(wiki_ret)

    return sanitize_ret
    