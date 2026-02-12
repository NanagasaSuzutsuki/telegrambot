import html
import io
import requests

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

from core.embed import embed
from core.state import ResearchState
from core.pipeline import run_pipeline


# ==============================
# GLOBAL STATE
# ==============================

fetch_manager = None
user_states = {}


# ==============================
# SEND PAPER LIST
# ==============================

async def send_paper_list(message, results, context):

    message_text = "<b>Recommended papers:</b>\n\n"

    context.user_data["paper_map"] = {}

    for i, paper in enumerate(results, start=1):

        safe_title = html.escape(paper.title)

        message_text += (
            f"{i}. {safe_title}\n"
            f"   Unknown\n"
            f"   /p{i}\n\n"
        )

        context.user_data["paper_map"][str(i)] = paper

    await message.reply_text(
        message_text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )


# ==============================
# HANDLE NORMAL MESSAGE
# ==============================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    text = update.message.text or ""

    context.user_data["last_input"] = text

    if chat_id not in user_states:
        user_states[chat_id] = ResearchState(embed(text))

    state = user_states[chat_id]

    results = run_pipeline(state, fetch_manager, text)

    await send_paper_list(update.message, results, context)


# ==============================
# HANDLE /pX CLICK
# ==============================

async def handle_p_click(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    index = text.replace("/p", "").strip()

    paper_map = context.user_data.get("paper_map", {})

    if index not in paper_map:
        await update.message.reply_text("Paper not found.")
        return

    paper = paper_map[index]

    pdf_url = paper.pdf_url

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(pdf_url, headers=headers, timeout=30)

    if r.status_code != 200:
        await update.message.reply_text("Download failed.")
        return

    file_obj = io.BytesIO(r.content)
    file_obj.name = f"{paper.id}.pdf"

    await update.message.reply_document(file_obj)


# ==============================
# UNIVERSAL ROUTER
# ==============================

async def command_router(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    text = update.message.text or ""

    print("ROUTER GOT:", text)

    # ⭐ 点击论文
    if text.startswith("/p"):
        await handle_p_click(update, context)
        return

    # ⭐ 普通文本 → 推荐
    await handle_message(update, context)


# ==============================
# RUN BOT
# ==============================

def run_bot(token, manager):

    global fetch_manager
    fetch_manager = manager

    app = ApplicationBuilder().token(token).build()

    # ⭐ 一个 handler 管全部
    app.add_handler(MessageHandler(filters.ALL, command_router))

    print("Bot running...")

    app.run_polling()
