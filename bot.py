import os
import sys
import time
import requests
from colorama import *
from datetime import datetime, timedelta
import json
import brotli
import urllib.parse
import schedule
from threading import Event

init(autoreset=True)

red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the full paths to the files
data_file = os.path.join(script_dir, "data.txt")

# Event for handling graceful shutdown
stop_event = Event()

class W3BFLIX:
    def __init__(self):
        self.line = white + "~" * 50
        self.banner = f"""
        {blue}╔══════════════════════════════════════════════════════════╗
        {blue}║     {white}███████╗██╗     ███████╗██╗  ██╗██╗  ██╗     {blue}║
        {blue}║     {white}██╔════╝██║     ██╔════╝╚██╗██╔╝╚██╗██╔╝     {blue}║
        {blue}║     {white}█████╗  ██║     █████╗   ╚███╔╝  ╚███╔╝      {blue}║
        {blue}║     {white}██╔══╝  ██║     ██╔══╝   ██╔██╗  ██╔██╗      {blue}║
        {blue}║     {white}██║     ███████╗███████╗██╔╝ ██╗██╔╝ ██╗     {blue}║
        {blue}║     {white}╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     {blue}║
        {blue}║        {yellow}██████╗ ██╗ ██████╗██╗  ██╗██╗███████╗   {blue}║
        {blue}║        {yellow}██╔══██╗██║██╔════╝██║  ██║██║██╔════╝   {blue}║
        {blue}║        {yellow}██████╔╝██║██║     ███████║██║█████╗     {blue}║
        {blue}║        {yellow}██╔══██╗██║██║     ██╔══██║██║██╔══╝     {blue}║
        {blue}║        {yellow}██║  ██║██║╚██████╗██║  ██║██║███████╗   {blue}║
        {blue}║        {yellow}╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝   {blue}║
        {blue}╚══════════════════════════════════════════════════════════╝
        {white}                t.me/flexxrichie
        {white}        Running in automated mode - Checking every 12 hours
        {white}                Press Ctrl+C to stop
        """

    def clear_terminal(self):
        # For Windows
        if os.name == "nt":
            _ = os.system("cls")
        # For macOS and Linux
        else:
            _ = os.system("clear")

    def headers(self):
        return {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Origin": "*",
            "Cache-Control": "no-cache",
            "Origin": "https://w3bflix.world",
            "Pragma": "no-cache",
            "Priority": "u=1, i",
            "Referer": "https://w3bflix.world/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "X-Api-Key": "vL7wcDNndYZOA5fLxtab33wUAAill6Kk",
        }

    def lucky_draw(self, tele_id):
        url = f"https://api.w3bflix.world/v1/users/{tele_id}/luckydraw"
        headers = self.headers()
        payload = {"type": "ton"}
        response = requests.post(url, headers=headers, json=payload)
        return response

    def videos(self):
        url = f"https://api.w3bflix.world/v1/videos"
        headers = self.headers()
        response = requests.get(url, headers=headers)
        return response

    def watch(self, tele_id, vid_id):
        url = f"https://api.w3bflix.world/v1/video/{vid_id}/user/{tele_id}/watch"
        headers = self.headers()
        response = requests.post(url, headers=headers)
        return response

    def claim(self, tele_id, vid_id, claim_data, query_id):
        url = f"https://api.w3bflix.world/v1/video/{vid_id}/user/{tele_id}/earn/{claim_data}"
        headers = self.headers()
        payload = {"initDataRaw": f"{query_id}"}
        data = json.dumps(payload)
        headers["Content-Length"] = str(len(data))
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers, data=data)
        return response

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{black}[{now}]{reset} {msg}{reset}")

    def extract_user_info(self, query_string):
        parsed_query = urllib.parse.parse_qs(query_string)
        user_info = parsed_query.get("user", [None])[0]
        if user_info:
            user_data = json.loads(user_info)
            user_id = user_data.get("id")
            first_name = user_data.get("first_name")
            return user_id, first_name
        else:
            return None, None

    def run_scheduled_task(self):
        """Run the main task and schedule the next run"""
        try:
            self.clear_terminal()
            print(self.banner)
            self.log(f"{yellow}Starting scheduled check at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.main()
            next_run = datetime.now() + timedelta(hours=12)
            self.log(f"{yellow}Next run scheduled for: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            self.log(f"{red}Error in scheduled task: {str(e)}")
            
    def main_loop(self):
        """Main loop that runs continuously"""
        self.clear_terminal()
        print(self.banner)
        
        # Schedule the task to run every 12 hours
        schedule.every(12).hours.do(self.run_scheduled_task)
        
        # Run immediately on start
        self.run_scheduled_task()
        
        # Keep running until stop_event is set
        while not stop_event.is_set():
            schedule.run_pending()
            time.sleep(60)  # Check schedule every minute

    def main(self):
        try:
            data = open(data_file, "r").read().splitlines()
            num_acc = len(data)
            self.log(self.line)
            self.log(f"{green}Number of account: {white}{num_acc}")
            
            for no, data in enumerate(data):
                if stop_event.is_set():
                    self.log(f"{yellow}Received stop signal. Completing current account...")
                    break
                    
                self.log(self.line)
                self.log(f"{green}Account number: {white}{no+1}/{num_acc}")
                tele_id, first_name = self.extract_user_info(query_string=data)
                self.log(f"{green}Name: {white}{first_name} - {green}Telegram ID: {white}{tele_id}")

                # Daily Lucky Draw
                self.log(f"{yellow}Trying to claim Daily Lucky Draw...")
                try:
                    draw_response = self.lucky_draw(tele_id=tele_id)
                    draw_data = draw_response.json()
                    
                    if 'data' in draw_data:
                        if 'rewards' in draw_data['data']:
                            rewards = draw_data['data']['rewards']
                            self.log(f"{white}Daily Lucky Draw: {green}Success {rewards} points")
                        elif 'wait' in draw_data['data']:
                            wait_time = draw_data['data']['wait']
                            self.log(f"{white}Daily Lucky Draw: {red}Not time to claim yet (Wait: {wait_time} seconds)")
                        else:
                            self.log(f"{white}Daily Lucky Draw: {red}Unexpected response: {draw_data}")
                    else:
                        self.log(f"{white}Daily Lucky Draw: {red}Invalid response format")
                    
                except Exception as e:
                    self.log(f"{white}Daily Lucky Draw: {red}Error: {str(e)}")

                # Videos
                if not stop_event.is_set():
                    self.log(f"{yellow}Start watching video...")
                    try:
                        videos_response = self.videos()
                        videos_data = videos_response.json()
                        
                        if 'data' not in videos_data:
                            self.log(f"{red}Invalid video response format")
                            continue
                            
                        videos = videos_data["data"]
                        for video in videos:
                            if stop_event.is_set():
                                break
                                
                            vid_title = video["Title"]
                            vid_id = video["Vid"]
                            
                            try:
                                watch = self.watch(tele_id=tele_id, vid_id=vid_id).json()
                                if 'data' not in watch:
                                    self.log(f"{white}{vid_title}: {red}Invalid watch response")
                                    continue
                                    
                                claim_data = watch["data"]["watch"]
                                claim_status = watch["data"]["claimedAt"]
                                self.log(f"{white}{vid_title}: {claim_data}")
                                
                                if claim_status is None:
                                    self.log(f"{yellow}Waiting 30 seconds to simulate video watch...")
                                    for _ in range(30):
                                        if stop_event.is_set():
                                            break
                                        time.sleep(1)
                                    
                                    if not stop_event.is_set():
                                        claim = self.claim(
                                            tele_id=tele_id,
                                            vid_id=vid_id,
                                            claim_data=claim_data,
                                            query_id=data,
                                        )
                                        
                                        if claim.status_code == 200:
                                            claim_response = claim.json()
                                            if 'data' in claim_response and 'claimCode' in claim_response['data']:
                                                claim_code = claim_response["data"]["claimCode"]
                                                self.log(f"{white}{vid_title}: {green}Claim successful")
                                                self.log(f"{white}{vid_title}: {green}/watch {claim_code}:{claim_data}")
                                            else:
                                                self.log(f"{white}{vid_title}: {red}Invalid claim response format")
                                        else:
                                            self.log(f"{white}{vid_title}: {red}Claim failed (Status: {claim.status_code})")
                                else:
                                    self.log(f"{white}{vid_title}: {yellow}Claimed already")
                                    
                            except Exception as e:
                                self.log(f"{red}Error processing video {vid_title}: {str(e)}")
                                continue
                                
                    except Exception as e:
                        self.log(f"{red}Get videos info error: {str(e)}")

            self.log(f"""{yellow}All accounts have been processed. 
            If Auto Claim Bot has not sent message automatically, then you should copy message "/watch ...." and send to W3BFLIX bot manually""")
            
        except Exception as e:
            self.log(f"{red}Main process error: {str(e)}")

if __name__ == "__main__":
    try:
        w3bflix = W3BFLIX()
        w3bflix.main_loop()
    except KeyboardInterrupt:
        print("\nReceived stop signal. Shutting down gracefully...")
        stop_event.set()  # Signal the main loop to stop
        sys.exit(0)