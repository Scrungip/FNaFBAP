require 'rbconfig'
require 'fileutils'

module Archipelago

    class Client

        class Data
            attr_reader :roominfo, :connected

            def initialize
                @data_folder = setup_data_folder()
                @roominfo = {}
                @connected = {}
                @checksum_hash = {}
                @datapackage_hash = {}
            end

            def import_roominfo(roominfo)
                @roominfo = Packets::RoomInfo.new(roominfo)
                @checksum_hash = @roominfo.datapackage_checksums
            end

            def import_connected(connected)
                @connected = Packets::Connected.new(connected)
            end

            def check_datapackages
                datapackages_to_update = []

                @checksum_hash.each do |game, checksum|
                    if !Dir.exist?(File.join(@data_folder, game))
                        Dir.mkdir(File.join(@data_folder, game))
                        datapackages_to_update << game
                    elsif !File.exist?(File.join(@data_folder, game, "#{checksum}.json"))
                        datapackages_to_update << game
                    else
                        @datapackage_hash[game] = JSON.parse(File.read(File.join(@data_folder, game, "#{checksum}.json")).sub("\xEF\xBB\xBF".force_encoding("UTF-8"), ''))
                    end
                end

                return datapackages_to_update
            end

            def update_datapackages(datapackage)
                dataPackagePacket = Packets::DataPackage.new(datapackage)

                dataPackagePacket.data["games"].each do |game, datapak|
                    json_filepath = File.join(@data_folder, game, "#{datapak["checksum"]}.json")
                    File.delete(json_filepath) if File.exist?(json_filepath)
                    File.open(json_filepath, 'w') do |file|
                        file.puts datapak.to_json
                        @datapackage_hash[game] = datapak
                    end
                end
            end

            def location_name_from_id(game, id)
                location_name_to_id = @datapackage_hash[game]["location_name_to_id"]

                location_name_to_id.each do |location, value|
                    return location if value == id
                end
                return "Unknown Location"
            end

            def games
                return @roominfo.games
            end

            # TODO: The location_names_from_group function. I cannot find any examples of games with groups.
            # TODO: Other data functions from archipelago.js

            private

            module OS
                WINDOWS = 1
                MACOS = 2
                LINUX = 3
                OTHER = 0
            end

            def get_operating_system

                if RbConfig::CONFIG['host_os'] =~ /mswin|msys|mingw|cygwin|bccwin|wince|emc/
                    return OS::WINDOWS
                elsif RbConfig::CONFIG['host_os'] =~ /darwin/
                    return OS::MACOS
                elsif RbConfig::CONFIG['host_os'] =~ /linux/
                    return OS::LINUX
                else
                    return OS::OTHER
                end

            end

            def setup_data_folder

                operating_system = get_operating_system()
                appdata_folder = File.join(ENV['LOCALAPPDATA'], "Archipelago")
                portable_folder = File.join(".", "Archipelago")
            
                if Dir.exist?(appdata_folder) && operating_system == OS::WINDOWS
                  data_folder = File.join(appdata_folder, "Cache", "datapackage")
                elsif operating_system == OS::WINDOWS
                  FileUtils.mkdir_p(File.join(appdata_folder, "Cache", "datapackage"))
                  data_folder = File.join(appdata_folder, "Cache", "datapackage")
                elsif Dir.exist?(portable_folder)
                  data_folder = File.join(portable_folder, "Cache", "datapackage")
                else
                  FileUtils.mkdir_p(File.join(portable_folder, "Cache", "datapackage"))
                  data_folder = File.join(portable_folder, "Cache", "datapackage")
                end

                return data_folder

            end
        end
    end
end