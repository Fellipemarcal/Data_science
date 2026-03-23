def snt_mnt(i):
    if i >= 73.75 and i <= 90 :
        return 'Bonne santé'
    elif i >= 57.50 and i <= 73.75 :
        return 'Santé stable'
    elif i >= 41.25 and i <= 57.50:
        return 'Santé en attention'
    elif i >= 25 and i <= 41.25 :
        return 'Mauvaise Santé'