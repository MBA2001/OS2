
def get_frames():
    while(1):
        frames = input("enter the number of frames: ")
        if frames.isnumeric():
            return int(frames)
        else:
            print('please enter a valid input')

def get_pages():
    pages = input("Enter a string containing numbers and spaces or commas inbetween\nEx: 1 2 3 4 5\nEx2: 1,2,3,4,5\n")
    if ',' in pages:
        return pages.strip().split(',')
    else:
        return pages.strip().split(' ')

def get_operation():
    while(1):
        x = input("1. FIFO\n2. LRU\n3. Optimal\n")

        if int(x) == 1 or int(x) == 2 or int(x) == 3:
            return int(x)
        else:
            print('please enter a valid number\n')


if __name__ == '__main__':
    number_of_frames = get_frames()
    pages = get_pages()
    pages =  [int(i) for i in pages]
    operation = get_operation()
    number_of_faults = 0
    frames = []
    size = 0

    if operation == 1:
        #* FIFO
        index = 0
        for i in range(len(pages)):
            if pages[i] not in frames:
                # size < number of frames ya3ni lessa fy frames fadya nzawed fiha
                if size < number_of_frames:
                    frames.append(pages[i])
                    size+=1
                    number_of_faults+=1
                #law mafish frames fadya ben7ot elpage dy mkan elindex elwa2ef 3and el First w nzawed elindex wa7ed
                else:
                    frames[index] = pages[i]
                    index+=1
                    if index  == size:
                        index =0
                    number_of_faults+=1
    
    elif operation == 2:
        #* LRU
        
        mru = []
        temp_size = 0
        for i in range(len(pages)):
            if pages[i] not in frames:
                if size < number_of_frames:
                    frames.append(pages[i])
                    size +=1
                    number_of_faults+=1
                    if temp_size < number_of_frames-1:
                        mru.append(pages[i])
                        temp_size+=1
                    elif temp_size == number_of_frames -1:
                        mru.pop(0)
                        mru.append(pages[i])
                else:
                    for j in range(len(frames)):
                        if frames[j] not in mru:
                            frames[j] = pages[i]
                            number_of_faults+=1
                            break
                    mru.pop(0)
                    mru.append(pages[i])
            else:
                if pages[i] not in mru:
                    mru.pop(0)
                    mru.append(pages[i])
                else:
                    mru.pop(mru.index(pages[i]))
                    mru.append(pages[i])
    elif operation == 3:
        #* Optimal
        for i in range(len(pages)):
            if pages[i] not in frames:
                if size < number_of_frames:
                    frames.append(pages[i])
                    size +=1
                    number_of_faults+=1
                else:
                    temp = list(frames)
                    found = False
                    for j in range(i,len(pages)):
                        if pages[j] in temp:
                            temp.pop(temp.index(pages[j]))
                            if len(temp) == 1:
                                found = True
                                frames[frames.index(temp[0])] = pages[i]
                                number_of_faults+=1
                                break
                    if not found:
                        frames[frames.index(temp[0])] = pages[i]
                        number_of_faults+=1
    print('Number of page faults: ',number_of_faults)
    print('Memory:',frames)
            
                
