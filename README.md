# ToJyutping

Install:

```sh
$ pip install ToJyutping
```

Usage:

```python
>>> from ToJyutping import ToJyutping
>>> tj = ToJyutping()
>>> tj.run('叙利亚和伊拉克边境重要口岸重新开放')
'叙(zeoi6)利(lei6)亚(aa3)和(wo4)伊(ji1)拉(laai1)克(hak1)边(bin1)境(ging2)重(zung6)要(jiu3)口(hau2)岸(ngon6)重(cung4)新(san1)开(hoi1)放(fong3)'
>>> tj.run('敘利亞和伊拉克邊境重要口岸重新開放')
'敘(zeoi6)利(lei6)亞(aa3)和(wo4)伊(ji1)拉(laai1)克(hak1)邊(bin1)境(ging2)重(zung6)要(jiu3)口(hau2)岸(ngon6)重(cung4)新(san1)開(hoi1)放(fong3)'
```

# License

Source code is distributed under MIT license.

Dictionary data follows the original license.
