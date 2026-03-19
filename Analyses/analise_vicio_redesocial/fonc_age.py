def cls_age(i):
    if i < 26.5:
        return 'Plus Jeune'
    else:
        return 'Adulte'
#appel la fonction avec apply -> df['Classe_age'] = df['Age'].apply(cls_age)