for i in range(2,20):
    print(f"Writing the table of {i} in file")
    filename=f"table_{i}.txt"
    path=f"file_handling/tables2/{filename}"
    with open(path,"a") as f:
        for k in range(1,11):
            f.write(f"{i}*{k}={i*k}\n")