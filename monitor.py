import platform, psutil, time, os
from datetime import datetime

class InfoPlatform:
    def __init__(self) -> None:
        self.__NAME = platform.node() # DESKTOP-6SHBOGJ
        self.__PLATFORM = platform.platform() # Windows-10-10.0.19045-SP0
        self.__VERSION = platform.release() # 10
        self.__ARCHITECTURE = platform.architecture()[0] # 64bit
        self.__MACHINE = platform.machine() # AMD64
        self.__CPU_COUNT = os.cpu_count()
        self.__CPU_FREQ = psutil.cpu_freq()
        self.__APP_USAGE = psutil.process_iter()
        self.__SYSTEM_INIT = psutil.cpu_times()
        self.__TIME_NOW = time.time()
        self.__RAM = psutil.virtual_memory().total
        self.__IPV4 = psutil.net_if_addrs()['Wi-Fi']
        self.__USER_INFO = psutil.users()
        self.__DISK_USAGE = psutil.disk_usage('C://')
        
        __NET_COUNT = psutil.net_io_counters()
        self.recv = __NET_COUNT.bytes_recv
        self.send = __NET_COUNT.bytes_sent
    
    def _memory_usage(self) -> list:
        '''Sorts in order the 10 processes that consume RAM memory in a list'''
        pr_list = []
        for p in self.__APP_USAGE:
            process = p.as_dict(['name', 'memory_percent'])
            if process['memory_percent'] > 0:
                pr_list.append(process)
        yield sorted(pr_list, key=lambda pr: pr['memory_percent'], reverse=True)[:10]
        
    def get_log(self):
        list_final = []    
        for order in self._memory_usage():
            for order in order:
                ranking = f'''{order['name']} => {order['memory_percent']:.2f}%'''
                list_final.append(ranking)
                 
        message = f'''
            - INFO SYSTEM
            {"="*35}
            [!] PC Name: {'':<6}{self.__NAME}
            [!] User Name: {'':<4}{self.__USER_INFO[0].name}
            [!] Platform: {'':<5}{self.__PLATFORM}
            [!] Version: {'':<6}{self.__VERSION}
            [!] Architecture: {'':<1}{self.__ARCHITECTURE}s 
            [!] Process: {'':<6}{self.__MACHINE}
            [!] Memory Ram: {'':<3}{round(self.__RAM/(1024.0 **3))} GB
            [!] Active System {'':<1}{datetime.fromtimestamp(self.__TIME_NOW + self.__SYSTEM_INIT.system).strftime("%H:%M:%S")}
            [!] Active User {'':<3}{datetime.fromtimestamp(self.__TIME_NOW + self.__SYSTEM_INIT.user).strftime("%H:%M:%S")}
            {"="*35}
            
            - INFO CPU
            {"="*35}
            [!] Frequece: {round(self.__CPU_FREQ.current)} GHz {round(self.__CPU_FREQ.max)} GHz
            [!] CPU: {'':<5}{f'{self.__CPU_COUNT} Core' if not self.__CPU_COUNT == None else None}
            {"="*35}
            
            - INFO NETWORK
            {"="*35}
            [!] IP: {'':<8}{self.__IPV4[1].address}
            [!] Mask_ipv4: {'':<1}{self.__IPV4[0].netmask}
            [!] Mask_ipv6: {'':<1}{self.__IPV4[1].netmask}
            [!] ↑ Send: {'':<4}{self.byteGB(self.send):.2f} GB
            [!] ↓ Received: {self.byteGB(self.recv):.2f} GB
            {"="*35}
            
            - INFO Disk HD/SSD
            {"="*35}
            [!] Total: {'':<2}{self.byteGB(self.__DISK_USAGE.total):.0f} GB
            [!] Used: {'':<3}{self.byteGB(self.__DISK_USAGE.used):.0f} GB
            [!] Free: {'':<3}{self.byteGB(self.__DISK_USAGE.free):.0f} GB
            [!] Percent: {self.__DISK_USAGE.percent} %
            {"="*35}
            
            - INFO Memory Usage
            {"="*35}
            {list_final}
            {"="*35}
            '''
        return message
    
    def byteGB(self, bytes):
        return bytes / (1024 **3)
    
    def save_log(self, file_log='system') -> None:
        get_message = self.get_log()                
        with open(f'{file_log}.log', 'w', encoding='utf-8') as log:
            log.write(get_message)