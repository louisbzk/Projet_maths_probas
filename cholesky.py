def cholesky(A):
	l = len(A)
	L = np.zeros((l,l))
	L[0][0] = math.sqrt(A[0][0])
	for j in range(1,l):
		L[j][0] = A[0][j]/L[0][0]

	for i in range(1,l):
		S = 0
		for k in range(0,i):
			S += (L[i][k])**2
		L[i][i] = math.sqrt(A[i][i]-S)
		for j in range(i+1,l):
			T = 0
			for k in range(0,i):
				T += L[i][k]*L[j][k]/L[i][i]
			L[j][i] = (A[i][j]-T)/L[i][i]

	return L
