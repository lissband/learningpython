def merger(*files):
    filelist = [f for f in files]
    with open('merged_file.txt','a') as merged:
        for content in filelist:
            write_object = open(str(content),'r')
            merged.write(str(write_object.readlines()))
            merged.write('\nend of file\n')
    return None
merger('anim1.txt','anim2.txt','anim3.txt')