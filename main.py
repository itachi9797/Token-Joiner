import tls_client, colorama, art, json, user_agent, random, threading, time
import os

config = json.load(open('config.json', 'r'))
jas = [ja.strip() for ja in open('preset/ja.txt', 'r').readlines()]

if config['clearConsole'] == True: 
   os.system('cls || clear')

class Faggsh:
      def __init__(self, token: str, proxy: str = None) -> None:
          self.endpoint = 'discord.com/api/v9'
          self.token = token 
          self.proxy = ({
               'http': 'http://%s' % (proxy),
               'https': 'http://%s' % (proxy),
          } if proxy != None else None)
          self.session = tls_client.Session(
               client_identifier = "chrome_108", 
               ja3_string = random.choice(jas), 
               h2_settings = {
                    "HEADER_TABLE_SIZE": 65536,
                    "MAX_CONCURRENT_STREAMS": 1000,
                    "INITIAL_WINDOW_SIZE": 6291456,
                    "MAX_HEADER_LIST_SIZE": 262144
               }, h2_settings_order = ["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],
               supported_signature_algorithms = ["ECDSAWithP256AndSHA256", "PSSWithSHA256", "PKCS1WithSHA256", "ECDSAWithP384AndSHA384", "PSSWithSHA384", "PKCS1WithSHA384", "PSSWithSHA512", "PKCS1WithSHA512",],
               supported_versions = ["GREASE", "1.3", "1.2"],
               key_share_curves = ["GREASE", "X25519"],
               cert_compression_algo = "brotli",
               pseudo_header_order = [":method", ":authority", ":scheme", ":path"],
               connection_flow = 15663105,
               header_order = ["accept", "user-agent", "accept-encoding", "accept-language"]
          )

      def getCookies(self) -> tuple:
          r = self.session.get(f'https://{self.endpoint.split("/")[0]}/login')
          return (
             r.headers['Set-Cookie'][0],
             r.headers['Set-Cookie'][1],
             r.headers['Set-Cookie'][2],
          )
        
      def joinServer(self, invite: str, cookie: tuple):
          return self.session.post(
               f'https://{self.endpoint}/invites/{invite}',
                 headers = {
                         'Accept': '*/*',
                         'Accept-Encoding': 'gzip, deflate, br',
                         'Accept-Language': 'en-US,en;q=0.9',
                         'Authorization': self.token,
                         'Content-Length': 2,
                         'Content-Type': 'application/json',
                         'Origin': f'https://{self.endpoint.split("/")[0]}/',
                         'Referer': f'https://{self.endpoint.split("/")[0]}/invites/{invite}',
                         'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                         'sec-ch-ua-mobile': '?0',
                         'sec-ch-ua-platform': '"Windows"',
                         'sec-fetch-dest': 'empty',
                         'sec-fetch-mode': 'cors',
                         'sec-fetch-site': 'same-origin',
                         'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3MzYyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
                         'User-Agent': user_agent.generate_user_agent(),
                         'Cookie': f'{cookie[0]}; {cookie[1]}; {cookie[2]};'
                 }, json = {}, proxy = self.proxy
          )

def joinServer(token: str, invite: str, proxy: str = None):
    faggsh = Faggsh(token, proxy)
    try:
      request = faggsh.joinServer(invite, faggsh.getCookies())
      print(f'{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}*{colorama.Style.RESET_ALL} {f"{colorama.Style.BRIGHT}{colorama.Fore.LIGHTGREEN_EX}JOINED{colorama.Style.RESET_ALL} | Token: {token[:26]}**" if request.status_code == 200 else f"{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}PAUSE{colorama.Style.RESET_ALL} | Token: {token[:26]}** | Status Code: {request.status_code} | Data: {request.text}"}')
    except Exception as E: 
           pass

print(art.text2art('Token  Joiner'))
invite = input(f'{colorama.Fore.LIGHTGREEN_EX}*{colorama.Fore.RESET} Invite: ')
delay = input(f'{colorama.Fore.LIGHTGREEN_EX}*{colorama.Fore.RESET} Delay: ')

for token in open('tokens.txt', 'r').readlines():
    token = token.strip();
    proxy = None if len(open('proxies.txt', 'r').readlines()) == 0 else random.choice(open('proxies.txt', 'r').readlines()).strip()
    if config['useThreads'] == True:
       threading.Thread(target = joinServer, args = (token, invite, proxy, )).start()
    else:
       joinServer(token, invite, proxy)
    try:
       time.sleep(int(delay))
    except:
        pass
