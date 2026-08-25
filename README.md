# DeepSeek V4 API Python Quickstart with CometAPI

Runnable Python examples for calling the currently available DeepSeek V4 models through CometAPI's OpenAI-compatible API.

> **Quick answer:** use `deepseek-v4-pro` for harder reasoning, coding, and agent tasks; use `deepseek-v4-flash` for faster, higher-throughput workflows. The CometAPI endpoint is `https://api.cometapi.com/v1`.

DeepSeek V4.1 is being discussed, but it is not an officially released model with a public model card or release date. This repository focuses on the confirmed V4 API surface and keeps the V4.1 forecast separate from production-ready examples.

## What this repository includes

- OpenAI-compatible Python quickstart
- Streaming responses
- Explicit thinking and reasoning-effort controls
- Environment-variable configuration
- Model-selection guidance for Pro versus Flash
- Source links to CometAPI and DeepSeek documentation

## Install

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

Create a local environment file from `.env.example`, or set the variable directly:

```bash
# macOS / Linux
export COMETAPI_API_KEY="YOUR_COMETAPI_KEY"

# Windows PowerShell
$env:COMETAPI_API_KEY = "YOUR_COMETAPI_KEY"
```

Never commit a real API key. The included `.gitignore` excludes `.env` files.

## First request

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMETAPI_API_KEY"],
    base_url="https://api.cometapi.com/v1",
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {
            "role": "user",
            "content": "Review this function and suggest one useful test case.",
        }
    ],
)

print(response.choices[0].message.content)
```

Run it with:

```bash
python examples/quickstart.py
```

## Choose the right model

| Model | Best fit | Main trade-off |
| --- | --- | --- |
| `deepseek-v4-pro` | Complex reasoning, coding, long-horizon agents | Higher-capability route with more latency or cost |
| `deepseek-v4-flash` | High-throughput calls, extraction, triage, repeated agent steps | Efficiency-focused route for speed and volume |

Both model IDs are available on CometAPI's live model pages. Verify availability and pricing before production deployment.

## Stream a response

Streaming improves perceived latency for long coding or research responses:

```bash
python examples/streaming.py
```

The example uses `stream=True` and prints text deltas as they arrive.

## Control thinking and reasoning effort

For reproducible evaluations, set the reasoning fields explicitly:

```bash
python examples/reasoning_controls.py
```

The example sends the provider-specific fields through the OpenAI SDK's `extra_body` argument:

```python
extra_body={
    "thinking": {"type": "enabled"},
    "reasoning_effort": "high",
}
```

Test lower-effort or disabled-thinking configurations for simple, latency-sensitive work when supported by the live route.

## API reference

| Setting | Value |
| --- | --- |
| Base URL | `https://api.cometapi.com/v1` |
| Endpoint | `POST /chat/completions` |
| Pro model ID | `deepseek-v4-pro` |
| Flash model ID | `deepseek-v4-flash` |
| SDK | `openai` Python package |
| Authentication | `Authorization: Bearer $COMETAPI_API_KEY` |

## Production checklist

1. Keep the API key in a secret manager or environment variable.
2. Pin the model ID in configuration rather than accepting arbitrary user input.
3. Compare Pro and Flash on representative prompts.
4. Record latency, tokens, retries, and successful-task rate.
5. Add timeouts and retry handling around network calls.
6. Re-check the live model page and DeepSeek release log before deployment.

## FAQ

### Is DeepSeek V4.1 available through this repository?

No. V4.1 is not treated as a confirmed production model here. The examples use the currently listed `deepseek-v4-pro` and `deepseek-v4-flash` identifiers.

### Which model should I start with?

Start with `deepseek-v4-pro` for difficult coding and agent tasks. Try `deepseek-v4-flash` when throughput, latency, or repeated calls matter most.

### Does the API use the OpenAI SDK?

Yes. Set the CometAPI base URL and API key, then use the standard `chat.completions.create` interface.

### Will model IDs or pricing change?

They can change. Check the live CometAPI model page and provider documentation before pinning a production integration.

## Links

- [CometAPI: DeepSeek V4.1 research and current status](https://www.cometapi.com/deepseek-v4-1-coming-soon/?utm_source=github&utm_medium=organic&utm_campaign=deepseek_v4_1_api_guide&utm_content=readme)
- [CometAPI: DeepSeek V4 Pro API](https://www.cometapi.com/models/deepseek/deepseek-v4/?utm_source=github&utm_medium=organic&utm_campaign=deepseek_v4_1_api_guide&utm_content=readme)
- [CometAPI: DeepSeek V4 Flash API](https://www.cometapi.com/models/deepseek/deepseek-v4-flash/?utm_source=github&utm_medium=organic&utm_campaign=deepseek_v4_1_api_guide&utm_content=readme)
- [DeepSeek API release log](https://api-docs.deepseek.com/updates/)

## Disclosure

This is an original, code-focused developer adaptation based on the linked sources. CometAPI model availability, pricing, and API fields can change; verify the live documentation before shipping.
