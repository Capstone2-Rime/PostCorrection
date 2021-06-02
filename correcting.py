import textdistance  # pip install textdistance
import hgtk #pip install hgtk



def checkYH(caption,data):
    spliter='ᴥ'
    caption_list=caption.split(spliter)
    data_list=caption.split(spliter)
    try:
        #caption_list=hgtk.text.decompose(caption).split(spliter)
        #data_list=hgtk.text.decompose(data).split(spliter)

        result=False

        for i in range(min(len(caption_list)-1,len(data_list)-1)):
            if(caption_list[i][0]=='ㅇ' and  data_list[i][0]=='ㅎ'):
                caption_list[i]='ㅎ'+caption_list[i][1:]
                result=True
    except:
        result=False

    return_value=spliter.join(caption_list)
    return_value=hgtk.text.compose(return_value)


    return result,return_value

def checkae(caption,data):
    spliter='ᴥ'
    caption_list=caption.split(spliter)
    data_list=caption.split(spliter)
    try:
        #caption_list=hgtk.text.decompose(caption).split(spliter)
        #data_list=hgtk.text.decompose(data).split(spliter)

        result=False
        #print(min(len(caption_list)-1,len(data_list)-1))
        for i in range(min(len(caption_list)-1,len(data_list)-1)):
            if(caption_list[i][1]=='ㅏ' and  data_list[i][1]=='ㅓ'):
                caption_list[i]=caption_list[i][0]+'ㅓ'+caption_list[i][2:]
                result=True
            elif(caption_list[i][1]=='ㅓ' and  data_list[i][1]=='ㅏ'):
                caption_list[i]=caption_list[i][0]+'ㅏ'+caption_list[i][2:]
                result=True
    except:
        result=False
    return_value=spliter.join(caption_list)
    return_value=hgtk.text.compose(return_value)

    return result,return_value

def checkou(caption,data):
    spliter='ᴥ'
    caption_list=caption.split(spliter)
    data_list=caption.split(spliter)
    try:
        #caption_list=hgtk.text.decompose(caption).split(spliter)
        #data_list=hgtk.text.decompose(data).split(spliter)

        result=False
        #print(min(len(caption_list)-1,len(data_list)-1))
        for i in range(min(len(caption_list)-1,len(data_list)-1)):
            if(caption_list[i][1]=='ㅜ' and  data_list[i][1]=='ㅡ'):
                caption_list[i]=caption_list[i][0]+'ㅡ'+caption_list[i][2:]
                result=True
            elif(caption_list[i][1]=='ㅡ' and  data_list[i][1]=='ㅜ'):
                caption_list[i]=caption_list[i][0]+'ㅜ'+caption_list[i][2:]
                result=True
    except:
        result=False
    return_value=spliter.join(caption_list)
    return_value=hgtk.text.compose(return_value)

    return result,return_value

def checkEndStart(caption,data):
    spliter='ᴥ'
    caption_list=caption.split(spliter)
    data_list=caption.split(spliter)
    try:
        #caption_list=hgtk.text.decompose(caption).split(spliter)
        #data_list=hgtk.text.decompose(data).split(spliter)

        result=False
        for i in range(min(len(caption_list)-2,len(data_list)-2)):
            if(len(caption_list[i])<3 or len(data_list[i])<3):
                continue
            if(caption_list[i][2]=='ㅂ' and  data_list[i][2]=='ㅂ'):
                if((caption_list[i+1][0]=='ㅂ' or caption_list[i+1][0]=='ㅍ')and caption_list[i+1][1]=='ㅡ'):
                    caption_list[i+1]='ㅇ'+caption_list[i+1][1:]
                    result=True
            if(caption_list[i][2]=='ㄷ' and  data_list[i][2]=='ㄷ'):
                if((caption_list[i+1][0]=='ㄷ' or caption_list[i+1][0]=='ㅌ')and caption_list[i+1][1]=='ㅡ'):
                    caption_list[i+1]='ㅇ'+caption_list[i+1][1:]
                    result=True
            if(caption_list[i][2]=='ㄱ' and  data_list[i][2]=='ㄱ'):
                if((caption_list[i+1][0]=='ㄱ' or caption_list[i+1][0]=='ㅋ')and caption_list[i+1][1]=='ㅡ'):
                    caption_list[i+1]='ㅇ'+caption_list[i+1][1:]
                    result=True
    except:
        result=False

    return_value=spliter.join(caption_list)
    return_value=hgtk.text.compose(return_value)
    return result,return_value

def checkNiuen(caption,data):
    spliter='ᴥ'
    caption_list=caption.split(spliter)
    data_list=caption.split(spliter)
    #caption_list=hgtk.text.decompose(caption).split(spliter)
    #data_list=hgtk.text.decompose(data).split(spliter)
    try:
        result=False
        for i in range(min(len(caption_list)-2,len(data_list)-2)):
            if(len(caption_list[i])<3 or len(data_list[i])<3):
                continue
            if((caption_list[i][2]=='ㄴ' and  data_list[i][2]=='ㄴ')and caption_list[i+1][1]=='ㅡ'):
                if(caption_list[i+1][0]=='ㄴ'):
                    caption_list[i+1]='ㅇ'+caption_list[i+1][1:]
                    result=True
    except:
        result=False
    return_value=spliter.join(caption_list)
    return_value=hgtk.text.compose(return_value)
    return result,return_value




# distance가 구해졌다고 가정




# 마지막에 수정된 자막에 대한 튜플은 디비 저장 및 클라이언트에 전송될 예정
