from dataclasses import dataclass

from fastapi import WebSocket, WebSocketDisconnect

from core.interfaces.base import AsyncBaseService
from ws_fastapi.redis import redis


@dataclass
class ConversationWsProcessor(AsyncBaseService):
	ws: WebSocket
	conversation_id: str

	async def receive_from_ws(self) -> None:
		while True:
			data = await self.ws.receive_text()
			await redis.publish(self.conversation_id, data)

	async def act(self) -> None:
		await self.ws.accept()
		try:
			await self.receive_from_ws()
		except WebSocketDisconnect:
			print(f'Disconnected: {self.conversation_id}')
