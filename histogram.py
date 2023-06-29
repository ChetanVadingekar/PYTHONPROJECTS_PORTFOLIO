def histogram():
    # Getting input from the user
    char = input("Please enter on of charcter ['@','#','$','*','^']: ")
    # Initializing histogram format
    hsitogram_format = [2,5,6,3]
    
    for ele in hsitogram_format:
        print(char * ele, sep=' ')

histogram()