# CMake 最低版本号要求
cmake_minimum_required (VERSION 3.22)

# 生成debug or release
set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")

# 项目信息
project (demo6)
set (demo6_VERSION_MAJOR 3)
set (demo6_VERSION_MINOR 8)
set (demo6_VERSION_PATCH 6)

#设置包含当前文件夹属性，方便#include<a.h> 不需要#include<dir/a.h>
set (CMAKE_INCLUDE_CURRENT_DIR ON)

#######################  "${CMAKE_INSTALL_PREFIX}/lib"

set (CMAKE_INSTALL_PREFIX "/opt/${PROJECT_NAME}")
set (path_to_search  "/opt/${PROJECT_NAME}/lib")
#设置 rpath，make install，不过pack还是有问题。
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH ${path_to_search})
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
list(FIND CMAKE_PLATFORM_IMPLICIT_LINK_DIRECTORIES ${path_to_search} isSystemDir)
if("${isSystemDir}" STREQUAL "-1")
    set(CMAKE_INSTALL_RPATH ${path_to_search})
endif("${isSystemDir}" STREQUAL "-1")
#########################

# 检查系统是否支持 pow 函数
include(CheckFunctionExists)
#include (${CMAKE_ROOT}/Modules/CheckFunctionExists.cmake)
check_function_exists(pow HAVE_POW)
message("The value of HAVE_POW is: ${HAVE_POW}")

#use this prefer
#include(CheckSymbolExists)
# Check for macro SEEK_SET
#check_symbol_exists(SEEK_SET "stdio.h" HAVE_SEEK_SET)
#message("The value of HAVE_SEEK_SET is: ${HAVE_SEEK_SET}")

# 加入一个配置头文件，用于处理 CMake 对源码的设置
# 根据config.h.in 输出config.h
configure_file (
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_SOURCE_DIR}/config.h"
    )

# "${PROJECT_BINARY_DIR}/config.h"
# 是否使用自己的 mathkarl 库
# option (USE_MYMATH
#    "Use provided math implementation" ON)

# 是否加入 MathFunctions 库
if  (NOT HAVE_POW)
    include_directories ("${PROJECT_SOURCE_DIR}/math")
    add_subdirectory (math)
    set (EXTRA_LIBS ${EXTRA_LIBS} mathkarl)
endif (NOT HAVE_POW)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 指定生成目标
add_executable(demo ${DIR_SRCS})

# 添加链接库
target_link_libraries (demo  ${EXTRA_LIBS})

# 指定安装路径
install (TARGETS demo DESTINATION bin)
install (FILES "${PROJECT_SOURCE_DIR}/config.h"
    DESTINATION include)

# 启用测试
enable_testing()
# 测试帮助信息是否可以正常提示
add_test (test_usage demo)
set_tests_properties (test_usage
    PROPERTIES PASS_REGULAR_EXPRESSION "Usage: .* base exponent")
# 定义一个宏，用来简化测试工作
macro (do_test arg1 arg2 result)
    add_test (test_${arg1}_${arg2} demo ${arg1} ${arg2})
    set_tests_properties (test_${arg1}_${arg2}
        PROPERTIES PASS_REGULAR_EXPRESSION ${result})
endmacro (do_test)

# 利用 do_test 宏，测试一系列数据
do_test (5 2 "is 25")
do_test (10 5 "is 100000")

# 构建一个 CPack 安装包
include (InstallRequiredSystemLibraries)
set(CPACK_PACKAGE_NAME "${PROJECT_NAME}-installer")
set(CPACK_PACKAGE_VENDOR "karl group")
set(CPACK_PACKAGING_INSTALL_PREFIX "/opt/${PROJECT_NAME}")

set (CPACK_RESOURCE_FILE_LICENSE
    "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set (CPACK_PACKAGE_VERSION_MAJOR "${demo6_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${demo6_VERSION_MINOR}")
set (CPACK_PACKAGE_VERSION_PATCH "${demo6_VERSION_PATCH}")
set(CPACK_SOURCE_IGNORE_FILES "${PROJECT_BINARY_DIR};/.git/;.gitignore")
set(CPACK_SOURCE_GENERATOR "ZIP;TGZ")
set(CPACK_GENERATOR "ZIP;TGZ")
if(UNIX)
    if(CMAKE_SYSTEM_NAME MATCHES Linux)
        list(APPEND CPACK_GENERATOR "DEB")
        set(CPACK_DEBIAN_PACKAGE_MAINTAINER "robertodr")
        set(CPACK_DEBIAN_PACKAGE_SECTION "devel")
        set(CPACK_DEBIAN_PACKAGE_DEPENDS "uuid-dev")
        list(APPEND CPACK_GENERATOR "RPM")
        set(CPACK_RPM_PACKAGE_RELEASE "1")
        set(CPACK_RPM_PACKAGE_LICENSE "MIT")
        set(CPACK_RPM_PACKAGE_REQUIRES "uuid-devel")
    endif()
endif()
message(STATUS "CPack generators: ${CPACK_GENERATOR}")
include (CPack)
