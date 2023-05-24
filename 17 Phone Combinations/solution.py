def lettercombinations(digits):
    if digits=="":
        return []
    
    # Create an empty list to store the combinations
    sol=[]
    nokia={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

    # Create a helper function to generate combinations
    def combs(s,nxt):
        if not nxt: #if all the digits are used then append the combination
            sol.append(s)
            return
        # using a for loop call the function for each letter of a given number
        for i in nokia[nxt[0]]:
            combs(s+i,nxt[1:])
    return sol
