#include <iostream>
#include <tcb/span.hpp>

int main() {
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    auto s = tcb::span<int>(arr, 10);
}
