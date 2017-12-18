"""
A set of methods to compute RAI
"""

def age_map(age,cancer):
    """
    A method to return the rai score w/ and w/o cancer
    """
    ranges = [(0,70),(70,75),(75,80),(80,85),(85,90),(90,95),(95,100),(100,150)]
    scores = [(2,20),(3,19),(4,18),(5,17),(6,15),(7,14),(8,14),(9,13)]
    found = True
    while found:
        for i,r in enumerate(ranges):
            if age in range(ranges[i][0],ranges[i][1]):
                s=scores[i]
                found = False
                break
    return s[cancer]


def get_adl(adl_score,cog):
    """
    A method to  compute adl corrected fo cognition
    """
    ranges = [(0),(1,2),(3,4),(5,6,7),(8,9),(10,11),(12,13),(14,15,16)]
    modifier = [-2,-1,0,1,2,3,4,5]
    #
    found = True
    while found:
        for i,r in enumerate(ranges):
            print(adl_score,range[i])
            if adl_score in ranges[i]:
                adl_score = adl_score+modifier[i]
                found = False
                break
    return adl_score

def get_rai(form):
    """
    A method to compute rai from the form:
    """
    age_score = age_map(int(form.data['age']),int(form.data['cancer']))
    #
    co_morbid = ['weight_loss','nephrologist','chf', 'appetite', 'sob',]
    co_morbid_features = [int(form.data[r]) for r in co_morbid]
    co_morbid_vals = [5,6,4,4,8]
    co_morbid_score = sum([i[0]*i[1] for i in zip(co_morbid_features,co_morbid_vals)])
    #
    snf_score = int(form.data['snf'])*8
    #
    adl =  ['mobility','eating','toileting','hygiene']
    adl_score = sum([int(form.data[r]) for r in adl])
    cog = int(form.data['memory'])
    print(cog)
    #if cog:
    #    adl_score = get_adl(adl_score,cog)
        
    #    
    return co_morbid_score+age_score+adl_score+snf_score

    
