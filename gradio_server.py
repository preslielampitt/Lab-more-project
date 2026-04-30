#!/usr/bin/env python
'''
A bare-bones web interface for conversations with LLMs served from openai-compatible endpoints.
'''

import argparse
import os

from openai import OpenAI


def parse_args(argv=None):
    """
    Parse command-line options for the Gradio server.

    >>> args = parse_args(["--url=http://127.0.0.1:8000/v1"])
    >>> args.url
    'http://127.0.0.1:8000/v1'
    >>> args.apikey
    'not-needed'
    >>> parse_args(["--url=http://127.0.0.1:8000/v1", "--share"]).share
    True
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--apikey", default=os.environ.get("OPENAI_API_KEY", "not-needed"))
    parser.add_argument("--model", default="llama-3.1-8b-instant")
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument("--share", action="store_true")
    return parser.parse_args(argv)


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


def build_chat(client, model):
    """
    Build a Gradio callback backed by an OpenAI-compatible client.
    """
    def chat(message, history):
        messages = history_to_messages(history)
        messages.append({"role": "user", "content": message})
        completion = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return completion.choices[0].message.content

    return chat


def main(argv=None):
    """
    Launch the Gradio chat UI.
    """
    import gradio as gr

    args = parse_args(argv)
    client = OpenAI(base_url=args.url, api_key=args.apikey)
    chat = build_chat(client, args.model)
    gr.ChatInterface(chat).launch(server_port=args.port, share=args.share)


if __name__ == "__main__":
    main()
