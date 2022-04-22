def solution(new_id):
    new_id = new_id.lower()
    
    new_id_after2 = ''
    for x in new_id:
        set_ = {'-', '_', '.'}   
        if 'a' <= x <= 'z' or '0' <= x <= '9' or x in set_:
            new_id_after2 += x
        
    new_id_after3 = new_id_after2[0]
    for idx in range(1, len(new_id_after2)):   
        if new_id_after2[idx] == '.' and new_id_after2[idx-1] == '.':
            continue
        new_id_after3+=new_id_after2[idx]
    
    new_id_after4 = new_id_after3.strip('.')
    
    new_id_after5 = new_id_after4
    if len(new_id_after5) == 0:
        new_id_after5 = 'a'

    new_id_after6 = new_id_after5
    if len(new_id_after5) > 15:
        new_id_after6 = new_id_after5[:15].strip('.')
    
    new_id_after7 = new_id_after6
    while (len(new_id_after7) < 3 ):
        new_id_after7 += new_id_after7[-1]
        
     
    return new_id_after7