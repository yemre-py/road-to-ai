from linealg import Matrix, Vector

if __name__ == "__main__":
    mat = [
        [2, -1, 3],
        [1, 0, -2],
        [4, 1, 0]
    ]
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    vector = Vector(v1, v2)
    
    vector2 = Vector(v1)
    print(vector2.length())
