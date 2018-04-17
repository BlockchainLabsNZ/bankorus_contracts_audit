# Gas consumption report
performed by Blockchain Labs, 18 April, 2018

```

  Contract: Ownable
    √ should have an owner
    √ changes owner after transfer (38073 gas)
    √ should prevent non-owners from transfering (25244 gas)
    √ should guard ownership against stuck state (27134 gas)

  Contract: StandardToken
    total supply
      √ returns the total amount of tokens
    balanceOf
      when the requested account has no tokens
        √ returns zero
      when the requested account has some tokens
        √ returns the total amount of tokens
    transfer
      when the recipient is not the zero address
        when the sender does not have enough balance
          √ reverts (27658 gas)
        when the sender has enough balance
          √ transfers the requested amount (53595 gas)
          √ emits a transfer event (53595 gas)
      when the recipient is the zero address
        √ reverts (23973 gas)

  Contract: StandardToken
    total supply
      √ returns the total amount of tokens
    balanceOf
      when the requested account has no tokens
        √ returns zero
      when the requested account has some tokens
        √ returns the total amount of tokens
    transfer
      when the recipient is not the zero address
        when the sender does not have enough balance
          √ reverts (27724 gas)
        when the sender has enough balance
          √ transfers the requested amount (53661 gas)
          √ emits a transfer event (53661 gas)
      when the recipient is the zero address
        √ reverts (24039 gas)
    approve
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (48832 gas)
          when there was no approved amount before
            √ approves the requested amount (48832 gas)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (33832 gas)
        when the sender does not have enough balance
          √ emits an approval event (48832 gas)
          when there was no approved amount before
            √ approves the requested amount (48832 gas)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (33832 gas)
      when the spender is the zero address
        √ approves the requested amount (47552 gas)
        √ emits an approval event (47552 gas)
    transfer from
      when the recipient is not the zero address
        when the spender has enough approved balance
          when the owner has enough balance
            √ transfers the requested amount (52896 gas)
            √ decreases the spender allowance (52896 gas)
            √ emits a transfer event (52896 gas)
          when the owner does not have enough balance
            √ reverts (29097 gas)
        when the spender does not have enough approved balance
          when the owner has enough balance
            √ reverts (31592 gas)
          when the owner does not have enough balance
            √ reverts (29097 gas)
      when the recipient is the zero address
        √ reverts (25411 gas)
    decrease approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (37334 gas)
          when there was no approved amount before
            √ keeps the allowance to zero (37334 gas)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (41072 gas)
        when the sender does not have enough balance
          √ emits an approval event (37334 gas)
          when there was no approved amount before
            √ keeps the allowance to zero (37334 gas)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (41072 gas)
      when the spender is the zero address
        √ decreases the requested amount (36054 gas)
        √ emits an approval event (36054 gas)
    increase approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (54525 gas)
          when there was no approved amount before
            √ approves the requested amount (54525 gas)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (39525 gas)
        when the sender does not have enough balance
          √ emits an approval event (54525 gas)
          when there was no approved amount before
            √ approves the requested amount (54525 gas)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (39525 gas)
      when the spender is the zero address
        √ approves the requested amount (53245 gas)
        √ emits an approval event (53245 gas)

  Contract: Bankorus

      √ initial name, symbol, decimals and arrayLimit. test the values of name, symbol, decimals, arrayLimit and allow,
      √ test initial totalSupply and owner balance in the constructor.
      setArrayLimit
        √ test new array limit (61401 gas)
        √ should fail if it is non-owner (24286 gas)
      transferToAddresses
        √ tranfer two values to two accounts. Should revert if called by non-owner (161596 gas)
        √ should revert if array lengths are different (31413 gas)
        √ should revert if array length > arrayLimit (67954 gas)

·--------------------------------------------------------------------------|-----------------------------------·
│                                   Gas                                    ·  Block limit: 17592186044415 gas  │
···········································|·······························|····································
│  Methods                                 ·          21 gwei/gas          ·          504.73 usd/eth           │
······················|····················|·········|·········|···········|··················|·················
│  Contract           ·  Method            ·  Min    ·  Max    ·  Avg      ·  # calls         ·  usd (avg)     │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  approve           ·  33832  ·  48832  ·    44762  ·               8  ·          0.47  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  decreaseApproval  ·  36054  ·  41072  ·    37949  ·               8  ·          0.40  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  increaseApproval  ·  39525  ·  54525  ·    50455  ·               8  ·          0.53  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  transfer          ·  23973  ·  53661  ·    39738  ·               8  ·          0.42  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  transferFrom      ·  25411  ·  52896  ·    39126  ·               7  ·          0.41  │
······················|····················|·········|·········|···········|··················|·················
│  Deployments                             ·                               ·  % of limit      ·                │
···········································|·········|·········|···········|··················|·················
│  BasicTokenMock                          ·      -  ·      -  ·  2339324  ·             0 %  ·         24.80  │
···········································|·········|·········|···········|··················|·················
│  StandardTokenMock                       ·      -  ·      -  ·  5846260  ·             0 %  ·         61.97  │
·------------------------------------------|---------|---------|-----------|------------------|----------------·

  56 passing

```

<br>

## Summary  
Upon finalization of the contracts to be used by Bankorus, the contracts were assessed on the gas usage of each function to ensure there aren't any unforeseen issues with exceeding the block size GasLimit.

<br>
