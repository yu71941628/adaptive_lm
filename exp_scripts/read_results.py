import json
import re
import sys

def read_state(prefix):
    with open(prefix + '/latest_state.json') as ifp:
        state = json.load(ifp)
    train_ppl = []
    dm_ppl = []
    with open(prefix + '/log.txt') as ifp:
        for line in ifp:
            if "- learning_rate:\t" in line:
                m = re.search(r'(- learning_rate:\t)([^,]*)(\n)',line)
                learning_rate = m.group(2)
            if "Train ppl = " in line:
                m = re.search(r'(Train ppl = )([^,]*)', line)
                if m is not None:
                    train_ppl.append(m.group(2))
                else:
                    train_ppl.append("0.0")
                m = re.search(r'(DM PPL = )([^,]*)', line)
                if m is not None:
                    dm_ppl.append(m.group(2))
                else:
                    dm_ppl.append("0.0")
#    print('{}\t{}\t{}\t \t{} ({})\t{}'.format(
#        dm_ppl[state['best_epoch']], train_ppl[state['best_epoch']], 
#        state['best_val_ppl'], state['best_epoch'] + 1,
#        state['epoch'] + 1, prefix))

#    print "learning_rate= " + str(learning_rate)

    print('{}\t{}'.format(
        learning_rate,state['best_val_ppl']))

    return float(learning_rate), state['best_val_ppl']

if __name__ == "__main__":
        read_state(sys.argv[1])
