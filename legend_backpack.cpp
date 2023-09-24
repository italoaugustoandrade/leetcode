
#include <iostream>
#include <vector>
#include<string>

using namespace std;

// Função para resolver o Problema da Mochila 0/1
int knapsack_01(vector<int>& values, vector<int>& weights, int capacity) {
    int n = values.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int w = 1; w <= capacity; ++w) {
            if (weights[i - 1] <= w) {
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

int main() {
    vector<int> values = {60, 100, 120};
    vector<int> weights = {10, 20, 30};
    int capacity = 50;

    int max_value = knapsack_01(values, weights, capacity);
    cout << "Valor máximo da mochila: " << max_value << endl;

    return 0;
}

/*
0 0              peso 
numero de intens 

*/