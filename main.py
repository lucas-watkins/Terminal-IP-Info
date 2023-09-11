from requests import get
import sys
from rich import print, pretty

#Install rich text
pretty.install()

#print information function
def print_ip_info(ipinfo):
    print('[bold red]===================================================[/bold red]')
    print(f'IP --> [bold red]{ipinfo["ip"]}[/bold red]')
    try:
        print(f'Hostname --> [bold blue]{ipinfo["hostname"]}[/bold blue]')
    except:
        pass
    try:
        print(f'Anycast --> [bold blue]{ipinfo["anycast"]}[/bold blue]')
    except Exception:
        pass
    
    print(f'ISP --> [bold blue]{ipinfo["org"]}[/bold blue]')
    print(f'City --> [bold green]{ipinfo["city"]}[/bold green]')
    print(f'Region --> [bold green]{ipinfo["region"]}[/bold green]')
    print(f'Country --> [bold green]{ipinfo["country"]}[/bold green]\n')
    print(f'Address --> [bold green]{address}[/bold green]\n')
    print(f'Location --> [bold green]{ipinfo["loc"]}[/bold green]')
    print(f'Postal Code --> [bold green]{ipinfo["postal"]}[/bold green]')
    print(f'Timezone --> [bold green]{ipinfo["timezone"]}[/bold green]')
    print('[bold red]===================================================[/bold red]')

#get info from ip
if len(sys.argv) == 1:
    ipinfo = get(f'https://ipinfo.io/json').json()
    # get location from lat and long
    lat = ipinfo['loc'][0:ipinfo['loc'].index(',')]
    long = ipinfo['loc'][ipinfo['loc'].index(',')+1:len(ipinfo['loc'])]
    address = get(f'https://geocode.maps.co/reverse?lat={lat}&lon={long}').json()['display_name']
    print_ip_info(ipinfo)
else:
    for i in range(len(sys.argv)-1):
        ipinfo = get(f'https://ipinfo.io/{sys.argv[i+1]}/json').json()
        try:

            # get location from lat and long
            lat = ipinfo['loc'][0:ipinfo['loc'].index(',')]
            long = ipinfo['loc'][ipinfo['loc'].index(',')+1:len(ipinfo['loc'])]
            address = get(f'https://geocode.maps.co/reverse?lat={lat}&lon={long}').json()['display_name']
            #print info
            print_ip_info(ipinfo)

        except KeyError:
            print('[bold red]===================================================[/bold red]')
            print(f'IP --> [bold red]{sys.argv[i+1]}[/bold red]')
            print(f'[bold red]{sys.argv[i+1]} --> Invalid IP Address[/bold red]')
            print('[bold red]===================================================[/bold red]')

