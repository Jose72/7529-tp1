
import sys
from queue import PriorityQueue


def ej2():
    if len(sys.argv) < 3:
        print("Not enough arguments")

    item_num = int(sys.argv[1])
    costs_file = sys.argv[2]

    with open(costs_file, 'r') as fp:
        costs_list = [int(e) for e in fp.readline().strip('\n\t').split(',')]
        if len(costs_list) != item_num:
            print("Mismatch number of items/costs list")
            return

    vault_total_cost_list = PriorityQueue()
    for e in [[costs_list[i], i] for i in range(0, item_num)]:
        vault_total_cost_list.put(e)
    vault_items_list = [[i] for i in range(0, item_num)]

    total_cost = 0
    while vault_total_cost_list.qsize() > 1:
        e1 = vault_total_cost_list.get()
        e2 = vault_total_cost_list.get()

        move_cost = e1[0] + e2[0]

        print(str(e1[1]) + " " + str(vault_items_list[e1[1]]) + " --> " + str(e2[1]) + " " +
              str(vault_items_list[e2[1]]) + ": pago " + str(move_cost) + ", ahora en " + str(e2[1]) + " tengo " +
              str(vault_items_list[e1[1]] + vault_items_list[e2[1]]))

        # Move elements from vault 1 to vault 2
        vault_items_list[e2[1]] += vault_items_list[e1[1]]
        vault_items_list[e1[1]].clear()

        total_cost += move_cost

        # Insert new node
        vault_total_cost_list.put([move_cost, e2[1]])

    print("Costo total = " + str(total_cost))
    return


if __name__ == '__main__':
    ej2()
