def est_palindrome(liste):
    return liste == liste[::-1]

print(est_palindrome([1, 2, 3, 2, 1]))
print(est_palindrome([1, 2, 3]))