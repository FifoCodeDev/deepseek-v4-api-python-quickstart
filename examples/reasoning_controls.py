"""Use explicit reasoning controls for a repeatable DeepSeek V4 call."""

import os

from openai import OpenAI


def main() -> None:
    client = OpenAI(
        api_key=os.environ["COMETAPI_API_KEY"],
        base_url="https://api.cometapi.com/v1",
    )

    response = client.chat.completions.create(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro"),
        messages=[
            {
                "role": "user",
                "content": "Find two edge cases for a JSON API validator.",
            }
        ],
        extra_body={
            "thinking": {"type": "enabled"},
            "reasoning_effort": "high",
        },
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
