import mesop as me
import mesop.labs as mel

import time
import random


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  # path="/chat",
  title="Jin-chan Chat",
)

def page():
  mel.chat(transform, title="Jin-chan Chat", bot_user="Jin-chan Bot")


def transform(input: str, history: list[mel.ChatMessage]):
  for line in random.sample(LINES, random.randint(1, min(3, len(LINES) - 1))):
    time.sleep(0.3)
    yield line + " "


LINES = [
    "Jin is very busy with various activities and responsibilities. Despite the hectic schedule, Jin doesn't care about what others say and always finds a way to have some fun. Balancing work and leisure, Jin believes in enjoying life to the fullest.",
    "Daily Life",
    "Busy Schedule: Jin's days are packed with work, projects, and personal pursuits. Staying organized and managing time effectively is key to handling everything smoothly.",
    "Independent Spirit: Jin values independence and pays little attention to others' opinions. This mindset helps in staying focused and confident in decisions and actions.",
    "Enjoyment and Fun: Amidst the busy life, Jin always carves out time for fun activities. Whether it's a hobby, a quick getaway, or just relaxing, having fun is an essential part of Jin's routine.",
    "Work and Projects",
    "As a Project Manager in IT, Jin handles multiple projects with efficiency and expertise. Always looking for innovative solutions and ways to improve, Jin's work is characterized by dedication and a proactive approach.",
    "Hobbies and Interests",
    "Reading: Jin loves to dive into books, exploring different genres and gaining new knowledge.",
    "Walking: Taking walks is a favorite pastime, providing a chance to unwind and stay active.",
    "Coding: Despite being busy with managerial tasks, Jin finds time to indulge in coding, staying connected to the technical aspects of the IT world.",
    "Sleeping: Rest is crucial, and Jin ensures to get quality sleep to recharge for the busy days ahead."
]
