# -*- coding: utf-8 -*-

import csv
import copy


def main():
    STATES = [
        'ESTABLISHED',
        'TIME_WAIT',
        'LISTEN',
        'SYN_SENT',
        'SYN_RECV',
        'FIN_WAIT1',
        'FIN_WAIT2',
        'CLOSE_WAIT',
        'CLOSING',
        'LAST_ACK',
        'CLOSED',
    ]
    #書き込み
    with open('output.csv', 'w') as csvfile:
	#STATESをコピーして行く
        fieldnames = copy.copy(STATES)
        fieldnames.insert(0, 'sec')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, 241):
            d = {}
            filename = 'sec{}.log'.format(i)
            with open(filename, 'r') as f:
                lines = f.readlines()
            
            #linesの中にstateがあればlistとして取得し，socketsに入れる
            for state in STATES:
                sockets = list(filter(lambda x: state in x, lines))
                #socketsの長さを
                d[state] = len(sockets)

            d['sec'] = i
            writer.writerow(d)


if __name__ == '__main__':
    main()
