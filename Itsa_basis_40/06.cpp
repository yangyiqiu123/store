#include <stdio.h>

int main(void)
{
    int g;

    while (scanf("%d", &g) == 1)
    {
        if (g >= 3 && g <= 5)
        {
            printf("Spring\n");
        }
        else if (g >= 6 && g <= 8)
        {
            printf("Summer\n");
        }
        else if (g >= 9 && g <= 11)
        {
            printf("Autumn\n");
        }
        else
        {
            printf("Winter\n");
        }
    }
}