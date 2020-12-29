import read_user_input as read


def main():
    name = read.rstring("Enter your name:")
    description = read.rstring("Enter a description of yourself:")
    outfile = open("webpage.html", 'w')
    outfile.write("<html>" + "\n")
    outfile.write("<head>" + "\n")
    outfile.write("</head>" + "\n")
    outfile.write("<body>" + "\n")
    outfile.write("<center>" + "\n")
    outfile.write("<h1>" + name + "</h1>" + "\n")
    outfile.write("</center>" + "\n")
    outfile.write("<hr />" + "\n")
    outfile.write(description + "\n")
    outfile.write("<hr />" + "\n")
    outfile.write("</body>" + "\n")
    outfile.write("</html>" + "\n")
    outfile.close()
    print("Data has been written to \'webpage.html\'")


main()
