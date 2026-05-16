---
title: "Weird Error with UV on Windows while doing sync"
date: 2025-12-08T13:58:31+00:00
lastmod: 2025-12-08T13:58:31+00:00
---

Day going normally while working on converting our Python projects to use `uv` (Just awesome!) instead of the usual `pip` and while converting one of the Azure Functions Python project, I encountered the following weird error while running `uv sync` -

```
PS D:\dev\RE> uv sync
  × Failed to build `fusepy==3.0.1`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit code: 101)

      [stderr]
      Unable to create process using '"D:\Python-3.10.15\PCbuild\amd64\python.exe" -c "import sys

      if sys.path[0] == \"\":
          sys.path.pop(0)

      sys.path = [] + sys.path

      from setuptools.build_meta import __legacy__ as backend

      import json

      get_requires_for_build = getattr(backend, \"get_requires_for_build_wheel\", None)
      if get_requires_for_build:
          requires = get_requires_for_build({})
      else:
          requires = []

      with
      open(\"C:\\Users\\PJ\\AppData\\Local\\uv\\cache\\builds-v0\\.tmp0KnOHv\\get_requires_for_build_wheel.txt\",
      \"w\") as fp:
          json.dump(requires, fp)
      "'

      hint: This usually indicates a problem with the package or the build environment.
  help: `fusepy` (v3.0.1) was included because `RE` (v2.2.0) depends on
        `REOE==2.2.0a3` (v2.2.0a3) which depends on `azureml-sdk==1.58.0`        
        (v1.58.0) which depends on `azureml-dataset-runtime[fuse]>=1.58.0, =3.0.1,  python --version
ResourceUnavailable: Program 'python.exe' failed to run: An error occurred trying to start process 'D:\Python-3.10.15\PCbuild\amd64\python.exe' with working directory 'D:\dev\RE'. This program is blocked by group policy. For more information, contact your system administrator.At line:1 char:1
+ python --version
+ ~~~~~~~~~~~~~~~~.

```

Aah! Turns out, our organization recently rolled out policies geared towards security and disabled a lot of the programs. What they have done is that in order to run anything like `python`, I need to escalate myself with Administrator privileges by entering the security details and then also provide justification before I could do anything.

I did the same and then ran `python --version` followed by `uv sync` which worked without any issues. The above issue happened because there were some dependencies which had to be built from source and that required Python to work.