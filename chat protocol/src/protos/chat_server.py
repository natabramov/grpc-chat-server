from concurrent import futures
import logging

import grpc
import chat_pb2
import chat_pb2_grpc

class SendChat(chat_pb2_grpc.ChatServerServicer):
    def SendChat(self, request, context):
        return chat_pb2.ChatReply(successful=True)

    def JoinChannel(self, request, context):
        return chat_pb2.JoinReply(successful=True)

    def JoinChannel(self, request, context):
        return chat_pb2.LeaveReply(successful=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServerServicer_to_server(SendChat(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()