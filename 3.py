
tome = 0

def cont(pos):
    def umn(step):
        global tome
        new_tome = tome + step
        pos = new_tome
        return pos
    return umn

conts = cont(tome)

print(conts(2))
print(conts(5))
print(conts(10))