# tarsier-input-webapi

webapi input plugin for tarsier.


## install

```bash
pip install tarsier-input-webapi
```

## configuration

```yaml
in:
  type: webapi
  url: https://test.com/api # required
  method: get # default.
  db: test # default
  user: admin # default
  field: "" # optional. witch field you want to check
  basic_auth: # optional.
   user: pass
  params: # get/post/patch/put params
    hoge: hoge
    fuga: fuga
  headers: # default
    content-type: application/json
```

