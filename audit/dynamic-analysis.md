[![Build Status](https://travis-ci.com/BlockchainLabsNZ/bankorus_contracts_audit.svg?token=cMsQLiEVxF8MFMMJiS2P&branch=master)](https://travis-ci.com/BlockchainLabsNZ/bankorus_contracts_audit)
# Dynamic Analysis
performed by Blockchain Labs, 18 April, 2018

```
  Contract: Ownable
    √ should have an owner
    √ changes owner after transfer (124ms)
    √ should prevent non-owners from transfering (73ms)
    √ should guard ownership against stuck state (85ms)

  Contract: StandardToken
    total supply
      √ returns the total amount of tokens (62ms)
    balanceOf
      when the requested account has no tokens
        √ returns zero (47ms)
      when the requested account has some tokens
        √ returns the total amount of tokens
    transfer
      when the recipient is not the zero address
        when the sender does not have enough balance
          √ reverts (62ms)
        when the sender has enough balance
          √ transfers the requested amount (220ms)
          √ emits a transfer event (181ms)
      when the recipient is the zero address
        √ reverts (63ms)

  Contract: StandardToken
    total supply
      √ returns the total amount of tokens (46ms)
    balanceOf
      when the requested account has no tokens
        √ returns zero (47ms)
      when the requested account has some tokens
        √ returns the total amount of tokens (46ms)
    transfer
      when the recipient is not the zero address
        when the sender does not have enough balance
          √ reverts (62ms)
        when the sender has enough balance
          √ transfers the requested amount (234ms)
          √ emits a transfer event (125ms)
      when the recipient is the zero address
        √ reverts (63ms)
    approve
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (93ms)
          when there was no approved amount before
            √ approves the requested amount (140ms)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (140ms)
        when the sender does not have enough balance
          √ emits an approval event (70ms)
          when there was no approved amount before
            √ approves the requested amount (125ms)
          when the spender had an approved amount
            √ approves the requested amount and replaces the previous one (132ms)
      when the spender is the zero address
        √ approves the requested amount (125ms)
        √ emits an approval event (78ms)
    transfer from
      when the recipient is not the zero address
        when the spender has enough approved balance
          when the owner has enough balance
            √ transfers the requested amount (237ms)
            √ decreases the spender allowance (187ms)
            √ emits a transfer event (141ms)
          when the owner does not have enough balance
            √ reverts (63ms)
        when the spender does not have enough approved balance
          when the owner has enough balance
            √ reverts (78ms)
          when the owner does not have enough balance
            √ reverts (78ms)
      when the recipient is the zero address
        √ reverts (63ms)
    decrease approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (94ms)
          when there was no approved amount before
            √ keeps the allowance to zero (125ms)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (119ms)
        when the sender does not have enough balance
          √ emits an approval event (94ms)
          when there was no approved amount before
            √ keeps the allowance to zero (126ms)
          when the spender had an approved amount
            √ decreases the spender allowance subtracting the requested amount (125ms)
      when the spender is the zero address
        √ decreases the requested amount (141ms)
        √ emits an approval event (94ms)
    increase approval
      when the spender is not the zero address
        when the sender has enough balance
          √ emits an approval event (173ms)
          when there was no approved amount before
            √ approves the requested amount (157ms)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (156ms)
        when the sender does not have enough balance
          √ emits an approval event (76ms)
          when there was no approved amount before
            √ approves the requested amount (141ms)
          when the spender had an approved amount
            √ increases the spender allowance adding the requested amount (141ms)
      when the spender is the zero address
        √ approves the requested amount (141ms)
        √ emits an approval event (93ms)

  Contract: Bankorus

      √ initial name, symbol, decimals and arrayLimit. test the values of name, symbol, decimals, arrayLimit and allow,  (94ms)
      √ test initial totalSupply and owner balance in the constructor. (62ms)
      setArrayLimit
        √ test new array limit (148ms)
        √ should fail if it is non-owner (78ms)
      transferToAddresses
        √ tranfer two values to two accounts. Should revert if called by non-owner (328ms)
        √ should revert if array lengths are different (78ms)
        √ should revert if array length > arrayLimit (125ms)


  56 passing (20s)
```
