
arraySize = 24
lines = 2

with open(f"array{arraySize}.txt", "w") as file:
    file.write("ArraySet:\n")
    file.write(f"\top mul offset arrayIndex {lines}\n")
    file.write("\top add @counter @counter offset\n\n")
    for i in range(arraySize):
        file.write(f"\tset value{i} value\n")
        file.write("\tset @counter callback\n")
    file.write("\n")
        
    file.write("ArrayGet:\n")
    file.write(f"\top mul offset arrayIndex {lines}\n")
    file.write("\top add @counter @counter offset\n\n")
    for i in range(arraySize):
        file.write(f"\tset value value{i}\n")
        file.write("\tset @counter callback\n")
    file.write("\n")
    
    file.write("ArrayClear:\n")
    file.write("\top add @counter @counter arrayIndex\n\n")
    for i in range(arraySize):
        file.write(f"\tset value{i} value\n")
    file.write("\tset @counter callback\n")
    file.write("\n")
    
    file.write("MoveUp:\n")
    file.write(f"\top mul offset arrayIndex {lines}\n")
    file.write("\top add @counter @counter offset\n\n")
    for i in range(0, arraySize - 2):
        currentI = i
        file.write(f"\tset value{currentI} value{currentI + 1}\n")
        file.write(f"\tjump EndMoveUp lessThanEq last {currentI}\n")
        
    currentI = currentI + 1
    file.write(f"\tset value{currentI} value{currentI + 1}\n")
    file.write("\tEndMoveUp:\n")
    file.write("\t\tset @counter callback\n")
    file.write("\n")  
    
    file.write("MoveDown:\n")
    ## op add next arrayIndex 1
        #op add last last 1
        #op sub offset length last
        #op mul offset offset 2
        #op add @counter @counter offset 
    ##
    file.write(f"\top add last last 1\n")
    file.write(f"\top sub offset maxIndex last\n")
    file.write(f"\top mul offset offset {lines}\n")
    file.write("\top add @counter @counter offset\n\n")
    for i in range(0, arraySize -1):
        currentI = arraySize - i - 1
        file.write(f"\tset value{currentI} value{currentI - 1}\n")
        file.write(f"\tjump EndMoveDown greaterThanEq arrayIndex {currentI}\n")
        
    file.write("\tEndMoveDown:\n")
    file.write("\t\tset @counter callback\n")
    file.write("\n")  
    
    file.write("FindInsertSpot:\n")
    for i in range(arraySize):
        file.write(f"\tset found {i}\n")
        file.write(f"\tjump Found strictEqual value{i} null\n")
        file.write(f"\tjump Found greaterThan value{i} value\n")
        
    
    file.write("\n")  
    file.write("NotFound:\n")
    file.write("\tset found -1\n")
    file.write("\n")  
    
    file.write("Found:\n")
    file.write("\tset @counter callback\n")
    file.write("\n")  
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    