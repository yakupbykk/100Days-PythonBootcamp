from rembg import remove

input_path = "image.jpeg"
output_path= "output.png"

with open(input_path,"rb") is i:
    with open(output_path,"wb") as o:
        input_file = i.read()
        putput_file = remove(input_file)
        o.write(output_file)