## Usage of Daisi

It is recommended to use this application on the daisi platform itself using the link https://app.daisi.io/daisies/vijay/LoveMeter/app. However, you can still use your own editor using the below method:

### First, load the Packages:

```
import pydaisi as pyd
lovemeter = pyd.Daisi("vijay/LoveMeter")
```

### Now, connect to Daisi and access the functions using:

```
lovemeter.check(namethis, namethat).value
```
