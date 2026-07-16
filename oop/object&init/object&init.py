class Factory:
    def __init__(self,material,zip,pockets):
        self.material = material
        self.zip = zip
        self.pockets = pockets

prada = Factory("lather","aluminium",4)
print(Factory('cotton','still',3).material)

print(prada.zip)