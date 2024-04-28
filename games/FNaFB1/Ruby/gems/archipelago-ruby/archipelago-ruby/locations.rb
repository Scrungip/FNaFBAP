module Archipelago

    class Client

        class Locations

            def initialize(data)
                @data = data
                @checked_locations = []
                @missing_locations = []
                @check_index = 0
            end

            def import_check_index(check_index)
                @check_index = check_index if check_index.is_a?(Integer)
                puts "Check index must be an integer!" unless check_index.is_a?(Integer)
            end

            def import_checked_locations(location_list)
                @checked_locations = location_list
            end

            def import_missing_locations(location_list)
                @missing_locations = location_list
            end

            def check(*id_arguments)
                if @client_connect_status == ConnectStatus::CONNECTED
                    id_arguments.each do |id|
                        @checked_locations << id if id.is_a?(Integer)
                    end

                    check_packet = Packets::LocationChecks.new(@checked_locations)
                    @client_socket.send(check_packet.to_json)
                else
                    puts "You need to have an active Archipelago connection to use this!"
                end
            end

            def scout(hint_mode, *id_arguments)
                if @client_connect_status == ConnectStatus::CONNECTED
                    scout_list = []
                    id_arguments.each do |id|
                        scout_list << id if id.is_a?(Integer)
                    end

                    scout_packet = Packets::LocationScouts.new(hint_mode, scout_list)
                    @client_socket.send(scout_packet.to_json)
                else
                    puts "You need to have an active Archipelago connection to use this!"
                end
            end

            def name(game_name, id)
                return @data.location_name_from_id(game_name, id)
            end

            def auto_release
                if @client_connect_status == ConnectStatus::CONNECTED
                    check_packet = Packets::LocationChecks.new(@missing_locations)
                    @client_socket.send(check_packet.to_json)
                else
                    puts "You need to have an active Archipelago connection to use this!"
                end
            end
        end
    end
end