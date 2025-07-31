import nmap
start = 20
end = 81
target = input("Target IP: ")
scanner = nmap.PortScanner()
for i in range(start, end):
    res = scanner.scan(target,str(i))
    res = res['scan'][target]['tcp'][i]['state']
    print(f"Port {i} is {res}.")