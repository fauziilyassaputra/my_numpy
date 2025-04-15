import numpy as np

# matriks simetrik
matriks_simetrk = np.array([[1,2,3],
                            [2,4,5],
                            [3,5,6]])

# matriks simetrik miring
matriks_miring = np.array([[0,-2,-3],
                           [2,0,-4],
                           [3,4,0]])

# matriks hermitian 
matriks_hermitian = np.array([[2+0j, 1-1j],
                             [1+1j, 3+0j]])

# matriks_hermitian miring
matriks_hermitian_miring = np.array([[0+1j,-2+3j],
                                     [2+3j, 0+4j]])


# fungsi check simetrik
def check_symmetry(matrix):
    """memeriksa apakah matriks simetris"""
    return np.array_equal(matrix,matrix.T)

def check_skew_symmetry(matrix):
    """memeriksa apakah matriks simetrik miring"""
    return np.array_equal(matrix.T, -matrix)

def check_hermitian(matrix):
    """memeriksa apakah matriks hermitian"""
    return np.array_equal(matrix,matrix.T.conj())

def check_skew_hermitian(matrix):
    """memeriksa apakah matriks hermitian miring"""
    return np.array_equal(matrix.T.conj(), -matrix)


# mengecek sifat masing-masing matriks
print("apakah simetris ?", check_symmetry(matriks_simetrk))
print("apakah simetris miring ?", check_skew_symmetry(matriks_miring))
print("apakah hermitian ? ", check_hermitian(matriks_hermitian))
print(matriks_hermitian_miring)
print("apakah hermitian miring ? ", check_skew_hermitian(matriks_hermitian_miring))
