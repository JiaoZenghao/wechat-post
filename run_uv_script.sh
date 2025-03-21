#!/bin/bash

# Generate timestamp for the output filename
TIMESTAMP=$(date "+%Y%m%d_%H%M%S")
OUTPUT_FILE="output_${TIMESTAMP}.txt"
PROMPT_FILE="prompt_${TIMESTAMP}.txt"

# Run the UV command and redirect output
uv run main.py >"${OUTPUT_FILE}" 2>&1

# Check exit status and handle errors
if [ $? -ne 0 ]; then
  echo "Error: UV command failed. Check ${OUTPUT_FILE} for details."
  exit 1
else
  echo "Success: Output saved to ${OUTPUT_FILE}"

  # Generate the LLM prompt
  cat >"${PROMPT_FILE}" <<EOLPROMPT
你是一位资深的科技类微信公众号写手，擅长将技术内容转化为通俗易懂、吸引人的文章。

下面是一些原始技术内容：

$(cat "${OUTPUT_FILE}")

请你基于以上内容，创作一篇微信公众号文章，要求：
1. 文章标题要吸引人，能够引发读者的好奇心和点击欲望
2. 开头要设置悬念或提出问题，抓住读者的注意力
3. 将技术内容转化为通俗易懂的语言，多使用类比和实际案例
4. 文章结构要清晰，段落之间要有良好的过渡
5. 适当加入互动元素，提高读者的参与度
6. 结尾要有号召性，引导读者关注公众号
7. 考虑SEO优化，使用合适的关键词
8. 配合2-3个与内容相关的图片建议

格式要求：
1. 文章长度3000字左右
2. 分段要清晰，每段不超过300字
3. 可以适当使用表情符号增加活力
4. 适当使用加粗、引用等格式
EOLPROMPT

  echo "Success: LLM prompt generated in ${PROMPT_FILE}"
fi
