import platform
import subprocess


def systemInformation():
    print(f'{"=" * 14} System Informations {"=" * 14}')
    uname = platform.uname()
    print(f'System: {uname.system}')
    print(f'Name: {uname.node}')
    print(f'Release: {uname.release}')
    print(f'Version: {uname.version}')
    print(f'Machine: {uname.machine}')
    print(f'Processor: {uname.processor}')


def activeNetworkDevices():
    def pingIP(address):
        (output, error) = subprocess.Popen((['ping', address, '-n', '1']), stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        if b'bytes=32' in output:
            return "Working"
        elif b'Destination host unreachable.' in output:
            return "No Response"
        elif error:
            return "DNS Error"
        else:
            return "Unknown"

    addr = input("Enter the first 3 sections of IP address: f.e.: XXX.XXX.XXX. :\n")
    try:
        a = int(input("Enter starting number of scan range (1 - 255)\n"))
        b = int(input("Enter ending number of scan range (1 - 255)\n"))
    except ValueError:
        print("Wrong value")
    else:
        for ip in range(a, b + 1):
            ip = str(addr) + str(ip)
            ip = ip.strip("\n")
            response = pingIP(ip)
            print(f'{ip} {response}')


def main():
    # systemInformation()
    activeNetworkDevices()


if __name__ == '__main__':
    main()
