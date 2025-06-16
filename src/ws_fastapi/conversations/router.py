from fastapi import APIRouter, WebSocket

from ws_fastapi.conversations.services.conversation_ws_processor import ConversationWsProcessor

router = APIRouter()


@router.websocket('/ws/conversations/{conversation_id}')
async def websocket_dialog(ws: WebSocket, conversation_id: str) -> None:
	await ConversationWsProcessor(ws, conversation_id)()
