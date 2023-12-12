# Process_monitor_log

This script, written in Python, allows you to extract some useful information from your Windows Operating System.

- The information will be saved in a log file, the file name by default is ```system```, but you can change it in ```info.py``` on line 7 using the parameter ```file_log``` in ```salve_log()``` method.

## example

```python
if __name__ == '__main__':
    info = InfoPlatform()
    info.save_log(file_log='name_file') # file name here
```

## Installing dependencies

```bash
> pip install -r requirements.txt
```

## Run Manually in Terminal

```bash
> python3 info.py
```

## Building executable

```bash
> pyinstaller --onefile --noconsole --icon=assets/img/log.png info.py
```



## Log System Info

|     Status     |           INFO SYSTEM             |
| :-----------:  | :--------------------------------:|
|       ✅       | PC Name                          |
|       ✅       | User Name                        |
|       ✅       | Platform                         |
|       ✅       | Version                          |
|       ✅       | Architecture                     |
|       ✅       | processor                        |
|       ✅       | Memory Ram                       |
|       ✅       | Memory Percent                   |
|       ✅       | Memory Usage                     |
|       ✅       | Memory Free                      |
|       ✅       | Active System                    |
|       ✅       | Active User                      |


|     Status     |           INFO CPU                |
| :-----------: | :--------------------------------: |
|       ✅      |   Frequece                         |
|       ✅      |   Temperature                      |
|       ✅      |   Temperature High                 |          
|       ✅      |   Temperature Critical             |               

|     Status    |           INFO NETWORK             |
| :-----------: | :--------------------------------: |
|       ✅        | IP                              |
|       ✅        | Mask_ipv4                       |
|       ✅        | Send                            |
|       ✅        | Received                        |

|     Status    |           INFO Disk HD/SSD         |
| :-----------: | :--------------------------------: |
|       ✅        | Total                           |
|       ✅        | Used                            |
|       ✅        | Free                            |
|       ✅        | Percent                         |

|     Status     |        INFO Memory Usage          |
| :-----------: | :--------------------------------: |
|       ✅      |   sorted list of processes         |