def print_dashed():
    print("------------------------------")


def header():
    print("CASH RECEIPT")
    print_dashed()


def body():
    print("Charged to____________________")
    print("Received by___________________")


def footer():
    print_dashed()
    print("© SoftUni")


def cash_receipt():
    header()
    body()
    footer()


cash_receipt()