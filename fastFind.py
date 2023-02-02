import sys, webbrowser, bs4, requests, urllib.parse
if len(sys.argv) >= 2:
    
    print("googling......")
    req = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))

    
    if '-t' not in sys.argv:
        number_of_links = 3
    else:
        t_index = sys.argv.index('-t')
        number_of_links = int(sys.argv[t_index+1])
        
        
        
     
    

    req.raise_for_status()

    soup = bs4.BeautifulSoup(req.text)

    linkElems = soup.select('.egMi0.kCrYT a')

    linkElems = linkElems[:number_of_links]



    for link in linkElems:
        encoded_url = str(link.get('href'))
        parsed = urllib.parse.urlparse(encoded_url)
        query = urllib.parse.parse_qs(parsed.query)
        actual_url = query["q"][0]
        webbrowser.open_new_tab(actual_url)
        
else:
    print('''usage :
          
          description: open multiple tabs of searched string.......c
          python3 lucky.py [search string]
        ''')


