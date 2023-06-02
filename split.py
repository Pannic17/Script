class person:
    def __init__(self, name):
        self.subtotal = 0
        self.paid = 0
        self.involved = 0
        self.name = name
        self.people = {}
        self.paid_list = {}
        self.involved_list = {}

    def set_people(self, people_list):
        for i in people_list:
            if i != self:
                self.people[i] = 0

    def print(self):
        print("################################")
        print(self.name)
        print("--------------------------------")
        print("* PAID: " + float_to_str(self.paid))
        for i in self.paid_list:
            print("  " + i.name.ljust(20) + ": " + float_to_str(self.paid_list[i]))
        print("--------------------------------")
        print("* SUBS: " + float_to_str(self.involved))
        for i in self.involved_list:
            print("  " + i.name.ljust(20) + ": " + float_to_str(self.involved_list[i]))
        print("--------------------------------")
        print("*TOTAL: " + float_to_str(self.subtotal))
        print("--------------------------------")
        print("<<<收<<<")
        for i in self.people:
            if self.people[i] > 0:
                print(i.name.ljust(18) + " <<< " + float_to_str(self.people[i]))
        print(">>>支>>>")
        for i in self.people:
            if self.people[i] < 0:
                print(i.name.ljust(18) + " >>> " + float_to_str(-self.people[i]))
        print("################################")
        print("\n")


class event:
    def __init__(self, name, paid_person, amount, involved_people):
        self.name = name
        self.involved_people = involved_people
        self.paid_person = paid_person
        self.amount = amount
        self.each = amount / len(involved_people)
        paid_person.paid_list[self] = self.amount

    def pay(self):
        self.paid_person.subtotal -= self.amount
        self.paid_person.paid += self.amount

        for i in self.involved_people:
            i.subtotal += self.each
            i.involved += self.each
            i.involved_list[self] = self.each
            if i != self.paid_person:
                self.paid_person.people[i] += self.each

    def print(self):
        print("################################")
        print(self.name)
        print("付款@" + self.paid_person.name)
        print("--------------------------------")
        print("金额: " + float_to_str(self.amount))
        print("人均: " + float_to_str(self.each))
        print("--------------------------------")
        print("参与人: ", end="")
        for i in self.involved_people:
            print(i.name, end=",")
        print(".")
        print("################################")


def float_to_str(num):
    return format(float(num), '.2f').rjust(8)


if __name__ == '__main__':
    print("分钱计算器")
    people_list = []
    print("Please add people")
    add_person = True
    while add_person:
        print("Enter name to add a person, Press [~] to stop adding person")
        name = input("Name: ")
        if name == "~":
            add_person = False
        else:
            people_list.append(person(name))
    for i in people_list:
        i.set_people(people_list)
    print("People: ", end="")
    for i in people_list:
        print(i.name, end=",")
    print(".")
    print("Now add events")
    event_list = []
    add_event = True
    while add_event:
        print("Enter name to add an event, Press [~] to stop adding event")
        name = input("Name: ")
        if name == "~":
            add_event = False
        else:
            paid_person = input("Paid person: ")
            for i in people_list:
                if i.name == paid_person:
                    paid_person = i
            amount = float(input("Amount: "))
            involved_people_input = input("参与人: ")
            if involved_people_input == "all":
                involved_people = people_list
            else:
                involved_people = involved_people_input.split(",")
                index = 0
                for i in involved_people:
                    for j in people_list:
                        if j.name == i:
                            involved_people[index] = j
                    index += 1
            new_event = event(name, paid_person, amount, involved_people)
            new_event.pay()
            event_list.append(new_event)
    for i in people_list:
        for j in i.people:
            if i.people[j] > j.people[i]:
                i.people[j] -= j.people[i]
                j.people[i] = -i.people[j]
    for i in people_list:
        i.print()
    print("\n\n\n")
    print("Event list")
    for i in event_list:
        i.print()
