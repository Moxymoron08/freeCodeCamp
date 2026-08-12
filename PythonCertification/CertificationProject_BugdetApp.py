def assemble_val(l,index):
    ret = ''
    for each in l:
        ret += (each[index-1])
    ret += ' '
    return ret

def assemble_key(l):
    ret_list = []
    max = 0
    for each in l:
        if len(each) > max :
            max = len(each)
    for ind,word in enumerate(l):
        if len(word) < max:
            l[ind] += ' '*(max - len(word))
    for i in range(max):
        ret = '     '
        for word in l:
            ret += word[i] + '  '
        ret_list.append(ret)
    return('\n'.join(ret_list))

def centre_print(value):
    num = 30 - len(value)
    tmp = int(num/2)
    return ('*'*tmp + value + '*'*tmp)

def entry_print(value):
    desc = value['description']

    cost = value['amount']
    if isinstance(cost, float):
        cost = str(round(cost,2))
    else:
        cost = str(cost)+".00"

    if len(desc) <= 23:
        return (desc + ' '*(23-len(desc)) + ' '*(7-len(cost)) + cost)
    else:
        return (desc[:23] + ' '*(23-len(desc)) + ' '*(7-len(cost)) + cost)

def clean(ledger):
    ret = 0
    for each in ledger:
        if each['amount'] < 0:
            ret += (-1*each['amount'])
    return ret

#==================================================================================

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': (-1*amount), 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for i in self.ledger :
            balance += i['amount']
        return balance

    def transfer(self,amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {Category.name}')
            Category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self,amount):
        if self.get_balance() >= amount:
            return True
        return False

    def __str__(self):
        print_list = []
        print_list.append(centre_print(self.name))
        for entry in self.ledger:
            print_list.append(entry_print(entry))
        print_list.append(f'Total: {self.get_balance()}')
        
        return ('\n'.join(print_list))

#==================================================================================

def create_spend_chart(categories):
    print_list = []
    print_list.append("Percentage spent by category") 
    output = {}
    cumulative = 0
    for each in categories:
        cumulative += clean(each.ledger)
    for each in categories:
        percent = int(((clean(each.ledger)/cumulative)*10)//1)
        output[each.name] = []
        for i in range(percent):
            output[each.name].append(' o ')
        for i in range(10-percent):
            output[each.name].append('   ')
    print_list.append("100|"+assemble_val(output.values(),10))
    for i in range(9,0,-1):
        print_list.append(" "+str(i*10)+"|"+assemble_val(output.values(),i))
    print_list.append("  0|"+' o '*len(output.values()) + ' ')
    footer = "    " + "-" * ((3 * len(categories)) + 1)
    print_list.append(footer)
    print_list.append(assemble_key(list(output.keys())))

    return '\n'.join(print_list)

#==================================================================================
