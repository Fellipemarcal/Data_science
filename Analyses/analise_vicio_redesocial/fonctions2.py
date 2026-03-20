def cls_age(i):
    if i < 26.5:
        return 'Plus Jeune'
    else:
        return 'Adulte'
#appel la fonction avec apply -> df['Classe_age'] = df['Age'].apply(cls_age)

def intrct (i):
    if i > 245.25 and i < 32:
        return 'Très Haute'
    elif i > 165.50 and i < 245.25:
        return 'Haute'
    elif i > 85.75 and i < 165.50:
        return 'Normal'
    elif i > 6 and i < 85.75:
        return 'Baisse'