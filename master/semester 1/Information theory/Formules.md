# 1.1 Parts of a communication system
# 1.2 Important achievements of information theory
Self-information of a message $x_i$:
$$S(x_i) = -log(p(x_i))$$
Entropy of a discrete source:
$$H(X) = -\sum_{n=1}^{n} p(x_i)log(p(x_i))$$
Entropy of a continuous source:
$$H(X) = \int_{\infty}^{-\infty} f_X(x) log( f_X(x) )dx$$
Information Rate:
$$R(X) = \sum_{i=1}^{n} f(x_i) S(x_i) = - \sum_{i=1}^{n} f(x_i) log(p(x_i))$$
Mutual Information I:
![[Pasted image 20251230151927.png]]

Conditional Entropy:
$$H(Y | X) = - \sum_{i=1}^{n} \sum_{j=1}^{m} p(x_i, y_j)log(p(y_j|x_i))$$
Channel Capacity:
$$C = sup_X I(X; Y)$$
$$ R \leq C$$
Shannon-Hartley theorem:
Channel capacity for AWGN:
$$C = W log( 1 + SNR )$$
Fundamental source coding theorem:
$$ \exists prefix\ code: \lim_{|block| \rightarrow \infty} : H(X) \leq \langle N\rangle < H(X) + \varepsilon$$
# 2.1 Discrete communication systems
## Introduction and notation

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
# 2.2 Entropy of independent discrete sources
$$log_b (p) = \frac{log_a (p)}{log_a (b)} = \frac{ln (p)}{ln (b)}$$
Entropy:
$$H(X) = \sum_{i=1}^{n} p(x_i) S(x_i) = - \sum_{i=1}^{n} p(x_i) log(p(x_i))$$
$f(x_i)$ average frequency of occurrence of $x_i$ 
Information Rate:
$$R(X) = \sum_{i=1}^{n} f(x_i) S(x_i) = - \sum_{i=1}^{n} f(x_i) log(p(x_i))$$
for symbol $x_i$ with duration $\tau(x_i)$:
$$f(x_i) = \frac{p(x_i)}{\langle \tau \rangle}$$
$$\langle \tau \rangle = \sum_{i=1}^{n} p(x_i) \tau (x_i)$$
Relation entropy and rate:
$$R(X) = - \sum_{i=1}^{n} f(x_i) log(p(x_i)) = - \sum_{i=1}^{n} \frac{p(x_i)}{\langle\tau\rangle} log(p(x_i)) = \frac{1}{\langle\tau\rangle} H(X)$$
Binary encoders:
each symbol $x_i$ translated into a sequence of $N(x_i)$ bits
Often with fixed sampling period $T_s$
$$\tau (x_i) = N(x_i)T_s$$
$$\langle\tau\rangle = \langle N \rangle T_s = \sum_{i=1}^{n} p(x_i)\tau(x_i)$$
$$\langle N \rangle = \sum_{i=1}^{n} p(x_i) N(x_i)$$
$$R(X) = \frac{1}{\langle\tau\rangle} H(X) = \frac{1}{\langle N \rangle T_s} H(X)\ in\ bit/s $$
multiply with sample rate $T_s$
$$R(X) = \frac{1}{\langle N \rangle} H(X)\ in\ bit/symbol$$
## Redundancy of independent discrete sources
Absolute reduncancy:
$$R_X = R_{max}(X) - R(X)$$
Relative redundancy:
$$r_X = 1 - \frac{R(X)}{R_{max}(X)}\ with\ 0 \leq r_X \leq 1$$
Efficiency:
$$e_X = \frac{R(X)}{R_{max}(X)}\ with\ 0 \leq e_X \leq 1$$
# 2.6 Markov Processes
Markov property:
$$P(x_j(k)| x_{i,k-1}(k-1) \cap ... \cap x_{i;1}(1)) = P(x_j(k)| x_{i,k-1}(k-1))$$
Representation from state i to j at instance k
$$P_{ij}(k) = p(x_j(k)|x_i(k-1))$$
