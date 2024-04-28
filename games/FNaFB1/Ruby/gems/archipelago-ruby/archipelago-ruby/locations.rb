module Archipelago

    class Client

        class LocationsManager

            def initialize(client)
                @client = client
                @checked_locations = []
                @missing_locations = []
                @datapackages = {}
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

            def import_datapackages(datapackages)
                @datapackages = datapackages if datapackages.is_a?(Hash)
            end

            def check(*id_arguments)
                if @client.client_connect_status == ConnectStatus::CONNECTED
                    id_arguments.each do |id|
                        @checked_locations << id if id.is_a?(Integer)
                    end

                    check_packet = Packets::LocationChecks.new(@checked_locations)
                    @client.client_socket.send(check_packet.to_json)
                else
                    puts "You need to have an active Archipelago connection to use this!"
                end
            end

            def scout(hint_mode, *id_arguments)
                if @client.client_connect_status == ConnectStatus::CONNECTED
                    scout_list = []
                    id_arguments.each do |id|
                        scout_list << id if id.is_a?(Integer)
                    end

                    scout_packet = Packets::LocationScouts.new(hint_mode, scout_list)
                    @client.client_socket.send(scout_packet.to_json)
                else
                    puts "You need to have an active Archipelago connection to use this!"
                end
            end

            def name(game_name, id)
                @datapackages[game]["location_name_to_id"].each do |location, value|
                    return location if value == id
                end
                return "Unknown Location"
            end

            def auto_release
                if @client.client_connect_status == ConnectStatus::CONNECTED
                    check_packet = Packets::LocationChecks.new(@missing_locations)
                    @client.client_socket.send(check_packet.to_json)
                else
                    puts "You need to have an active Archipelago connection to use this!"
                end
            end
        end
    end
end