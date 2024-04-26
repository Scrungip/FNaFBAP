require_relative 'packets'
require_relative 'constants'
require_relative 'objects'
require_relative 'location'
require 'websocket-client-simple'
require 'json'

module Archipelago

    class Client
        include Location

        def initialize()
            @client_version = Objects::Version.new(0, 4, 5)
            @client_connect_status = ConnectStatus::DISCONNECTED
            @checked_locations = []
            @missing_locations = []
            @listeners = Hash.new { |hash, key| hash[key] = []}
        end

        def connect(connect_info)
            return if @client_connect_status != ConnectStatus::DISCONNECTED
            Thread.new do
                @connect_info = connect_info
                url = "wss://#{@connect_info["hostname"]}:#{@connect_info["port"]}"
                @client_socket = WebSocket::Client::Simple.connect(url) # Assign to instance variable
            
                @client_socket.on :open do
                end
            
                # Get a reference to the instance method
                packet_handler = method(:notify_listeners)
            
                @client_socket.on :message do |msg|
                    packet_handler.call(msg)
                end
            
                @client_socket.on :error do |e|
                    puts "-- error (#{e.inspect})"
                end
            
                @client_socket.on :close do
                end
            
                loop do
                    STDIN.gets.strip
                end
            end
        end

        def disconnect()
            if @client_socket
                @client_socket.close
                @client_connect_status = ConnectStatus::DISCONNECTED
                puts "Client disconnected."
            end
        end

        def add_listener(packet_type, &block)
            @listeners[packet_type] << block
        end

        def say(text)
            if @client_connect_status == ConnectStatus::CONNECTED
                say_packet = Packets::Say.new(text)
                @client_socket.send(say_packet.to_json)
            else
                puts "You need to have an active Archipelago connection to use this!"
            end
        end

        def update_status(status)
            if @client_connect_status == ConnectStatus::CONNECTED
                status_packet = Packets::StatusUpdate.new(status)
                @client_socket.send(status_packet.to_json)
            else
                puts "You need to have an active Archipelago connection to use this!"
            end
        end

        private

        def notify_listeners(msg)
            if @client_connect_status != ConnectStatus::CONNECTED
                handshake(msg)
            else
                if valid_json?(msg.data)
                    packetString = JSON.parse(msg.data)[0]
                    @listeners[packetString["cmd"]].each { |listener| listener.call(msg)}
                elsif msg.type == :ping
                    @client_socket.send(msg.data, type: :pong)
                else
                    puts msg
                end
            end
        end
        
        def handshake(msg)
            # TODO: Move the handshake protocol into its own function
            if @client_connect_status == ConnectStatus::DISCONNECTED
                # Expecting RoomInfo packet.
                roomInfoPacket = Packets::RoomInfo.new(msg.data)
                if roomInfoPacket.cmd != "RoomInfo"
                    puts "ERROR: Recieved packet type #{roomInfoPacket.cmd}. Expecting RoomInfo packet."
                    @client_socket.close
                end

                if roomInfoPacket.password
                    puts "Password:"
                    password = STDIN.gets.strip
                else
                    password = nil
                end

                connect_packet = Packets::Connect.new(
                    password, 
                    @connect_info["game"], 
                    @connect_info["name"], 
                    "99999", 
                    @client_version.to_hash, 
                    @connect_info["items_handling"], 
                    ["AP"], 
                    false
                )
                # RoomInfo confirmed. Attempt connection.
                @client_socket.send(connect_packet.to_json)
                @client_connect_status = ConnectStatus::CONNECTING
            elsif @client_connect_status == ConnectStatus::CONNECTING
                connectionPacket = JSON.parse(msg.data)[0]
                case connectionPacket["cmd"]
                when "Connected"
                    puts "Connection successful!"
                    import_checked_locations(connectionPacket["checked_locations"])
                    import_missing_locations(connectionPacket["missing_locations"])
                    @client_connect_status = ConnectStatus::CONNECTED
                when "ConnectionRefused"
                    puts "Connection rejected!"
                else
                    puts "ERROR: Recieved packet type #{connectionPacket["cmd"]}. Expecting Connection/ConnectionRefused packet."
                end
            end
        end
    end
end
