# Functional tests
Tests are conducted on the Kovan test network. The following contract has been verified on Etherscan.

## [`Bankorus [0x60fb84]`](https://kovan.etherscan.io/address/0x60fb8487c3a9b5ef359ce0102432c520c8e2e75d#code)

## Accounts

* Owner: [0x95083ef48d10d778f8bf8aa89f08856bb2ee1c41](https://kovan.etherscan.io/address/0x95083ef48d10d778f8bf8aa89f08856bb2ee1c41)

## Expected behaviour tests

- [x] Cannot transfer ownership of Bankorus contract if called by non-owner. [`0xf074f8`](https://kovan.etherscan.io/tx/0xf074f83112a1b5ed3e3c141228f70d7535891e6ad7cf0cb62b2d5d30c574457e)
- [x] Owner can successfully transfer ownership of Bankorus.
[`0x24a41f`](https://kovan.etherscan.io/tx/0x24a41f72eede3b3e40a0564251249c622aac4380e85f612b95a043461ce716f5)
- [x] Token holders can successfully transfer tokens to specified addresses
[`0x1c6494`](https://kovan.etherscan.io/tx/0x1c6494c03622de635cca9fab58738cd6a16c96ff78f4c82478d7f089be0fbe47)
- [x] No transfer of tokens takes place when calling transfer from an address without a balance [`0xe1fc19`](https://kovan.etherscan.io/tx/0xe1fc196acb96580e01029b0defad308274aa758b26881f162275c2b39bc2728e)
- [x] Non-owner cannot call setArrayLimit without reverting. [`0xe99ed7`](https://kovan.etherscan.io/tx/0xe99ed7a1bafd719506bf7d430279113fd15bb20ef294a8b1749d323da28d6063)
- [x] Owner can successfully setArrayLimit. [`0x2c10b5`](https://kovan.etherscan.io/tx/0x2c10b53e55c68ee061040fb189fb7d1679dff688d9ef02690e7714f868424f36)
- [x] Successfully approve allowance amount of tokens that can be spent by set spender address. [`0xcc21c5`](https://kovan.etherscan.io/tx/0xcc21c5aa1f5dac2a7115133675ebded8352963a0eff86740f198ce25098f972f)
- [x] Successfully decrease allowance amount of tokens that can be spent by set spender address. [`0x54a75f`](https://kovan.etherscan.io/tx/0x54a75f8dbd8f65cbaee9b5601dae37574e1febff7b08769a3378fc94f1ac580f)
- [x] Successfully increase allowance amount of tokens that can be spent by set spender address. [`0x714e66`](https://kovan.etherscan.io/tx/0x714e66a41f839bcda54c0297f0e460319fd5b76e798f982e2bddce1ab895ddfb)
- [x] Spender address cannot spend more tokens exceeding the set allowance. [`0x7fdcdc`](https://kovan.etherscan.io/tx/0x7fdcdc58623d526763bbc704b2c8fc72284186ce7ed13acb2998ab7f19824656)
- [x] Spender address can successfully spend specified allowance amount of tokens. [`0x34ae9e`](https://kovan.etherscan.io/tx/0x34ae9ed774bfb68321441c1518e31fa56837c6883d6b7bd284ad16d4c55bbaf5)
- [x] Owner can successfully call transferToAddresses, sending tokens to an amount <= setArrayLimit. [`0x0d6cd0`](https://kovan.etherscan.io/tx/0x0d6cd034ea99520ab69add0fed65869b266e1f9377eb77be53462c30032e4133)
- [x] Unable to call transferToAddresses, sending tokens to an amount >= setArrayLimit. [`0x4740f2`](https://kovan.etherscan.io/tx/0x4740f2d101a1aafbfd863a69a1d1f7f32e0a6cb8a2e2763ebdbb29ca82479ab3)
