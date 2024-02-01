# Binary Search
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1

#     while low <= high:
#         mid = (low + high)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             return mid - 1
#         else:
#             return mid + 2
#     return None

# my_list = [1, 3, 5, 7, 9]
# print(binary_search(my_list, 9))

# Selection Sort
# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr

# print(selectionSort([5, 3, 6, 2, 10]))

# Quick Sort
# def quickSort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quickSort(less) + [pivot] + quickSort(greater)
# print(quickSort([10, 5, 2, 3]))

# Dijkstra Alogirthm
import heapq

# Fungsi untuk menjalankan algoritma Dijkstra
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Graf yang merepresentasikan tawaran
graph = {
    'book': [('poster', 0), ('LP', 5)],
    'poster': [('book', 0), ('LP', 5), ('guitar', 0), ('drum set', 0)],
    'LP': [('book', 5), ('poster', 5), ('guitar', 0), ('drum set', 0), ('piano', 20)],
    'guitar': [('poster', 0), ('piano', 15)],
    'drum set': [('poster', 0), ('piano', 15)],
    'piano': [('LP', 20), ('guitar', 15), ('drum set', 15)]
}

# Menjalankan algoritma Dijkstra dari 'book' (start) ke simpul lainnya
distances = dijkstra(graph, 'book')

# Mencetak jalur terpendek ke 'piano'
print("Jalur terpendek ke piano:")
for node, distance in distances.items():
    if node == 'piano':
        print(f"Total biaya: ${distance}")
