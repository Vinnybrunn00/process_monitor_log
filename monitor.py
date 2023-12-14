import platform, psutil, time, os, sys
from datetime import datetime

class InfoPlatform:
    def __init__(self) -> None:
        self.__NAME = platform.node() # DESKTOP-6SHBOGJ
        self.__PLATFORM = platform.platform() # Windows-10-10.0.19045-SP0
        self.__VERSION = platform.release() # 10
        self.__ARCHITECTURE = platform.architecture()[0] # 64bit
        self.__MACHINE = platform.machine() # AMD64
        self.__CPU_COUNT = f'{os.cpu_count()} %'
        self.__CPU_FREQ = psutil.cpu_freq()
        self.__APP_USAGE = psutil.process_iter()
        self.__SYSTEM_INIT = psutil.cpu_times()
        self.__TIME_NOW = time.time()
        self.__RAM_TOTAL = psutil.virtual_memory().total
        self.__RAM_PERCENT = f'{psutil.virtual_memory().percent} %'
        self.__RAM_USAGE = psutil.virtual_memory().used
        self.__RAM_fREE = psutil.virtual_memory().free
        self.__IPV4 = psutil.net_if_addrs()['Wi-Fi'][1] if sys.platform != 'linux' else psutil.net_if_addrs()['wlo1'][0]
        self.__USER_INFO = psutil.users()
        self.__DISK_USAGE = psutil.disk_usage('C://') if sys.platform != 'linux' else psutil.disk_usage('/')
        self.__TEMPERATURE_CURRENT = f'{psutil.sensors_temperatures()["acpitz"][0].current} ºC' if sys.platform == 'linux' else ...
        self.__TEMPERATURE_HIGH = f'{psutil.sensors_temperatures()["acpitz"][0].high} ºC' if sys.platform == 'linux' else ...
        self.__TEMPERATURE_CRITICAL = f'{psutil.sensors_temperatures()["acpitz"][0].critical} ºC' if sys.platform == 'linux' else ...
        
        __NET_COUNT = psutil.net_io_counters()
        self.recv = __NET_COUNT.bytes_recv
        self.send = __NET_COUNT.bytes_sent
        
        if sys.platform != 'linux':
            self.__TEMPERATURE_CURRENT = None
            self.__TEMPERATURE_HIGH = None
            self.__TEMPERATURE_CRITICAL = None
    
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
            [!] PC Name: {'':<7}{self.__NAME}
            [!] User Name: {'':<5}{self.__USER_INFO[0].name}
            [!] Platform: {'':<6}{self.__PLATFORM}
            [!] Version: {'':<7}{self.__VERSION}
            [!] Architecture: {'':<2}{self.__ARCHITECTURE}s
            [!] Process: {'':<7}{self.__MACHINE}
            [!] Memory Ram: {'':<4}{round(self.__RAM_TOTAL/(1024.0 **3))} GB
            [!] Memory Percent: {self.__RAM_PERCENT}
            [!] Memory Usage: {'':<2}{round(self.__RAM_USAGE / (1024.0 **3))} GB
            [!] Memory Free: {'':<3}{round(self.__RAM_fREE / (1024.0 **3))} GB
            [!] Active System {'':<2}{datetime.fromtimestamp(self.__TIME_NOW + self.__SYSTEM_INIT.system).strftime("%H:%M:%S")}
            [!] Active User {'':<4}{datetime.fromtimestamp(self.__TIME_NOW + self.__SYSTEM_INIT.user).strftime("%H:%M:%S")}
            {"="*35}
            
            - INFO CPU
            {"="*35}
            [!] Frequece:{'':<5} {round(self.__CPU_FREQ.current)} GHz {round(self.__CPU_FREQ.max)} GHz
            [!] CPU: {'':<10}{f'{self.__CPU_COUNT}'}
            [!] Temperature: {'':<2}{f'{self.__TEMPERATURE_CURRENT}'}
            [!] Temp High: {'':<4}{f'{self.__TEMPERATURE_HIGH}'}
            [!] Temp Critical: {f'{self.__TEMPERATURE_CRITICAL}'}
            {"="*35}
            
            - INFO NETWORK
            {"="*35}
            [!] IP: {'':<8}{self.__IPV4.address}
            [!] Mask_ipv4: {'':<1}{self.__IPV4.netmask}
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