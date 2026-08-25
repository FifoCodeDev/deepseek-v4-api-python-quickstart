"""Minimal DeepSeek V4 request through CometAPI."""

import os

from openai import OpenAI


def main() -> None:
    api_key = os.environ["COMETAPI_API_KEY"]
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.cometapi.com/v1",
    )

    response = client.chat.completions.create(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro"),
        messages=[
            {
                "role": "user",
                "content": "Review this function and suggest one useful test case.",
            }
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
