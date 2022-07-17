from subprocess import run, PIPE
from collections import Counter
import json
import argparse

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('indir', type=str, help='Path to Access.log')

parser.add_argument("-l", "--locate", default="file")
args = parser.parse_args()



def log_list_in_dir():
    search_result = run(f'ls {args.indir} | grep "\.log" ', shell=True,
                        stdout=PIPE)
    list_log_files = search_result.stdout.decode().split("\n")
    print(type(list_log_files))
    return list_log_files


def rewrite_files():
    list = log_list_in_dir()
    for i in range (len(list) - 1):
        with open(f'{args.indir}/{list[i]}', "r") as file:
            data = file.read().split("\n")
        with open("result.txt", "a") as f:
            f.write(data)



if args.locate == "file":
    FILE = args.indir
elif args.locate == "dir":
    FILE = log_list_in_dir()

def list_request():
    with open(f'{args.indir}', "r") as f:
        File = f.read()

        list = File.split("\n")
        return list


LIST = list_request()


def get_ip():
    ip = []
    for i in range(len(LIST) - 1):
        y = LIST[i].split()

        ip.append(y[0])
    counter = Counter(ip).most_common(3)
    return counter


def lengthy_request():
    lengthy_request = []
    for i in range(len(LIST) - 1):
        y = LIST[i].split()

        lengthy_request.append(y[-1])

    list_request = list(enumerate(lengthy_request, 0))

    sort_list = sorted(list_request, key=lambda value: value[1])
    top_one = sort_list[-1]

    top_two = sort_list[-2]

    top_three = sort_list[-3]

    return [LIST[top_one[0]], LIST[top_two[0]], LIST[top_three[0]]]


def search_get():
    search_result = run(f'grep GET {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def serch_post():
    search_result = run(f'grep POST {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def serch_delete():
    search_result = run(f'grep DELETE {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def serch_put():
    search_result = run(f'grep PUT {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def serch_head():
    search_result = run(f'grep HEAD {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def serch_connect():
    search_result = run(f'grep CONNECT {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def serch_options():
    search_result = run(f'grep OPTIONS {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def serch_trace():
    search_result = run(f'grep TRACE {FILE}', shell=True,
                        stdout=PIPE)
    return len(search_result.stdout.decode())


def create_json():
    data = {}

    data['amount'] = []
    data['amount'].append({
        'POST': f'{serch_post()}',
        'GET': f'{search_get()}',
        'PUT': f'{serch_put()}',
        'DELETE': f'{serch_delete()}',
        'HEAD': f'{serch_head()}',
        'CONNECT': f'{serch_connect()}',
        'OPTIONS': f'{serch_options()}',
        'TRACE': f'{serch_trace()}'
    })
    data['amount_ip_request'] = []
    data['amount_ip_request'].append({
        'One': f'{get_ip()[0]}',
        'Two': f'{get_ip()[1]}',
        'Three': f'{get_ip()[2]}'
    })
    data['long_ip_request'] = []
    data['long_ip_request'].append({
        'One': f'{lengthy_request()[0]}',
        'Two': f'{lengthy_request()[1]}',
        'Three': f'{lengthy_request()[2]}'
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == '__main__':
    # get_ip()
    # lengthy_request()
    # create_json()
    create_json()
