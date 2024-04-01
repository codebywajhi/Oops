# def send_data(file_name="./cmd.txt", content="This is my new data which is going to help you in every moment!"):
#     try:
#         with open(file_name, "w") as file:
#             file.write(content)
#             print(f"Content has been written to the {file_name} file.")
#             return f"Successfully written! {file_name} "
#     except IOError as e:
#         print(f"Error writing to {file_name}: {e}")

# for read 

# def read_file(file_path = "cmd.py"):
#     try:
#         with open(file_path) as file:
#          content = file.read()
#          print(f"Your file has been rad")
#          print(content)
#          return "working"
#     except IOError as e:
#         print(f"Error reading file  {file_path} : {e} ")

f = open("wajhi.txt")
content = f.read()
print(content)
