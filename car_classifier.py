from sklearn import tree

features = [[300,2],[150,4],[400,2],[180,4],[200,4],
            [115,2],[125,4],[200,4],[180,4],[210,4],
            [102,4],[110,6],[140,4],[182,4],[88,6]
            ]
labels = ["sports car","hatchback","sports car","hatchback","hatchback",
          "sedan","sedan","sedan","sedan","sedan",
          "convertible","wagon","convertible","wagon","convertible"
            ]

clf = tree.DecisionTreeClassifier()

clf.fit(features,labels)

print "-----------------------------------------------"
print "Car Category Classifier"
print "-----------------------------------------------"
x = raw_input("Enter Horsepower of your car : ")
y = raw_input("Enter Number of seats in your car : ")

category = clf.predict([[x,y]])

print category