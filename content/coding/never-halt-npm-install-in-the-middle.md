---
title: "Never Halt NPM Install in the middle!"
date: 2024-12-13T08:09:07+00:00
lastmod: 2024-12-13T08:09:07+00:00
---

Typing this up because I would like this to be a reminder to myself that do not press `Ctrl+C` when running `npm install`. I just ran into a very weird issue where few files were missing out of a package but when I tried `npm install` again, NPM just thought that the package has already been installed and didn't check the integrity of the files.

Here is the weird error -

```
PS D:\dev\packages\components> npm run build:css

> @components/components@0.1.0 build:css
> postcss src/stylesSrc/main.css -o src/index.css

node:internal/modules/run_main:129
    triggerUncaughtException(
    ^

Error [ERR_MODULE_NOT_FOUND]: Cannot find module 'D:\dev\node_modules\escalade\sync\index.mjs' imported from D:\dev\node_modules\yargs\lib\platform-shims\esm.mjs
Did you mean to import "escalade/sync/index.js"?
    at finalizeResolution (node:internal/modules/esm/resolve:265:11)
    at moduleResolve (node:internal/modules/esm/resolve:933:10)
    at defaultResolve (node:internal/modules/esm/resolve:1157:11)
    at ModuleLoader.defaultResolve (node:internal/modules/esm/loader:383:12)
    at ModuleLoader.resolve (node:internal/modules/esm/loader:352:25)
    at ModuleLoader.getModuleJob (node:internal/modules/esm/loader:227:38)
    at ModuleWrap. (node:internal/modules/esm/module_job:87:39)
    at link (node:internal/modules/esm/module_job:86:36) {
  code: 'ERR_MODULE_NOT_FOUND',
  url: 'file:///D:/dev/node_modules/escalade/sync/index.mjs'
}

Node.js v20.15.0
npm error Lifecycle script `build:css` failed with error:
npm error Error: command failed
npm error   in workspace: @components/components@0.1.0
npm error   at location: D:\dev\packages\components

```

After checking the folder structure, I could see that the file was indeed missing but when I checked [Escalade's code, the package did have those files](https://github.com/lukeed/escalade/commit/a72e1c3b049f9ce770a3ae07b48f340530950ea3). Silly me!