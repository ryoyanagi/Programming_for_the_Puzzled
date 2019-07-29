def runLength(hugou):							
    before = []							
    after = []							
    char_after = []							
    scan_s = 0							
    append_num = 0							
    count = 0							
    before = list(hugou)							
    if(before[scan_s].isalpha() == True):							
        for i in range(0,len(before)):							
                if(before[scan_s] == before[i]):							
                    append_num += 1							
                else:							
                    after.append((scan_s,append_num,before[scan_s]))							
                    scan_s = i + 1							
                    append_num = 1							
        #仮にaaabbbcccの時、cのパターンがafterに追加する文を通らないため							
        #forの終わりに最後のパターンをappendする							
        after.append((scan_s,append_num,before[scan_s]))							
							
        for i in range(len(after)):							
            char_after.append(str(after[i][1]))							
            char_after.append(str(after[i][2]))							
        result = ''.join(char_after)							
							
    else:							
        for i in range(0,len(before)):							
            if(before[i].isalpha() == False):							
                count += 1							
                if(count == 2):							
                    append_num += (append_num*10 - append_num)							
                    append_num += int(before[i])							
                else:							
                    append_num = int(before[i])							
            elif(before[i].isalpha() == True):							
                for j in range(append_num):							
                    after.append(before[i])							
                count = 0							
                append_num = 0							
        result = ''.join(after)							
							
    print(result)							
