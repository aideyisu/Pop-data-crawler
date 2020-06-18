import pickle

with open("mapping.db", "rb") as get_myprofile:
    A = pickle.load(get_myprofile)
    print(len(A))
    for i in A:
        print(i)
        print(A[i])
        break
    # print(pickle.load(get_myprofile))
