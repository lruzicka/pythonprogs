import os

class Structure: # This holds the directory structure beginning the current dir.
    def __init__(self,path):
        self.structure = {} # Gets the directory structure
        for root,dirs,files in os.walk(path):
            self.structure[root] = files
        self.paths = {}
        for directory in self.structure.keys(): # Creates list of files as keys and their paths.
            files = self.structure[directory]
            for file in files:
                path = os.path.join(directory,file)
                self.paths[file] = path
    
    def showDirs(self): # Returns all directories in the tree.
        dirs = []
        for directory in self.structure.keys():
            dirs.append(directory)
        return(dirs)

    def showFiles(self,path): # Returns all files in a given directory.
        files = self.structure[path]
        return(files)

    def showAllPaths(self): # Returns a list of all paths in the structure.
        paths = []
        for file in self.paths.keys():
            paths.append(self.paths[file])
        return(paths)

    def expandFilePath(self,file): # Returns a path for the given file.
        path = self.paths[file]
        return(path)


class File: # This holds the info about the module (from tags)
    def __init__(self,file,structure):
        self.filename = file
        self.info = {}
        self.filepath = structure.expandFilePath(file)
        with open(self.filepath) as module:
            lines = module.readlines()
        for line in lines:
            if ":" in line:
                data = line.split(":")
                data = data[1:]
                
                value = data[1].strip()
                if data[0] == "rhid":
                    self.info["rhid"] = value
                elif data[0] == "type":
                    self.info["type"] = value
                elif data[0] == "used":
                    self.info["used"] = value
                elif data[0] == "prev":
                    self.info["prev"] = value
                elif data[0] == "next":
                    self.info["next"] = value
                else:
                    pass

    def expandInfo(self):
        info = ["File: "+self.filename, 
                "rhid: "+ self.info["rhid"],
                "type: "+ self.info["type"],
                "used: "+ self.info["used"],
                "prev: "+ self.info["prev"],
                "next: "+ self.info["next"]
                ]
        info = "\n".join(info)
        return(info)

    def showInfo(self,info):
        if info == "rhid":
            out = self.info["rhid"]
        elif info == "type":
            out = self.info["type"]
        elif info == "used":
            out = self.info["used"]
        elif info == "prev":
            out = self.info["prev"]
        elif info == "next":
            out = self.info["next"]
        else:
            out = "Tag not implemented."
        return(out)



class Assembly:
    def __init__(self,structure):
        pass
        
            

dirs = Structure(".")

f = File("fire-and-ice.adoc",dirs)
print(f.showInfo('next'))
