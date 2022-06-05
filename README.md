We have these hpi 'packages':

- main (+ `core` subpackage)
- overlay1 (with symlink to `main`)
- overlay2 (with symlinks to `main` and `overlay1`)

Then we run `PYTHONPATH=overlay2:overlay1:main python3 -c 'import my.module'`

Expected output: something like this

```
HI FROM core my.core /project/main/my/core.py
HI FROM core my.overlay1.my.main.my.core /project/overlay2/my/overlay1/my/main/my/core.py
HI FROM main my.overlay1.my.main.my.module /project/overlay2/my/overlay1/my/main/my/module.py
HI FROM overlay1 my.overlay1.my.module /project/overlay2/my/overlay1/my/module.py
HI FROM overlay2 my.module /project/overlay2/my/module.py
```

, so it's possible to use both `main` and `overlay1` functions in `overlay2`, this might be useful if we want some complicated merging logic.


Results:

If we use `from .  import core` in `overlay1`, it doesn't work. Presumably because `overlay1` has name `my.overlay1.my` in that context, and there is no `my.overlay1.my.core` package.

If we use `from my import core` in `overlay1`, it works, because the import is absolute and it doesn't matter what name the package itself has.

So the conclusion perhaps is that
- if you have a single overlay, it's fine to use either relative or absolute packages
- with multiple (stacked!) overlays, seems that it's necessary to use absolute imports in all overlays when you import 'upstream' modules (like `my.core`)

also see https://memex.zulipchat.com/#narrow/stream/279601-hpi/topic/relative.20vs.20absolute.20imports for the discussion
