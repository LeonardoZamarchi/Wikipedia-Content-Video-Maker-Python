from re import search



def start():
    def pergunta_termo():
        print('Type a Wikipedia search term: ')
        termo = input()
        return termo

    def pergunta_prefix():
        prefix = ['Who is', 'What is', 'The history of']
        for i in prefix:
            print(str(prefix.index(i))+ ' '+ i)
        sel_prefix = int(input())
        return prefix[sel_prefix]    
    
    content = {}
    content['searchTerm'] = pergunta_termo()
    content['prefix'] = pergunta_prefix()
    content['text_wiki'] = txt_bot.bot(content['searchTerm'])
    
    print(content)



start()