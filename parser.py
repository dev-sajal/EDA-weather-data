import re
import os

if not os.path.exists('unit.xml'):
    try:
        raise SystemExit
    except SystemExit:
        print(0)
else:
    with open('unit.xml') as fp:
        line = fp.read()

    pattern = re.compile(r'errors="(.+?)".+failures="(.+?)".+tests="(.+?)"')

    m = pattern.search(line)

    if m:
        errors_count = m.group(1)
        errors_count = int(errors_count)

        failure_count = m.group(2)
        failure_count = int(failure_count)

        tests_count = m.group(3)
        tests_count = int(tests_count)


    pass_count = tests_count - (errors_count + failure_count)
    pass_percent = int(round((pass_count/tests_count)*100,0))
    print(pass_percent)