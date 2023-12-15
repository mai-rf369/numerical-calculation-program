# Numerical-Calculation-Program - Tri-Diagonal-Matrix-Algorithm
## Equation


$$
\vec{A} \vec{X} = \vec{B}
$$

$$
\vec{A} =
\begin{pmatrix}
	a_{0, 0}	& a_{0, 1}	& 0		& \cdots	& 0		& 0		& 0		& \cdots	& 0		& 0		& 0		\\
	a_{1, 0}	& a_{1, 1}	& a_{1, 2}	& \cdots	& 0		& 0		& 0		& \cdots	& 0		& 0		& 0		\\
	0		& a_{2, 1}	& a_{2, 2}	& \cdots	& 0		& 0		& 0		& \cdots	& 0		& 0		& 0		\\
	\vdots		& \vdots	& \vdots	& \ddots	& \vdots	& \vdots	& \vdots	& 		& \vdots	& \vdots	& \vdots	\\
	0		& 0		& 0		& \cdots	& a_{i-1, i-1}	& a_{i-1, i}	& 0		& \cdots	& 0		& 0		& 0		\\
	0		& 0		& 0		& \cdots	& a_{i, i-1}	& a_{i, i}	& a_{i, i+1}	& \cdots	& 0		& 0		& 0		\\
	0		& 0		& 0		& \cdots	& 0		& a_{i+1, i}	& a_{i+1, i+1}	& \cdots	& 0		& 0		& 0		\\
	\vdots		& \vdots	& \vdots	& 		& \vdots	& \vdots	& \vdots	& \ddots	& \vdots	& \vdots	& \vdots	\\
	0		& 0		& 0		& \cdots	& 0		& 0		& 0		& \cdots	& a_{N-3, N-3}	& a_{N-3, N-2}	& 0		\\
	0		& 0		& 0		& \cdots	& 0		& 0		& 0		& \cdots	& a_{N-2, N-3}	& a_{N-2, N-2}	& a_{N-2, N-1}	\\
	0		& 0		& 0		& \cdots	& 0		& 0		& 0		& \cdots	& 0		& a_{N-1, N-2}	& a_{N-1, N-1}	\\
\end{pmatrix}
,
\vec{X} =
\begin{pmatrix}
	x_{0}	\\
	x_{1}	\\
	x_{2}	\\
	\vdots	\\
	x_{i-1}	\\
	x_{i}	\\
	x_{i+1}	\\
	\vdots	\\
	x_{N-3}	\\
	x_{N-2}	\\
	x_{N-1}	\\
\end{pmatrix}
,
\vec{B} =
\begin{pmatrix}
	b_{0}	\\
	b_{1}	\\
	b_{2}	\\
	\vdots	\\
	b_{i-1}	\\
	b_{i}	\\
	b_{i+1}	\\
	\vdots	\\
	b_{N-3}	\\
	b_{N-2}	\\
	b_{N-1}	\\
\end{pmatrix}
$$

## Algorithm
### Step 1
$$
\begin{align}
	& \begin{pmatrix}
		a_{0, 0}	& a_{0, 1}	& 0		& \cdots	& 0		& 0		& 0		& \cdots	& 0		& 0		& 0		\\
		a_{1, 0}	& a_{1, 1}	& a_{1, 2}	& \cdots	& 0		& 0		& 0		& \cdots	& 0		& 0		& 0		\\
		0		& a_{2, 1}	& a_{2, 2}	& \cdots	& 0		& 0		& 0		& \cdots	& 0		& 0		& 0		\\
		\vdots		& \vdots	& \vdots	& \ddots	& \vdots	& \vdots	& \vdots	& 		& \vdots	& \vdots	& \vdots	\\
		0		& 0		& 0		& \cdots	& a_{i-1, i-1}	& a_{i-1, i}	& 0		& \cdots	& 0		& 0		& 0		\\
		0		& 0		& 0		& \cdots	& a_{i, i-1}	& a_{i, i}	& a_{i, i+1}	& \cdots	& 0		& 0		& 0		\\
		0		& 0		& 0		& \cdots	& 0		& a_{i+1, i}	& a_{i+1, i+1}	& \cdots	& 0		& 0		& 0		\\
		\vdots		& \vdots	& \vdots	& 		& \vdots	& \vdots	& \vdots	& \ddots	& \vdots	& \vdots	& \vdots	\\
		0		& 0		& 0		& \cdots	& 0		& 0		& 0		& \cdots	& a_{N-3, N-3}	& a_{N-3, N-2}	& 0		\\
		0		& 0		& 0		& \cdots	& 0		& 0		& 0		& \cdots	& a_{N-2, N-3}	& a_{N-2, N-2}	& a_{N-2, N-1}	\\
		0		& 0		& 0		& \cdots	& 0		& 0		& 0		& \cdots	& 0		& a_{N-1, N-2}	& a_{N-1, N-1}	\\
	\end{pmatrix}
	\begin{pmatrix}
		x_{0}	\\
		x_{1}	\\
		x_{2}	\\
		\vdots	\\
		x_{i-1}	\\
		x_{i}	\\
		x_{i+1}	\\
		\vdots	\\
		x_{N-3}	\\
		x_{N-2}	\\
		x_{N-1}	\\
	\end{pmatrix}
	=
	\begin{pmatrix}
		b_{0}	\\
		b_{1}	\\
		b_{2}	\\
		\vdots	\\
		b_{i-1}	\\
		b_{i}	\\
		b_{i+1}	\\
		\vdots	\\
		b_{N-3}	\\
		b_{N-2}	\\
		b_{N-1}	\\
	\end{pmatrix}\\
	\Rightarrow &
	\begin{pmatrix}
		1		& a_{0, 1}^{'}	& 0		& \cdots	& 0		& 0			& 0			& \cdots	& 0		& 0			& 0			\\
		0		& 1		& a_{1, 2}^{'}	& \cdots	& 0		& 0			& 0			& \cdots	& 0		& 0			& 0			\\
		0		& 0		& 1		& \cdots	& 0		& 0			& 0			& \cdots	& 0		& 0			& 0			\\
		\vdots		& \vdots	& \vdots	& \ddots	& \vdots	& \vdots		& \vdots		& 		& \vdots	& \vdots		& \vdots		\\
		0		& 0		& 0		& \cdots	& 1		& a_{i-1, i}^{'}	& 0			& \cdots	& 0		& 0			& 0			\\
		0		& 0		& 0		& \cdots	& 0		& 1			& a_{i, i+1}^{'}	& \cdots	& 0		& 0			& 0			\\
		0		& 0		& 0		& \cdots	& 0		& 0			& 1			& \cdots	& 0		& 0			& 0			\\
		\vdots		& \vdots	& \vdots	& 		& \vdots	& \vdots		& \vdots		& \ddots	& \vdots	& \vdots		& \vdots		\\
		0		& 0		& 0		& \cdots	& 0		& 0			& 0			& \cdots	& 1		& a_{N-3, N-2}^{'}	& 0			\\
		0		& 0		& 0		& \cdots	& 0		& 0			& 0			& \cdots	& 0		& 1			& a_{N-2, N-1}^{'}	\\
		0		& 0		& 0		& \cdots	& 0		& 0			& 0			& \cdots	& 0		& 0			& 1			\\
	\end{pmatrix}
	\begin{pmatrix}
		x_{0}	\\
		x_{1}	\\
		x_{2}	\\
		\vdots	\\
		x_{i-1}	\\
		x_{i}	\\
		x_{i+1}	\\
		\vdots	\\
		x_{N-3}	\\
		x_{N-2}	\\
		x_{N-1}	\\
	\end{pmatrix}
	=
	\begin{pmatrix}
		b_{0}^{'}	\\
		b_{1}^{'}	\\
		b_{2}^{'}	\\
		\vdots		\\
		b_{i-1}^{'}	\\
		b_{i}^{'}	\\
		b_{i+1}^{'}	\\
		\vdots		\\
		b_{N-3}^{'}	\\
		b_{N-2}^{'}	\\
		b_{N-1}^{'}	\\
	\end{pmatrix}\\
\end{align}
$$

#### 1st row
$$
\begin{align}
	& \begin{pmatrix}
		a_{0, 0}	& a_{0, 1}	& \cdots	& 0		\\
		a_{1, 0}	& a_{1, 1}	& \cdots	& 0		\\
		\vdots		& \vdots	& \ddots	& \vdots	\\
		0		& 0		& \cdots	& a_{N-1, N-1}	\\
	\end{pmatrix}
	\begin{pmatrix}
		x_{0}	\\
		x_{1}	\\
		\vdots	\\
		x_{N-1}	\\
	\end{pmatrix}
	=
	\begin{pmatrix}
		b_{0}	\\
		b_{1}	\\
		\vdots	\\
		b_{N-1}	\\
	\end{pmatrix}\\
	\text{Divide the 1st row by } a_{0, 0} \\
	\Leftrightarrow &
	\begin{pmatrix}
		\frac{1}{a_{0, 0}}	& 0		& \cdots	& 0		\\
		0			& 1		& \cdots	& 0		\\
		\vdots			& \vdots	& \ddots	& \vdots	\\
		0			& 0		& \cdots	& 1		\\
	\end{pmatrix}
	\begin{pmatrix}
		a_{0, 0}	& a_{0, 1}	& \cdots	& 0		\\
		a_{1, 0}	& a_{1, 1}	& \cdots	& 0		\\
		\vdots		& \vdots	& \ddots	& \vdots	\\
		0		& 0		& \cdots	& a_{N-1, N-1}	\\
	\end{pmatrix}
	\begin{pmatrix}
		x_{0}	\\
		x_{1}	\\
		\vdots	\\
		x_{N-1}	\\
	\end{pmatrix}
	=
	\begin{pmatrix}
		\frac{1}{a_{0, 0}}	& 0		& \cdots	& 0		\\
		0			& 1		& \cdots	& 0		\\
		\vdots			& \vdots	& \ddots	& \vdots	\\
		0			& 0		& \cdots	& 1		\\
	\end{pmatrix}
	\begin{pmatrix}
		b_{0}	\\
		b_{1}	\\
		\vdots	\\
		b_{N-1}	\\
	\end{pmatrix}\\
	\Leftrightarrow &
	\begin{pmatrix}
		1		& \frac{a_{0, 1}}{a_{0, 0}}	& \cdots	& 0		\\
		a_{1, 0}	& a_{1, 1}			& \cdots	& 0		\\
		\vdots		& \vdots			& \ddots	& \vdots	\\
		0		& 0				& \cdots	& a_{N-1, N-1}	\\
	\end{pmatrix}
	\begin{pmatrix}
		x_{0}	\\
		x_{1}	\\
		\vdots	\\
		x_{N-1}	\\
	\end{pmatrix}
	=
	\begin{pmatrix}
		\frac{b_{0}}{a_{0, 0}}	\\
		b_{1}			\\
		\vdots			\\
		b_{N-1}			\\
	\end{pmatrix}\\
	\Rightarrow &
	\begin{pmatrix}
		1		& a_{0, 1}^{'}	& \cdots	& 0		\\
		a_{1, 0}	& a_{1, 1}	& \cdots	& 0		\\
		\vdots		& \vdots	& \ddots	& \vdots	\\
		0		& 0		& \cdots	& a_{N-1, N-1}	\\
	\end{pmatrix}
	\begin{pmatrix}
		x_{0}	\\
		x_{1}	\\
		\vdots	\\
		x_{N-1}	\\
	\end{pmatrix}
	=
	\begin{pmatrix}
		b_{0}^{'}		\\
		b_{1}			\\
		\vdots			\\
		b_{N-1}			\\
	\end{pmatrix}\\
\end{align}
$$

$$
\left\lbrace
\begin{array}{ccc}
	a_{0, 0}^{'}	&=& 1				\\
	a_{0, 1}^{'}	&=& \frac{a_{0, 1}}{a_{0, 0}}	\\
	b_{0}^{'}	&=& \frac{b_{0}}{a_{0, 0}}	\\
\end{array}
\right.
$$

#### i-1th row
$$
\begin{align}
	& \begin{pmatrix}
		1	& \cdots	& 0		& 0			& 0		& \cdots	& 0		\\
		\vdots	& \ddots	& \vdots	& \vdots		& \vdots	& 		& \vdots	\\
		0	& \cdots	& 1		& a_{i-1, i}^{'}	& 0		& \cdots	& 0		\\
		0	& \cdots	& a_{i, i-1}	& a_{i, i}		& a_{i, i+1}	& \cdots	& 0		\\
		0	& \cdots	& 0		& a_{i+1, i}		& a_{i+1, i+1}	& \cdots	& 0		\\
		\vdots	& 		& \vdots	& \vdots		& \vdots	& \ddots	& \vdots	\\
		0	& \cdots	& 0		& 0			& 0		& \cdots	& a_{N-1, N-1}	\\
	\end{pmatrix}
	\begin{pmatrix}
		x_{0}	\\
		x_{1}	\\
		\vdots	\\
		x_{N-1}	\\
	\end{pmatrix}
	=
	\begin{pmatrix}
		b_{0}^{'}	\\
		\vdots		\\
		b_{i-1}^{'}	\\
		b_{i}		\\
		b_{i+1}		\\
		\vdots		\\
		b_{N-1}		\\
	\end{pmatrix}\\
\end{align}
$$


#### N-1th row



### Step 2



## Execution
```
> python ./program.py
Tri-Diagonal Matrix Algorithm
A X = B

file name (A) = A.csv
file name (B) = B.csv

Input:
A:
   1.00000    2.00000    0.00000    0.00000
   3.00000    2.00000    4.00000    0.00000
   0.00000    6.00000    3.00000    6.00000
   0.00000    0.00000    9.00000    4.00000
B:
   1.00000
   2.00000
   3.00000
   4.00000

Output:
A:
   1.00000    2.00000    0.00000    0.00000
   0.00000    1.00000   -1.00000    0.00000
   0.00000    0.00000    1.00000    0.66667
   0.00000    0.00000    0.00000    1.00000
B:
   1.00000
   0.25000
   0.16667
  -1.25000
X:
  -1.50000
   1.25000
   1.00000
  -1.25000
```
