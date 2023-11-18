import graphviz

g = graphviz.Graph('G', filename='./data/process.gv', engine='sfdp')

sentence = "this is a test sentence\n to see how lines are\n created and handled in the nodes"

g.edge('run' + sentence, 'intr' + sentence)
g.edge('intr' + sentence, 'runbl' + sentence)
g.edge('runbl' + sentence, 'run' + sentence)
g.edge('run' + sentence, 'kernel' + sentence)
g.edge('kernel' + sentence, 'zombie' + sentence)
g.edge('kernel' + sentence, 'sleep' + sentence)
g.edge('kernel' + sentence, 'runmem' + sentence)
g.edge('sleep' + sentence, 'swap' + sentence)
g.edge('swap' + sentence, 'runswap' + sentence)
g.edge('runswap' + sentence, 'new' + sentence)
g.edge('runswap' + sentence, 'runmem' + sentence)
g.edge('new' + sentence, 'runmem' + sentence)
g.edge('sleep' + sentence, 'runmem' + sentence)


if __name__ == '__main__':
    g.view()
