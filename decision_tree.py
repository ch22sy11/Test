from sklearn import tree
X = [[0,0],[1,1]]
Y = [0,1]
clf = tree.DecisionTreeclassifier()
clf = clf.fit(X,Y)