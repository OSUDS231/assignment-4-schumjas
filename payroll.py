import copy

# ── Global variables — do not modify ─────────────────────────────────────────

employee_list = []
employee_set  = set()
employee_records  = {}
employee_benefits = {}

VALID_LEVELS      = {'employee', 'manager', 'executive'}
VALID_DEPARTMENTS = {'engineering', 'marketing', 'hr', 'finance', 'operations'}
VALID_PAY_TYPES   = {'hourly', 'salary'}

BENEFITS = {
    'healthcare': ('Health Insurance',        150.0),
    'childcare':  ('Child Care Support',      100.0),
    'transport':  ('Public Transport Benefit', 50.0),
}

change_log = []

# ── Your implementations go below ────────────────────────────────────────────


# Part 1 — Employee Registration

def add_employee(input_str):
    input_str.split()
    if len(input_str) != 5:
        raise ValueError(f"Expected 5 fields, got {len(input_str)}")
    if input_str[0] in employee_set:
        raise ValueError(f"Name already exists: {input_str[0]}")
    if input_str[1] not in VALID_LEVELS:
        raise ValueError(f"Invalid level: {input_str[1]}")
    if input_str[2] not in VALID_DEPARTMENTS:
        raise ValueError(f"Invalid department: {input_str[2]}")
    if input_str[3] not in VALID_PAY_TYPES:
        raise ValueError(f"Invalid pay type: {input_str[3]}")
    try:
        float(input_str[4])
    except ValueError:
        raise ValueError(f"Invalid pay amount: {input_str[4]}")
    employee_list.append(input_str[0])
    employee_set.add(input_str[0])
    employee_records[input_str[0]] = {'level':input_str[1],
                                      'dept':input_str[2],
                                      'pay_type':input_str[3],
                                      'pay_amount':input_str[4]}
    employee_benefits[input_str[0]] = set()
    return employee_records[input_str[0]]


def run_registration():
    count = 0
    while True:
        infor = input("Enter employee info (or 'quit' to stop): ")
        if infor == 'quit':
            print("Stopped")
            print(f"{count} employee(s) registered")
            break
        else:
            count += 1
            try:
                add_employee(infor)
                print(f"Employee {infor.split()[0]} added successfully.")
            except ValueError as err:
                print(f"Error: {str(err)}. Plese try again.")


# Part 2 — Accessors

def get_employee(name):
    return employee_records[name]


def get_employees_by_department(dept):
    empd = []
    for i in employee_records:
        if i['dept'] == dept:
            empd.append(i)
    return empd


def get_employees_by_level(level):
    emps = []
    for i in employee_records:
        if i['level'] == level:
            emps.append(i)
    return emps


# Part 3 — Benefit Assignment

def assign_benefit(name, benefit_code):
    if name not in employee_records:
        raise KeyError(name)
    if benefit_code not in BENEFITS:
        raise ValueError(f"Invalid benefit code: {benefit_code}")
    employee_benefits[name].add(benefit_code)


# Part 4 — Change Log and Modifiers

def save_to_change_log(name):
    change_log.append(copy.deepcopy(employee_records[name]))


def update_employee_pay(name, new_amount):
    if name not in employee_records:
        raise KeyError(name)
    try:
        float(new_amount)
    except:
        raise ValueError(f"Invalid pay amount: {new_amount}")
    save_to_change_log(name)
    employee_benefits[name]['pay_amount'] = new_amount


def update_employee_level(name, new_level):
    if name not in employee_records:
        raise KeyError(name)
    if new_level not in VALID_LEVELS:
        raise ValueError(f"Invalid level: {new_level}")
    save_to_change_log(name)
    employee_records[name]['level'] = new_level


def remove_employee(name):
    if name not in employee_records:
        raise KeyError(name)
    save_to_change_log(name)
    del(employee_records[name])
    employee_set.remove(name)
    employee_list.remove(name)
    del(employee_benefits[name])


