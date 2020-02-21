import os
import pickle
from typing import Dict

class SearchEngine:
    ''' Create a search engine object '''

    def __init__(self):
        self.file_index = [] # directory listing returned by os.walk()
        self.results = [] # search results returned from search method
        self.matches = 0 # count of records matched
        self.records = 0 # count of records searched


    def create_new_index(self, values: Dict[str, str]) -> None:
        ''' Create a new file index of the root; then save to self.file_index and to pickle file '''
        root_path = values['PATH']
        self.file_index: list = [(root, files) for root, dirs, files in os.walk(root_path) if files]

        # save index to file
        with open('file_index.pkl','wb') as f:
            pickle.dump(self.file_index, f)


    def load_existing_index(self) -> None:
        ''' Load an existing file index into the program '''
        try:
            with open('file_index.pkl','rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = []


    def search(self, values: Dict[str, str]) -> None:
        ''' Search for the term based on the type in the index; the types of search
            include: contains, startswith, endswith; save the results to file '''
        self.results.clear()
        self.matches = 0
        self.records = 0
        term = values['TERM']

        # search for matches and count results
        for path, files in self.file_index:
            for file in files:
                self.records +=1
                if (values['CONTAINS'] and term.lower() in file.lower() or 
                    values['STARTSWITH'] and file.lower().startswith(term.lower()) or 
                    values['ENDSWITH'] and file.lower().endswith(term.lower())):

                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)
                    self.matches +=1
                else:
                    continue 
        
        # save results to file
        with open('search_results.txt','w') as f:
            for row in self.results:
                f.write(row + '\n')

def fst():
    s = SearchEngine()
    s.create_new_index('C:/CODE/file_search_engine') #for first time
    s.search("lol")
    print('>> {:,d} mathes out of {:,d} records searched.'.format(s.matches, s.records))
    for match in s.results:
        print("  >>", match)

def sec():
    s = SearchEngine()
    s.load_existing_index() #for second time
    s.search("lol")
    print('>> {:,d} mathes out of {:,d} records searched.'.format(s.matches, s.records))
    for match in s.results:
        print("  >>", match)
