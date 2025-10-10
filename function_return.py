def function():
    return (2, 3), (4, 5)

(train_X, train_y), (test_X, test_y) = function()
print((train_X, train_y))
print((test_X, test_y))
print(type((train_X, train_y)))
print(type((test_X, test_y)))