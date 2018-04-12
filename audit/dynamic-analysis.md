# Dynamic Analysis
performed by Blockchain Labs, 12 April, 2018

```
  Contract: Ownable
    √ should have an owner
    √ changes owner after transfer (131ms)
    √ should prevent non-owners from transfering (92ms)
    √ should guard ownership against stuck state (94ms)

  Contract: StandardToken
    total supply
      √ returns the total amount of tokens (47ms)
    balanceOf
      when the requested account has no tokens
        √ returns zero
      when the requested account has some tokens
        √ returns the total amount of tokens (47ms)
    transfer
      when the recipient is not the zero address
        when the sender does not have enough balance
          √ reverts (94ms)
        when the sender has enough balance
          √ transfers the requested amount (190ms)
          √ emits a transfer event (133ms)
      when the recipient is the zero address
        √ reverts (47ms)

  Contract: Mintable
    minting finished
      when the token is not finished
        √ returns false (47ms)
      when the token is finished
        √ returns true
    finish minting
      when the sender is the token owner
        when the token was not finished
          √ finishes token minting (140ms)
          √ emits a mint finished event (112ms)
        when the token was already finished
          √ reverts (38ms)
      when the sender is not the token owner
        when the token was not finished
          √ reverts (52ms)
        when the token was already finished
          √ reverts (59ms)
    mint
      when the sender is the token owner
        when the token was not finished
          √ mints the requested amount (253ms)
          √ emits a mint finished event (131ms)
        when the token minting is finished
          √ reverts (62ms)
      when the sender is not the token owner
        when the token was not finished
          √ reverts (62ms)
        when the token was already finished
          √ reverts (47ms)

  Contract: StandardToken
    total supply
      √ returns the total amount of tokens (47ms)
    balanceOf
      when the requested account has no tokens
        √ returns zero
      when the requested account has some tokens
        √ returns the total amount of tokens (62ms)
    transfer
      when the recipient is not the zero address
        when the sender does not have enough balance
          √ reverts
        when the sender has enough balance
          √ transfers the requested amount (241ms)
          √ emits a transfer event (167ms)
      when the recipient is the zero address
        √ reverts
    approve
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (78ms)
          when there was no approved amount before
            √ approves the requested amount (83ms)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (89ms)
        when the sender does not have enough balance
          √ emits an approval event (81ms)
          when there was no approved amount before
            √ approves the requested amount (141ms)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (109ms)
      when the spender is the zero address
        √ approves the requested amount (65ms)
        √ emits an approval event (78ms)
    transfer from
      when the recipient is not the zero address
        when the spender has enough approved balance
          when the owner has enough balance
            √ transfers the requested amount (228ms)
            √ decreases the spender allowance (160ms)
            √ emits a transfer event (209ms)
          when the owner does not have enough balance
            √ reverts (63ms)
        when the spender does not have enough approved balance
          when the owner has enough balance
            √ reverts (70ms)
          when the owner does not have enough balance
            √ reverts (62ms)
      when the recipient is the zero address
        √ reverts (47ms)
    decrease approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (94ms)
          when there was no approved amount before
            √ keeps the allowance to zero (128ms)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (125ms)
        when the sender does not have enough balance
          √ emits an approval event (64ms)
          when there was no approved amount before
            √ keeps the allowance to zero (140ms)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (148ms)
      when the spender is the zero address
        √ decreases the requested amount (100ms)
        √ emits an approval event (78ms)
    increase approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (99ms)
          when there was no approved amount before
            √ approves the requested amount (112ms)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (117ms)
        when the sender does not have enough balance
          √ emits an approval event (105ms)
          when there was no approved amount before
            √ approves the requested amount (130ms)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (127ms)
      when the spender is the zero address
        √ approves the requested amount (127ms)
        √ emits an approval event (77ms)

  Contract: Bankorus

      √ initial name, symbol, decimals, arrayLimit and allow. test the values of name, symbol, decimals, arrayLimit and allow,  (106ms)
      √ test initial totalSupply and owner balance in the constructor. (54ms)
      transfer
        √ when it is allowed(not paused). (156ms)
        √ when it is not allowed. (287ms)
      transferFrom
        √ when it is allowed (241ms)
        √ when it is not allowed. (640ms)
      setArrayLimit
        √ test new array limit (134ms)
        √ should fail if it is non-owner (62ms)
      transferToAddresses
        √ tranfer two values to two accounts. Should revert if called by non-owner (353ms)
        √ should revert if array lengths are different (63ms)
        √ should revert if array length > arrayLimit (143ms)
      changeAllow
        √ owner change allow (103ms)
        √ should revert if non-owner call this function (49ms)

  74 passing
```
