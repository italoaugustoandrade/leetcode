#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

#define V 4

// Função para calcular o TSP usando recursão e memorização
int tsp(int graph[][V], int s, vector<int>& vertex, vector<vector<int>>& memo) {
    if (vertex.empty()) {
        return graph[s][0];
    }

    int n = vertex.size();
    int min_cost = INT_MAX;

    // Verifique se o resultado já está em cache
    if (memo[s][n] != -1) {
        return memo[s][n];
    }

    for (int i = 0; i < n; i++) {
        int next_city = vertex[i];
        vector<int> new_vertex = vertex;
        new_vertex.erase(new_vertex.begin() + i);
        int cost = graph[s][next_city] + tsp(graph, next_city, new_vertex, memo);
        min_cost = min(min_cost, cost);
    }

    // Armazene o resultado em cache
    memo[s][n] = min_cost;
    return min_cost;
}

int main() {
    int graph[][V] = {{0, 10, 15, 20},
                     {10, 0, 35, 25},
                     {15, 35, 0, 30},
                     {20, 25, 30, 0}};

    int s = 0; // Cidade de partida
    vector<int> vertex;
    for (int i = 0; i < V; i++) {
        if (i != s) {
            vertex.push_back(i);
        }
    }

    vector<vector<int>> memo(V, vector<int>(V, -1)); // Tabela de memorização

    int min_path = tsp(graph, s, vertex, memo);
    cout << "O menor custo de viagem é: " << min_path << endl;

    return 0;
}


// int travllingSalesmanProblem(int graph[][V], int s)
// {
//     vector<int> vertex;
//     for (int i = 0; i < V; i++)
//         if (i != s)
//             vertex.push_back(i);
 
//     int min_path = INT_MAX;
//     do {
//         int current_pathweight = 0;
//         int k = s;
//         for (int i = 0; i < vertex.size(); i++) {
//             current_pathweight += graph[k][vertex[i]];
//             k = vertex[i];
//         }
//         current_pathweight += graph[k][s];
 
//         // update minimum
//         min_path = min(min_path, current_pathweight);
 
//     } while (
//         next_permutation(vertex.begin(), vertex.end()));
 
//     return min_path;
// }


// #define V 4

// int main()
// {
//     int graph[][V] = { { 0, 10, 15, 20 },
//                        { 10, 0, 35, 25 },
//                        { 15, 35, 0, 30 },
//                        { 20, 25, 30, 0 } };
//     int s = 0;
//     cout << solveTSP(graph, s) << endl;
//     return 0;
// } 


// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// const int INF = 1e9;


// // Função para resolver o TSP usando programação dinâmica
// int solveTSP(vector<vector<int>>& distance, int numCities, int startingCity) {
//     // Crie uma tabela de programação dinâmica para armazenar os custos mínimos
//     vector<vector<int>> dp(1 << numCities, vector<int>(numCities, INF));

//     // Inicialize o caso base: quando há apenas uma cidade (a cidade de partida)
//     dp[1 << startingCity][startingCity] = 0;

//     // Percorra todas as máscaras de subconjuntos de cidades
//     for (int mask = 1; mask < (1 << numCities); ++mask) {
//         for (int currentCity = 0; currentCity < numCities; ++currentCity) {
//             if ((mask & (1 << currentCity)) == 0) {
//                 continue;  // Ignore se a cidade atual não estiver na máscara
//             }
//             for (int nextCity = 0; nextCity < numCities; ++nextCity) {
//                 if (currentCity != nextCity && (mask & (1 << nextCity))) {
//                     // Atualize o custo mínimo para chegar à cidade atual
//                     dp[mask][currentCity] = min(dp[mask][currentCity], dp[mask ^ (1 << currentCity)][nextCity] + distance[nextCity][currentCity]);
//                 }
//             }
//         }
//     }

//     // Encontre o menor custo de volta à cidade inicial
//     int finalMask = (1 << numCities) - 1;
//     int minCost = INF;
//     for (int currentCity = 0; currentCity < numCities; ++currentCity) {
//         if (currentCity != startingCity) {
//             // Encontre o custo mínimo para retornar à cidade inicial a partir de cada cidade
//             minCost = min(minCost, dp[finalMask][currentCity] + distance[currentCity][startingCity]);
//         }
//     }

//     return minCost;
// }

// int main() {
//     int n = 4;  // Número de cidades
//     int start = 0;  // Cidade inicial
//     vector<vector<int>> graph = {
//         {0, 29, 20, 21},
//         {29, 0, 15, 12},
//         {20, 15, 0, 10},
//         {21, 12, 10, 0}
//     };

//     int menor_custo = tsp(graph, n, start);
    
//     // Imprima o menor custo do TSP
//     cout << "Menor custo do TSP: " << menor_custo << endl;

//     return 0;
// }