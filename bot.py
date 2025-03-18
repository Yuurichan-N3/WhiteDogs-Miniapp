import requests
import json
import time
from urllib.parse import unquote, parse_qs
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.table import Table
from rich.logging import RichHandler
import logging

# Setup logging dengan Rich
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger("rich")
console = Console()

# Banner
BANNER = """
╔══════════════════════════════════════════════╗
║       🌟 WHITEDOGS BOT - Task Automation     ║
║   Automate your WhiteDogs account tasks!     ║
║  Developed by: https://t.me/sentineldiscus   ║
╚══════════════════════════════════════════════╝
"""

# Konfigurasi endpoint
BASE_URL = "https://server.whitedogs.xyz/api"
COMPLETE_TASK_ENDPOINT = f"{BASE_URL}/tasks/complete"
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
}

# Data task lengkap
TASK_DATA = {
    "tasks": [
        {"task_id": 149, "task_name": "Play Path", "reward": "2500", "task_category": "Partner"},
        {"task_id": 148, "task_name": "Join Planes", "reward": "2500", "task_category": "Partner"},
        {"task_id": 147, "task_name": "Do Brrrrr", "reward": "2500", "task_category": "Partner"},
        {"task_id": 146, "task_name": "Join And Play CrashCoin", "reward": "2500", "task_category": "Partner"},
        {"task_id": 145, "task_name": "Play Happy Village", "reward": "2500", "task_category": "Partner"},
        {"task_id": 144, "task_name": "Play HappyBoxes", "reward": "2500", "task_category": "Partner"},
        {"task_id": 140, "task_name": "React To The Post✨", "reward": "2500", "task_category": "One-Time"},
        {"task_id": 139, "task_name": "Repost And Likes❤️", "reward": "2500", "task_category": "One-Time"},
        {"task_id": 134, "task_name": "Play Bagel", "reward": "2500", "task_category": "Partner"},
        {"task_id": 132, "task_name": "Make An Upvote For Whitedogs on Ton App", "reward": "6000", "task_category": "One-Time"},
        {"task_id": 129, "task_name": "Like & share this post", "reward": "1500", "task_category": "One-Time"},
        {"task_id": 128, "task_name": "Retweet and like this post", "reward": "1500", "task_category": "One-Time"},
        {"task_id": 127, "task_name": "React to this post ✨", "reward": "1500", "task_category": "One-Time"},
        {"task_id": 126, "task_name": "Check Out Whitedogs on Telegram App store", "reward": "5000", "task_category": "One-Time"},
        {"task_id": 125, "task_name": "Join WEBBED Community", "reward": "2500", "task_category": "Partner"},
        {"task_id": 124, "task_name": "Farm Webbed Token", "reward": "2500", "task_category": "Partner"},
        {"task_id": 123, "task_name": "Play Mushroom Warrior", "reward": "2500", "task_category": "Partner"},
        {"task_id": 122, "task_name": "Play Shiba Fishing", "reward": "2500", "task_category": "Partner"},
        {"task_id": 120, "task_name": "Join Happy Farmer Channel", "reward": "2500", "task_category": "Partner"},
        {"task_id": 119, "task_name": "Launch Happy Farmer", "reward": "2500", "task_category": "Partner"},
        {"task_id": 118, "task_name": "Rate WhiteDogs on @appss", "reward": "5000", "task_category": "Partner"},
        {"task_id": 117, "task_name": "Launch Picardia Ecosystem", "reward": "2500", "task_category": "Partner"},
        {"task_id": 116, "task_name": "Play SKILLER", "reward": "2500", "task_category": "Partner"},
        {"task_id": 115, "task_name": "Play Giraffekombat", "reward": "2500", "task_category": "Partner"},
        {"task_id": 113, "task_name": "React To This Post", "reward": "1500", "task_category": "One-Time"},
        {"task_id": 112, "task_name": "Repost & Like This Post", "reward": "1500", "task_category": "One-Time"},
        {"task_id": 111, "task_name": "Like, Comment And Share This Post", "reward": "1500", "task_category": "One-Time"},
        {"task_id": 110, "task_name": "Share & Like This Post", "reward": "1000", "task_category": "One-Time"},
        {"task_id": 109, "task_name": "React To This Post✨", "reward": "1000", "task_category": "One-Time"},
        {"task_id": 108, "task_name": "Valentine Gift 🎁", "reward": "20000", "task_category": "One-Time"},
        {"task_id": 100, "task_name": "Join MemeMarket Channel", "reward": "1000", "task_category": "Partner"},
        {"task_id": 99, "task_name": "Launch MemeMarket App", "reward": "1500", "task_category": "Partner"},
        {"task_id": 92, "task_name": "Join POKE Center channel", "reward": "1000", "task_category": "Partner"},
        {"task_id": 91, "task_name": "Earn USDT on POKE Center", "reward": "1000", "task_category": "Partner"},
        {"task_id": 90, "task_name": "Free Gift", "reward": "5000", "task_category": "One-Time"},
        {"task_id": 87, "task_name": "Play Burn Ghost", "reward": "1000", "task_category": "Partner"},
        {"task_id": 86, "task_name": "Play Biz Tycoon now", "reward": "1000", "task_category": "Partner"},
        {"task_id": 85, "task_name": "Join CAPtcha channel", "reward": "1000", "task_category": "Partner"},
        {"task_id": 84, "task_name": "Join CAPtcha", "reward": "1000", "task_category": "Partner"},
        {"task_id": 72, "task_name": "Comment And Clap", "reward": "1000", "task_category": "One-Time"},
        {"task_id": 71, "task_name": "Follow Us On Medium", "reward": "2000", "task_category": "One-Time"},
        {"task_id": 66, "task_name": "Play Outmine", "reward": "1000", "task_category": "Partner"},
        {"task_id": 63, "task_name": "PLAY AND EARN WITH BOORI", "reward": "1000", "task_category": "Partner"},
        {"task_id": 59, "task_name": "Follow us on Instagram", "reward": "2000", "task_category": "One-Time"},
        {"task_id": 58, "task_name": "Repost (retweet) and like our X post", "reward": "500", "task_category": "One-Time"},
        {"task_id": 48, "task_name": "Play Masterverses", "reward": "1000", "task_category": "Partner"},
        {"task_id": 47, "task_name": "Play ApesOfTon", "reward": "1000", "task_category": "Partner"},
        {"task_id": 45, "task_name": "Play AstroBuster", "reward": "1000", "task_category": "Partner"},
        {"task_id": 44, "task_name": "Play KOLOBOK", "reward": "1000", "task_category": "Partner"},
        {"task_id": 43, "task_name": "Join KOLOBOK Channel", "reward": "1000", "task_category": "Partner"},
        {"task_id": 42, "task_name": "Play Pandatap", "reward": "1000", "task_category": "Partner"},
        {"task_id": 40, "task_name": "Join the Bit Billionaire Anouncement Channel", "reward": "1000", "task_category": "Partner"},
        {"task_id": 39, "task_name": "Play the Bit Billionaire game", "reward": "1000", "task_category": "Partner"},
        {"task_id": 36, "task_name": "Play KANDR", "reward": "1000", "task_category": "Partner"},
        {"task_id": 22, "task_name": "Boost Our Telegram Channel", "reward": "250", "task_category": "Daily"},
        {"task_id": 9, "task_name": "Boost Our Telegram Channel", "reward": "1500", "task_category": "One-Time"},
        {"task_id": 8, "task_name": "Refer 100 Friends", "reward": "30000", "task_category": "One-Time"},
        {"task_id": 7, "task_name": "Refer 50 friends", "reward": "20000", "task_category": "One-Time"},
        {"task_id": 6, "task_name": "Refer 25 Friends", "reward": "12500", "task_category": "One-Time"},
        {"task_id": 5, "task_name": "Refer 10 Friends", "reward": "6000", "task_category": "One-Time"},
        {"task_id": 4, "task_name": "Refer 5 Friends", "reward": "3000", "task_category": "One-Time"},
        {"task_id": 3, "task_name": "Refer 3 Friends", "reward": "1000", "task_category": "One-Time"},
        {"task_id": 2, "task_name": "Follow Us On X", "reward": "2000", "task_category": "One-Time"},
        {"task_id": 1, "task_name": "Join our Telegram channel", "reward": "2000", "task_category": "One-Time"}
    ],
    "lastCompletedTasks": [
        {"task_id": 13, "task_category": "Daily", "completion_date": "2025-03-18T05:40:25.621Z"}
    ]
}

def read_webappdata_from_file(file_path):
    """Membaca dan parse WebAppData dari file data.txt"""
    accounts = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            lines = content.split('\n')
            for line in lines:
                if not line:
                    continue
                decoded_data = unquote(line)
                parsed_data = parse_qs(decoded_data)
                if "user" in parsed_data:
                    user_json = parsed_data["user"][0]
                    user_data = json.loads(user_json)
                    telegram_id = str(user_data.get("id"))
                    if telegram_id:
                        accounts.append({"telegram_id": telegram_id})
        return accounts
    except Exception as e:
        logger.error(f"Error membaca file: {str(e)}")
        return []

def filter_uncompleted_tasks(tasks, completed_tasks):
    """Filter task yang belum selesai"""
    completed_ids = {task["task_id"] for task in completed_tasks}
    return [task for task in tasks if task["task_id"] not in completed_ids]

def complete_task(telegram_id, task):
    """Mengirim request untuk complete task"""
    payload = {
        "taskId": task["task_id"],
        "telegram_id": telegram_id,
        "reward": task["reward"],
        "task_category": task["task_category"]
    }
    
    try:
        response = requests.put(COMPLETE_TASK_ENDPOINT, headers=HEADERS, json=payload)
        task_id = task["task_id"]
        
        if response.status_code == 200:
            logger.info(f"[SUCCESS] Task {task_id} - {task['task_name']} completed")
            return True
        elif response.status_code == 409:
            logger.warning(f"[SKIP] Task {task_id} - {task['task_name']} already completed")
            return False
        elif response.status_code == 401:
            logger.error(f"[UNAUTHORIZED] Task {task_id} - {task['task_name']} - Status: 401, auth mungkin diperlukan")
            return False
        else:
            logger.error(f"[FAILED] Task {task_id} - {task['task_name']} - Status: {response.status_code}")
            logger.error(f"Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"[ERROR] Request failed for task {task_id}: {str(e)}")
        return False

def process_account(account):
    """Proses task untuk satu akun"""
    telegram_id = account["telegram_id"]
    logger.info(f"Memproses telegram_id: {telegram_id}")
    
    tasks_to_complete = filter_uncompleted_tasks(TASK_DATA["tasks"], TASK_DATA["lastCompletedTasks"])
    tasks_completed = 0
    for task in tasks_to_complete:
        if complete_task(telegram_id, task):
            tasks_completed += 1
        time.sleep(2)
    
    return {"telegram_id": telegram_id, "tasks_completed": tasks_completed}

def display_results(results):
    """Tampilkan hasil dalam tabel"""
    table = Table(title="Hasil Proses Akun")
    table.add_column("Telegram ID", style="cyan")
    table.add_column("Tasks Completed", style="green")
    
    for result in results:
        table.add_row(
            result["telegram_id"],
            str(result["tasks_completed"])
        )
    
    console.print(table)

def main():
    console.print(BANNER)
    file_path = "data.txt"
    accounts = read_webappdata_from_file(file_path)
    
    if not accounts:
        logger.error("Tidak ada akun yang valid di data.txt")
        return
    
    logger.info(f"Ditemukan {len(accounts)} akun untuk diproses")
    tasks_to_complete = filter_uncompleted_tasks(TASK_DATA["tasks"], TASK_DATA["lastCompletedTasks"])
    logger.info(f"Ditemukan {len(tasks_to_complete)} task yang belum selesai")
    
    # Proses akun dengan thread pool
    results = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(process_account, account) for account in accounts]
        for future in futures:
            results.append(future.result())
    
    # Tampilkan hasil
    display_results(results)
    logger.info("Proses selesai!")

if __name__ == "__main__":
    main()
