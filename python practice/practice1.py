
fruits=[" MANGO ","CHERRY", "@#Bananas@!", "grapes"]

def clean(x):
    return x.strip(' @!%$#').capitalize()
fruits=[" MANGO ","CHERRY", "@#Bananas@!", "grapes"]
fruits=[clean(i) for i in fruits]
print(fruits)
