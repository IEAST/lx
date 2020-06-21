#include <stdio.h>

int tag;
//判断行列
int IsNot(int i, int j, int (*Q)[4])
{
    int s, t;
    //判断行
    for (s = i, t = 0; t < 4; t++)
    {
        if (Q[s][t] != 0 && t != j)
        {
            return 0;
        }
    }
    //判断列
    for (s = 0, t = j; s < 4; s++)
    {
        if (Q[s][t] != 0 && s != i)
        {
            return 0;
        }
    }
    // 判断左上
    for (s = i - 1, t = j - 1; s >= 0 && t >= 0; s--, t--) //因为s和t会同时进行变化,不会出现一个变一个不变的情况,故这样写
    {
        if (Q[s][t] == 1)
        {
            return 0;
        }
    }
    // 判断左下
    for (s = i - 1, t = j + 1; s >= 0 && t < 4; s--, t++) //因为s和t会同时进行变化,不会出现一个变一个不变的情况,故这样写
    {
        if (Q[s][t] == 1)
        {
            return 0;
        }
    }
    // 判断右上
    for (s = i + 1, t = j - 1; s < 4 && t >= 0; s++, t--) //因为s和t会同时进行变化,不会出现一个变一个不变的情况,故这样写
    {
        if (Q[s][t] == 1)
        {
            return 0;
        }
    }
    // 判断右下
    for (s = i + 1, t = j + 1; s < 4 && t < 4; s++, t++) //因为s和t会同时进行变化,不会出现一个变一个不变的情况,故这样写
    {
        if (Q[s][t] == 1)
        {
            return 0;
        }
    }

    return 1;
}

//Queen方法
void Queen(int i, int (*Q)[4])
{
    int j, k;
    if (i == 4)
    {
        for (k = 0; k < 4; k++)
        {
            for (j = 0; j < 4; j++)
            {
                printf("%d", Q[k][j]);
            }
            printf("\n");
        }
        printf("\n");
        tag++;
        return;
    }

    for (j = 0; j < 4; j++)
    {
        if (IsNot(i, j, Q))
        {
            Q[i][j] = 1;
            Queen(i + 1, Q);
            Q[i][j] = 0;
        }
    }
}

void main()
{
    int Q[4][4];
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            Q[i][j] = 0;
        }
    }

    Queen(0, Q);
}
