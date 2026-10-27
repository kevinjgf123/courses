#!/bin/bash
NODE="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/node.exe"
CLI="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/lib/node_modules/@tencent/slidep/dist/index.js"
for f in slides/*.slide; do
  R=$("$NODE" "$CLI" lint TA业务架构咨询方法论.pptx --dsl-file "$f" 2>&1 | tail -1)
  OK=$(echo "$R" | grep -o '"ok":true' | head -1)
  if [ -z "$OK" ]; then
    echo "FAIL $f"
    echo "$R" | head -c 700
    echo
  else
    echo "ok   $f"
  fi
done
