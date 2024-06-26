# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
# SIN ACTUALIZAR POR ERROR 

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered a comment:",data)
        pos = self.getpos()
        print("At line:", pos[0],"position",pos[1])

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        print("Encountered a comment:",data)
        pos = self.getpos()
        print("At line:", pos[0],"position",pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("/workspaces/learning-python-2896241/Ch5 - Internet Data/samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)    

if __name__ == "__main__":
    main()
  