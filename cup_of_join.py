"#hadasa-web"


def join(*parm, esp="-"):
    try:
        if isinstance(parm[-1], str):
            esp = parm[-1]
            parm = parm[:-1]

        list_of_jpin = []
        for i in parm[:-1]:
            list_of_jpin += i + [esp]
        list_of_jpin += parm[-1]
        return (list_of_jpin)
    except:
        return "error"

print(join())
