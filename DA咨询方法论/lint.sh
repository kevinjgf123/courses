#!/bin/sh
# 逐页 lint Agent 专册 SlideDSL
NODE="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/node.exe"
CLI="C:/Users/gfjia/.workbuddy/binaries/node/versions/22.22.2-6/lib/node_modules/@tencent/slidep/dist/index.js"
PPTX="DA数据架构咨询方法论.pptx"
ok=0; bad=0
for f in slides/*.slide; do
  out=$("$NODE" "$CLI" lint "$PPTX" --dsl-file "$f" 2>&1)
  if echo "$out" | grep -q "error\|Error\|x Unexpected\|x Missing"; then
    bad=$((bad+1)); echo "FAIL $f"; echo "$out" | head -12
  else
    ok=$((ok+1)); echo "ok   $f"
  fi
done
echo "RESULT ok=$ok bad=$bad"
