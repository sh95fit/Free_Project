import asyncio
import websockets

async def send_data():
    uri = "ws://localhost:8000/ws"  # 서버의 WebSocket 엔드포인트 주소로 변경해야 합니다.
    
    async with websockets.connect(uri) as websocket:
        # 연결이 수립되면 서버에 데이터를 전송합니다.
        while True:
            message = input("전송할 메시지를 입력하세요: ")
            await websocket.send(message)
            print(f"> 데이터 전송 완료: {message}")

if __name__ == "__main__":
    asyncio.run(send_data())