#!/usr/bin/env python3
"""
YADI77 WHATSAPP SPAMMER v3.0
GitHub: https://github.com/M-YADI/YADI77-WHATSAPP-SPAMMER
EXCLUSIVE FOR M.YADI - CREATOR ABSOLUT
"""

import os
import sys
import json
import time
import random
import webbrowser
from datetime import datetime

try:
    import pyautogui
    PYGUII = True
except ImportError:
    PYGUII = False
    print("[!] pyautogui not installed. Install with: pip install pyautogui")

class YADI77Spammer:
    def __init__(self):
        self.VERSION = "3.0"
        self.CREATOR = "M.YADI"
        self.config = self.load_config()
        self.messages = self.load_messages()
        
        self.target = ""
        self.spam_count = 0
        self.max_spam = self.config.get("max_spam", 200)
    
    def load_config(self):
        """Load configuration from config.json"""
        default_config = {
            "max_spam": 200,
            "typing_speed": 0.01,
            "delay_between": 1.0,
            "creator": "M.YADI",
            "auto_open_browser": True,
            "show_banner": True
        }
        
        try:
            with open("config.json", "r") as f:
                return json.load(f)
        except:
            return default_config
    
    def load_messages(self):
        """Load messages from messages.txt or use default"""
        try:
            with open("messages.txt", "r", encoding="utf-8") as f:
                messages = [line.strip() for line in f if line.strip()]
                if messages:
                    return messages
        except:
            pass
        
        # Default M.YADI messages
        return [
            "⚠️ WARNING: M.YADI ATTACK IN PROGRESS ⚠️",
            "🚨 YOUR WHATSAPP IS BEING DESTROYED 🚨",
            "💀 DEVICE LAG DETECTED - YADI77 ACTIVE 💀",
            "🔥 PHONE OVERHEATING IN 60 SECONDS 🔥",
            "💣 MEMORY CORRUPTION: 75% COMPLETE 💣",
            "⚡ ELECTRICAL SURGE - SYSTEM FAILURE ⚡",
            "🌋 MELTDOWN SEQUENCE INITIATED 🌋",
            "☢️ RADIATION LEAK - EVACUATE DEVICE ☢️",
            "🛑 CRITICAL ERROR: FORMATTING DRIVE 🛑",
            "💥"
