from subprocess import (run, PIPE)

from collections import Counter
from datetime import datetime


def psaux_run():
    execution_results = run(["ps", "aux"], stdout=PIPE)
    lines = (execution_results.stdout.decode().split("\n"))

    return lines


all_proc = len(psaux_run())


def get_user():
    user = []

    for i in range(1, all_proc - 1):
        y = psaux_run()[i].split()

        user.append(y[0])
    uniq_users = list(set(user))
    users_process = Counter(user)
    return [uniq_users, users_process]


def get_process():
    print(len(psaux_run()) - 1)


def get_memory():
    memory = []

    print(all_proc)
    for i in range(1, all_proc - 1):
        y = psaux_run()[i].split()
        memory.append(float(y[3]))

    return sum(memory)


def get_max_memory():
    memory = []

    print(all_proc)
    for i in range(1, all_proc - 1):
        y = psaux_run()[i].split()
        memory.append(float(y[3]))
    max_memory = max(memory)
    for i in range(1, all_proc - 1):
        y = psaux_run()[i].split()
        if i == (memory.index(max_memory) + 1):
            max_memory_proc = y[10]
    if len(max_memory_proc) > 20:
        return max_memory_proc[:20]
    else:
        return max_memory_proc[0] * len(max_memory_proc)


def get_cpu_load():
    proc = []

    print(all_proc)
    for i in range(1, all_proc - 1):
        y = psaux_run()[i].split()
        proc.append(float(y[2]))
    max_load = max(proc)
    return max_load


def get_max_load_proc():
    proc = []
    for i in range(1, all_proc - 1):
        y = psaux_run()[i].split()
        proc.append(float(y[2]))
    max_load = max(proc)
    for i in range(1, all_proc - 1):
        y = psaux_run()[i].split()
        if i == (proc.index(max_load) + 1):
            max_load_proc = y[10]
    if len(max_load_proc) > 20:
        return max_load_proc[:20]
    else:
        return max_load_proc


def create_report():
    current_date = datetime.now()
    uniq_users = get_user()
    proc_to_user = get_user()[1]
    memory = get_memory()
    cpu = get_cpu_load()
    max_mem = get_max_memory()
    max_cpu = get_max_load_proc()

    with open(f'~/Documents/{current_date}', 'w') as f:
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
