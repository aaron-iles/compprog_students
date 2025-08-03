# Decrypt the Cipher

## Description
Solve the riddle to find the password. Use the MD5 hash of that password to decrypt the given AES-encrypted message. The answer will be a plaintext Christmas message!

This assignment is an exercise in critical thinking, string manipulation, cryptography, and Python coding. Have fun and remember: Google is your friend.

## Instructions

1. Read the riddle carefully and solve it to determine the password.
2. Convert the password to its **MD5 hash** (this will be your decryption key).
3. Use this key to **decrypt the AES cipher** using AES (CBC mode with a static IV of 16 zero bytes).
4. The encrypted message is Base64-encoded. Be sure to decode it before decrypting.
5. The final result should be a human-readable message.
6. Submit your Python script and the decrypted message.

### Riddle

> You were full from second-day turkey,  
> and you had no patience for lines,  
> so when you should have been focused on mission,  
> my Monday was just too divine.  
>   
> Perhaps I'm a punk from the 80s,  
> or later you played in my space,  
> my security is surely your passion,  
> so name me and go crack the case!

### Cipher
```
cgGm2CmmoAlqYYZ4YU5Lod/J36A0/cAROpALdqWcSyIiQM8xm17r6ignhad75rMaXueQnQJqIc9yulhgFAXKdH4hp3Bv6m0eHc22AprW7hg=
```

## Examples & Test Cases

This is an open-ended problem. Your solution will be evaluated based on the correctness of the final decrypted message and your clean implementation.

## Submission Checklist
- [ ] File named `christmas_decrypt.py` created and pushed to your GitHub.
- [ ] Script computes the correct MD5 hash.
- [ ] Script successfully decrypts the AES cipher.
- [ ] Decrypted message is printed and makes sense.
- [ ] Script and message link submitted.

## Grading Criteria

| Criteria                         | Points |
|----------------------------------|--------|
| Correct MD5 implementation       | 5 pts  |
| Correct AES decryption           | 10 pts |
| Code formatting and readability  | 3 pts  |
| Decrypted message is correct     | 7 pts  |

**Total**: 25 points

## Resources
- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
- [Python cryptography package](https://cryptography.io/en/latest/)
