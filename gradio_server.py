#!/usr/bin/env python
'''
A bare-bones web interface for conversations with LLMs served from openai-compatible endpoints.
'''

import argparse
import os

import gradio as gr
from openai import OpenAI

parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--apikey", default=os.environ.get("OPENAI_API_KEY", "not-needed"))
parser.add_argument("--model", default='llama-3.1-8b-instant')
parser.add_argument("--port", type=int, default=7860)
args = parser.parse_args()

client = OpenAI(base_url=args.url, api_key=args.apikey)


def history_to_messages(history):
    """
    Convert Gradio chat history into OpenAI-compatible messages.

    >>> history_to_messages([{"role": "user", "content": "hi"}])
    [{'role': 'user', 'content': 'hi'}]
    >>> history_to_messages([("hi", "hello")])
    [{'role': 'user', 'content': 'hi'}, {'role': 'assistant', 'content': 'hello'}]
    """
    messages = []
    for entry in history:
        if isinstance(entry, dict):
            messages.append({"role": entry["role"], "content": entry["content"]})
        else:
            user_message, assistant_message = entry
            if user_message is not None:
                messages.append({"role": "user", "content": user_message})
            if assistant_message is not None:
                messages.append({"role": "assistant", "content": assistant_message})
    return messages


def chat(message, history):
    messages = history_to_messages(history)
    messages.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model=args.model,
        messages=messages
    )
    return completion.choices[0].message.content


gr.ChatInterface(chat, type="messages").launch(server_port=args.port)
