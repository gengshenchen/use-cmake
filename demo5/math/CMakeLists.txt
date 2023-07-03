# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
aux_source_directory(. DIR_LIB_SRCS)

# 生成链接库 SHARED or  STATIC
add_library (mathkarl SHARED ${DIR_LIB_SRCS})

# 指定 MathFunctions 库的安装路径
install (TARGETS mathkarl DESTINATION bin)
install (FILES math.h DESTINATION include)
