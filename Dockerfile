FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim
WORKDIR /app

# LibreOffice Installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice-writer \
    libreoffice-calc \
    libreoffice-l10n-es \
    fonts-noto \
    fonts-dejavu \
    libxtst6 \
    libcups2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

COPY . /app

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "main.py"]
