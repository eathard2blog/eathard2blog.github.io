在c++中：

```c++
#include <iostream>

using namespace std;


int main()
{
  const int i=0;
  int *j = (int*)&i;
  *j=1;
  printf("%d,%d",i,*j);
}
```

```
$g++ -o main *.cpp
$main
0,1
```

在C中：

```c
#include <stdio.h>

int main()
{
  const int i=0;
  int *j = (int*)&i;
  *j=1;
  printf("%d,%d",i,*j);
}
```

```
$gcc -o main *.c
$main
1,1
```

----

**总结**：在C++中const修饰的常量更像是宏定义，可以在编译器的优化阶段被替换。而在c中const常量可以通过指针访问来篡改。

> http://c.biancheng.net/cpp/biancheng/view/3259.html

