# Functional tests
Tests are conducted on the Kovan test network. The following contract has been verified on Etherscan.

## [`Bankorus [0x668c04]`](https://kovan.etherscan.io/address/0x668c048a44c5fc90492fdcd142918a425ae060c0#code)

## Accounts

* Owner: [0x80AF605E497a710400d3be60e5C2Bf41594f0422](https://kovan.etherscan.io/address/0x80af605e497a710400d3be60e5c2bf41594f0422)

## Expected behaviour tests

- [x] Cannot transfer ownership of Bankorus contract if called by non-owner. [`0xd82d52`](https://kovan.etherscan.io/tx/0xd82d523d90aefe206f77d7543b189571ed722a99da601b18d927fd25f2dc7a51)
- [x] Owner can successfully transfer ownership of Bankorus. [`0x46b2e3`](https://kovan.etherscan.io/tx/0x46b2e35eb3405238a5c2c46b675c7948a4205721a5a279903fc4943ad266c977)
- [x] Token holders can successfully transfer tokens to specified addresses
[`0xd5ec4b`](https://kovan.etherscan.io/tx/0xd5ec4b751b7a01f6fe320bed2cc265ca234ea1b19e2206fb175a5033d619098e)
- [x] Owner can successfully mint tokens, increasing totalSupply. [`0xf5dc06`](https://kovan.etherscan.io/tx/0xf5dc06ac4e6732a9cd98e12aa5eecdb228412fbf35bf345cfa7517a02177ddc6)
- [x] Non-owner is unable to mint new tokens when calling the mint function. [`0xb7ef30`](https://kovan.etherscan.io/tx/0xb7ef308286ab1ae960d411ed88ee2a897d0be0a809c512b580933d012174ac73)
- [x] Non-owner cannot call finishMinting() without reverting. [`0xa60c5a`](https://kovan.etherscan.io/tx/0xa60c5ad9b80d1689111d37a623689b0c0b296a93723c4856d387bc7746645e28)
- [x] No transfer of tokens takes place when calling transfer from an address without a balance [`0xe49574`](https://kovan.etherscan.io/tx/0xe495748ea610f7a1140fb3c09890f8baf3c52f40c0c1dfa122f8eb34e389322d)
- [x] Non-owner cannot call setArrayLimit without reverting. [`0x01a36d`](https://kovan.etherscan.io/tx/0x01a36d00612ff56988cbf618411488f31a280ff37918ed707b18acf6c2e547bb)
- [x] Owner can successfully setArrayLimit. [`0xdcae69`](https://kovan.etherscan.io/tx/0xdcae697334177d546d097a816400fff2aa5a30b8ad05868c6b9cba8d83afc0a1)
- [x] Successfully approve allowance amount of tokens that can be spent by set spender address. [`0x723d3d`](https://kovan.etherscan.io/tx/0x723d3d306f2fd19318ab4b213f9412a016a4711248a191a3f9a8975f7e7e8001)
- [x] Successfully decrease allowance amount of tokens that can be spent by set spender address. [`0xe5972d`](https://kovan.etherscan.io/tx/0xe5972d68a1c9922c22dc06efcedfa691db8613cb73c03e6f1eb7238d89eaea3b)
- [x] Successfully increase allowance amount of tokens that can be spent by set spender address. [`0x8bc92d`](https://kovan.etherscan.io/tx/0x8bc92d9bd7a3018d87329233b0a6eb5d96b5c4305bb3a402ae981fb781197be5)
- [x] Spender address cannot spend more tokens exceeding the set allowance. [`0x9234d3`](https://kovan.etherscan.io/tx/0x9234d3059ca3e0427b9305de46e6227f646b8585ddbf696cf308118419279c8c)
- [x] Spender address can successfully spend specified allowance amount of tokens. [`0x9c0102`](https://kovan.etherscan.io/tx/0x9c010233003cb9c35e22d45d3321642686c044c3e0998d802f75de3d6b57a776)
- [x] Owner can successfully call transferToAddresses, sending tokens to an amount <= setArrayLimit. [`0x7ca7a2`](https://kovan.etherscan.io/tx/0x7ca7a222809118e113cbddb40bfc0dd9398e021887a64e548231ac069cb5cabb)
- [x] Unable to call transferToAddresses, sending tokens to an amount >= setArrayLimit. [`0xe65fc7`](https://kovan.etherscan.io/tx/0xe65fc7709d4caafd8dec98ac01851ff897b027daa6303f86bf91993fc279e159)
- [x] Owner can successfully call finishMinting() function. [`0x5a6661`](https://kovan.etherscan.io/tx/0x5a6661fd8cb126f5395552e131bd8c2c5e5412fb7daa7854e1e99b9aa1734fd3)
- [x] Owner cannot call finishMinting() function after it has already been called once. [`0x9fea7f`](https://kovan.etherscan.io/tx/0x9fea7ff2deab05d74957e70df762dcc27cfc95ca3177bc3cb7ee6897b2558f14)
- [x] Non-owner cannot pause token transfers by calling changeAllow. [`0x3028c6`](https://kovan.etherscan.io/tx/0x3028c66da86824a41f5859936339a98c83e79c50695f649d85b87556ca2e719b)
- [x] Owner can successfully pause token transfers by calling changeAllow. [`0x1b0fdd`](https://kovan.etherscan.io/tx/0x1b0fdd7558ab656d774067515ed5e8e46eabe86ebdac3608708720d2b0201815)
- [x] Token holders cannot transfer tokens while allow bool is set to False.
[`0x1374c5`](https://kovan.etherscan.io/tx/0x1374c5115546f5550b3bd88fa4a8eb342161d624daad4a178bf51e6bdbc636a2)
- [x] Owner can successfully unpause token transfers by calling changeAllow [`0x87e7b9`](https://kovan.etherscan.io/tx/0x87e7b9adf6452117820b37aaeef284297d01a659c434c81baf1a4e34ecea494a)
- [x] Token holders can successfully transfer tokens while after token transfers have been unpaused.
[`0x32c4b0`](https://kovan.etherscan.io/tx/0x32c4b0b57bb54415d75c8cb9bffacfcc69c70cb8768a62020178415bbd568eb3)
