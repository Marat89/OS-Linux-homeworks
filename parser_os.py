from subprocess import (run, PIPE)

from collections import Counter
from datetime import datetime


def psaux_run():
    execution_results = run(["ps", "aux"], stdout=PIPE)
    lines = (execution_results.stdout.decode().split("\n"))
    print(len(lines))
    return lines


LINES = psaux_run()
all_proc = len(LINES)
print(all_proc)


def get_user():
    user = []

    for i in range(1, all_proc - 1):
        y = LINES[i].split()

        user.append(y[0])
    uniq_users = list(set(user))
    users_process = Counter(user)
    return [uniq_users, users_process]


def get_process():
    print(len(LINES) - 1)


def get_memory():
    memory = []

    for i in range(1, all_proc - 1):
        y = LINES[i].split()
        memory.append(float(y[3]))

    max_memory = max(memory)
    for i in range(1, all_proc - 1):
        y = LINES[i].split()
        if i == (memory.index(max_memory) + 1):
            max_memory_proc = y[10]
    if len(max_memory_proc) > 20:
        return [max_memory_proc[:20], sum(memory)]
    else:
        return [max_memory_proc[0] * len(max_memory_proc), sum(memory)]


def get_cpu_load():
    proc = []

    for i in range(1, all_proc - 1):
        y = LINES[i].split()
        proc.append(float(y[2]))
    max_load = max(proc)

    for i in range(1, all_proc - 1):
        y = LINES[i].split()
        if i == (proc.index(max_load) + 1):
            max_load_proc = y[10]
            if len(max_load_proc) > 20:
                return [(max_load_proc[:20]), max_load]
            else:
                return [max_load_proc, max_load]


def create_report():
    current_date = datetime.now()
    uniq_users = get_user()
    proc_to_user = get_user()[1]
    memory = get_memory()[1]
    cpu = get_cpu_load()[1]
    max_mem = get_memory()[0]
    max_cpu = get_cpu_load()[0]

    with open(f'{current_date}', 'w') as f:
        f.write(f"Отчёт о состоянии системы:\n"
                f"Пользователи системы:{uniq_users}\n"
                f"Процессов запущено: {all_proc}\n"
                f"Пользовательских процессов: {proc_to_user}\n"
                f"Всего памяти используется: {memory}%\n"
                f"Всего CPU используется: {cpu}%\n"
                f"Больше всего памяти использует: {max_mem}\n"
                f"Больше всего CPU использует: {max_cpu}\n")


if __name__ == '__main__':
    create_report()
