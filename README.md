# quantum-random-aes
CNIT 370 project for utilizing quantum randomness in a cipher block chaining implementation of AES

AES Python
1. Command for accepting a message as arg, prints the cipher text (encrypt)🔒
2. Command for accepting ciphertext as arg,  prints message (decrypt)🔑
3. Arbitrary IV input and processing (weird and undocumented for Crypto library)

>https://medium.com/quick-code/aes-implementation-in-python-a82f582f51c2

AWS:
1. Quantum circuit: simulated and non-simulated runs

>https://aws.amazon.com/blogs/quantum-computing/generating-quantum-randomness-with-amazon-braket/
>https://github.com/aws/amazon-braket-examples/blob/main/examples/advanced_circuits_algorithms/Randomness/Randomness_Generation.ipynb

Middleware:
1. AWS CLI called from Python code (configure def account)
2. Invokes circuit (jupyter notebook) via Lambda function
3. Include toggle flag in code, default simulated

>https://medium.com/appsmills/executing-jupyter-notebooks-in-lambda-665b5fac1c42


