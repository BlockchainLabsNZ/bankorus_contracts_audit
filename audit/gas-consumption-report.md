# Gas consumption report
performed by Blockchain Labs, 12 April, 2018

```
  Contract: Ownable
    √ should have an owner
    √ changes owner after transfer (30240 gas)
    √ should prevent non-owners from transfering (23142 gas)
    √ should guard ownership against stuck state (21906 gas)

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
          √ reverts (23472 gas)
        when the sender has enough balance
          √ transfers the requested amount (36387 gas)
          √ emits a transfer event (36387 gas)
      when the recipient is the zero address
        √ reverts (21871 gas)

  Contract: Mintable
    minting finished
      when the token is not finished
        √ returns false
      when the token is finished
        √ returns true
    finish minting
      when the sender is the token owner
        when the token was not finished
          √ finishes token minting (28314 gas)
          √ emits a mint finished event (28314 gas)
        when the token was already finished
          √ reverts (22141 gas)
      when the sender is not the token owner
        when the token was not finished
          √ reverts (21829 gas)
        when the token was already finished
          √ reverts (21829 gas)
    mint
      when the sender is the token owner
        when the token was not finished
          √ mints the requested amount (67935 gas)
          √ emits a mint finished event (67935 gas)
        when the token minting is finished
          √ reverts (23739 gas)
      when the sender is not the token owner
        when the token was not finished
          √ reverts (23427 gas)
        when the token was already finished
          √ reverts (23427 gas)

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
          √ reverts (23538 gas)
        when the sender has enough balance
          √ transfers the requested amount (36453 gas)
          √ emits a transfer event (36453 gas)
      when the recipient is the zero address
        √ reverts (21937 gas)
    approve
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (45170 gas)
          when there was no approved amount before
            √ approves the requested amount (45170 gas)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (30170 gas)
        when the sender does not have enough balance
          √ emits an approval event (45170 gas)
          when there was no approved amount before
            √ approves the requested amount (45170 gas)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (30170 gas)
      when the spender is the zero address
        √ approves the requested amount (43890 gas)
        √ emits an approval event (43890 gas)
    transfer from
      when the recipient is not the zero address
        when the spender has enough approved balance
          when the owner has enough balance
            √ transfers the requested amount (29458 gas)
            √ decreases the spender allowance (29458 gas)
            √ emits a transfer event (29458 gas)
          when the owner does not have enough balance
            √ reverts (24911 gas)
        when the spender does not have enough approved balance
          when the owner has enough balance
            √ reverts (25322 gas)
          when the owner does not have enough balance
            √ reverts (24911 gas)
      when the recipient is the zero address
        √ reverts (23309 gas)
    decrease approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (31044 gas)
          when there was no approved amount before
            √ keeps the allowance to zero (31044 gas)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (31135 gas)
        when the sender does not have enough balance
          √ emits an approval event (31044 gas)
          when there was no approved amount before
            √ keeps the allowance to zero (31044 gas)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (31135 gas)
      when the spender is the zero address
        √ decreases the requested amount (29764 gas)
        √ emits an approval event (29764 gas)
    increase approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (46174 gas)
          when there was no approved amount before
            √ approves the requested amount (46174 gas)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (31174 gas)
        when the sender does not have enough balance
          √ emits an approval event (46174 gas)
          when there was no approved amount before
            √ approves the requested amount (46174 gas)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (31174 gas)
      when the spender is the zero address
        √ approves the requested amount (44894 gas)
        √ emits an approval event (44894 gas)

  Contract: Bankorus

      √ initial name, symbol, decimals, arrayLimit and allow. test the values of name, symbol, decimals, arrayLimit and allow,
      √ test initial totalSupply and owner balance in the constructor.
      transfer
        √ when it is allowed(not paused). (52335 gas)
        √ when it is not allowed. (90915 gas)
      transferFrom
        √ when it is allowed (90268 gas)
        √ when it is not allowed. (205548 gas)
      setArrayLimit
        √ test new array limit (49602 gas)
        √ should fail if it is non-owner (22294 gas)
      transferToAddresses
        √ tranfer two values to two accounts. Should revert if called by non-owner (110520 gas)
        √ should revert if array lengths are different (26295 gas)
        √ should revert if array length > arrayLimit (54071 gas)
      changeAllow
        √ owner change allow (14022 gas)
        √ should revert if non-owner call this function (21994 gas)


·--------------------------------------------------------------------------|-----------------------------------·
│                                   Gas                                    ·  Block limit: 17592186044415 gas  │
···········································|·······························|····································
│  Methods                                 ·          21 gwei/gas          ·          434.68 usd/eth           │
······················|····················|·········|·········|···········|··················|·················
│  Contract           ·  Method            ·  Min    ·  Max    ·  Avg      ·  # calls         ·  usd (avg)     │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  approve           ·  30170  ·  45598  ·    42327  ·              11  ·          0.39  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  decreaseApproval  ·  29764  ·  31135  ·    30747  ·               8  ·          0.28  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  increaseApproval  ·  31174  ·  46174  ·    42104  ·               8  ·          0.38  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  transfer          ·  21871  ·  52611  ·    34838  ·              12  ·          0.32  │
······················|····················|·········|·········|···········|··················|·················
│  StandardTokenMock  ·  transferFrom      ·  22473  ·  44670  ·    27949  ·              10  ·          0.26  │
······················|····················|·········|·········|···········|··················|·················
│  Deployments                             ·                               ·  % of limit      ·                │
···········································|·········|·········|···········|··················|······· ··········
│  BasicTokenMock                          ·      -  ·      -  ·   374604  ·             0 %  ·          3.42  │
···········································|·········|·········|···········|··················|······· ··········
│  StandardTokenMock                       ·      -  ·      -  ·  1188066  ·             0 %  ·         10.84  │
·------------------------------------------|---------|---------|-----------|------------------|----------------·

  74 passing

```

<br>

## Summary  
Upon finalization of the contracts to be used by Bankorus, the contracts were assessed on the gas usage of each function to ensure there aren't any unforeseen issues with exceeding the block size GasLimit.

<br>
