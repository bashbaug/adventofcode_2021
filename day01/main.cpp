#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char** argv)
{
    std::ifstream is(argv[1]);
    std::string str;
    std::vector<int> values;
    while (std::getline(is, str)) {
        values.push_back(std::stoi(str));
    }

    size_t increases = 0;
    const size_t sz = values.size();
    for (size_t i = 1; i < sz; i++) {
        if (values[i] > values[i-1]) {
            increases++;
        }
    }

    printf("number of increases = %zu\n", increases);
    increases = 0;

    size_t previous = LONG_MAX;
    for (size_t i = 2; i < sz; i++) {
        int sum = values[i] + values[i-1] + values[i-2];
        if (sum > previous) {
            increases++;
        }
        previous = sum;
    }

    printf("number of increases = %zu\n", increases);

    return 0;
}
