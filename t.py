import os, pickle 

def read_index(root_path):
    #get file index from path
    file_index = [(path, files) for r, _, f in os.walk(root_path)]

    #save files index to file_index.pkl
    with open("file_index.pkl", 'wb') as f:
        pickle.dump(file_index, f)

def search(key, search_type):
    #load file_index.pkl
    with open("file_index.pkl", 'rb') as f:
        file_index = pickle.load(f)
    
    #search
    all = 0
    match = 0
    result = []
    for path, files in file_index:
        if (search_type == "contain" or search_type == None):
                for f in files:
                    all += 1
                    if (key in f) == True:
                        match += 1
                        result.append(path+"/"+f)
        elif (search_type == "startwith"):
            pass
        elif (search_type == "endwith"):
            pass
    
    print(">> found", match, "out of", all, "files")
    for i in result:
        print(">>", i)

    
#read_index("C:/CODE/file_search_engine")
search("t", "contain")