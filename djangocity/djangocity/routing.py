from channels.routing import route

from votes.consumers import ws_connect, ws_disconnect, vote_saved

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.disconnect", ws_disconnect),
    route("vote-saved", vote_saved)
]