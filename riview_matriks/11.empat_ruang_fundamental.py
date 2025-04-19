import sympy as sp 

# inisialisasi agar tampilan output lebih rapi
sp.init_printing()


def fundamental_spaces(matrix):
    """
    fungsi ini menghitung dan menampilkan empat ruang fundamental dari sebuah matriks:
    1. ruang kolom (Column spaces)
    2. Ruang baris (Row spaces)
    3. Nullspace (kernel dari M)
    4. Left Nullspace (kernel dari M^T)
    """
    # menghitung ruang-ruang fundamental menggunakan metode bawaan sympy
    col_space =  matrix.columnspace()
    row_space = matrix.rowspace()
    null_space = matrix.nullspace()
    left_null_space = matrix.T.nullspace()

    # menampilkan matrix input
    print("matrix M : ")
    sp.pretty_print(matrix)

    # menampilkan ruang kolom
    print("Ruang kolom (column space) : ")
    if col_space:
        for vec in col_space:
            sp.pretty_print(vec)
    else:
        print("tidak ada ruang kolom selain nol")

    # menampilkan ruang baris
    print("ruang baris adalah (Row space) :")
    if row_space:
        for vec in row_space:
            sp.pretty_print(vec)
    else:
        print("tidak ada ruang baris selain nol")

    # menampilkan null space
    print("Nullspace (kernel dari M) : ")
    if null_space:
        for vec in null_space:
            sp.pretty_print(vec)
    else:
        print("nullspace hanya memiliki vektor nol")

    # menampilkan  left nullspace
    print("left nullspace (kernel  dari M^T) :")
    if left_null_space:
        for vec in left_null_space:
            sp.pretty_print(vec)
    else:
        print("left nullspace hanya memiliki vektor nol")


# contoh penggunaan
if __name__ == "__main__":
    # contoh matriks
    M = sp.Matrix([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    fundamental_spaces(M)
    