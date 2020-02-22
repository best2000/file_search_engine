import os, pickle 

def read_index(root_path):
    #get file index from path
    file_index = [(path, files) for r, _, f in os.walk(root_path)]

    #save files index to file_index.pkl
    with open("file_index.pkl", 'wb') as f:
        pickle.dump(file_index, f)

def search(key, search_type, f_ex):
    #load file_index.pkl
    with open("file_index.pkl", 'rb') as f:
        file_index = pickle.load(f)
    
    #search
    all = 0
    match = 0
    result = []
    for path, files in file_index:
        for f in files:
            all += 1
            #remove file extension from name
            if f_ex == False:
                f2 = os.path.splitext(f)[0]
            else:
                f2 = f
            #search by search_type
            if key == f2: #it the same
                    match += 1
                    result.append(path+"/"+f)
            elif (search_type == "contain" or search_type == None): #contain keyword  
                if (key in f2) == True:
                    match += 1
                    result.append(path+"/"+f)
            elif (search_type == "startwith"): #start with keyword
                if f2.find(key) == 0: 
                    match += 1
                    result.append(path+"/"+f)
            elif (search_type == "endwith"): #end with keyword
                f_len = len(f2)
                key_len = len(key)
                key_start_index = f2.find(key, f_len-key_len-1, f_len)
                if (key_start_index != -1): 
                    match += 1
                    result.append(path+"/"+f)
    
    print(">> found", match, "out of", all, "files")
    for i in result:
        print(">>", i)

    
#read_index("C:/CODE/file_search_engine")
search("ol", "endwith", False)