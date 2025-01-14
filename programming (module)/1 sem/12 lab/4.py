from scapy.all import ARP, Ether, srp
import ipaddress
def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

ip_range = input("Введите диапазон IP адресов для сканирования (например, 192.168.1.1/24): ")

try:
    ip_network = ipaddress.ip_network(ip_range)
    devices = scan_network(str(ip_network))
    
    print("Список устройств в сети:")
    for device in devices:
        print(f"IP адрес: {device['ip']}, MAC адрес: {device['mac']}")
        
except ValueError:
    print("Некорректный формат IP диапазона")
