#==============================================================================
# ** Archipelago_RGSS3
#------------------------------------------------------------------------------
#  All lines of text that start with # are comments and aren't read as code.
#  They'll appear in GREEN in the RPGMaker VX Ace script editor.
#
#  This script uses archipelago_rb to allow RPGMaker VX Ace games to connect
#  to the Archipelago Multiworld System.
#
#  Make sure you read the documentation to learn how this works after you
#  set this up! (LINK HERE)
#
#  Credits:
#  Author: EggSlashEther
#       (contact@eggslashether.com)
#  Tester: Scrungip
#       (Discord: scrungip)
#  Archipelago: All of the wonderful developers, staff and players
#       (https://archipelago.gg/)
#  mkxp: Ancurio + everyone else who made commits over the years
#       (https://github.com/Ancurio/mkxp)
#  mkxp-z: All of the maintainers + Ancurio's Discord server
#       (https://github.com/mkxp-z/mkxp-z)
#==============================================================================
#==============================================================================
# ** SETUP
#------------------------------------------------------------------------------
#  Ignore me! I'm just importing required libraries. Go to CONFIGURATION!
#==============================================================================
#--------------------------------------------------------------------------
# * Add "Ruby" directory to load path and import archipelago_rb
#--------------------------------------------------------------------------
    ruby_directory = File.join(Dir.pwd, "Ruby")

    $:.push(ruby_directory) unless System.is_mac?

    if File.directory?(ruby_directory)
        Dir.glob(File.join(ruby_directory, '**', '*')).each do |path|
            $:.push(path) if File.directory?(path)
        end
    end

    require 'archipelago_rb'
    require 'io/console'
    require 'json'
#==============================================================================
# ** CONFIGURATION
#------------------------------------------------------------------------------
#  This section allows you to configure basic facts about the game.
#  For simpler RPGMaker VX Ace games, you shouldn't have to delve deeper than
#  this section.
#==============================================================================
#--------------------------------------------------------------------------
# * Basic Details
#  '$archipelago_gamename' is the game name as it appears in your APWorld.
#  '$archipelago_items_handling' determines what items this client can handle.
#    * DEFAULT: Archipelago::ItemsHandlingFlags::REMOTE_ALL
#  '$load_autoconnect' determines if the game will automatically try to
#  reconnect to its multiworld when loading a save.
#    * DEFAULT: true
#  '$receive_items_outside_map' determines if the game will register AP items
#  while the player is not in the main Map Scene. This may include during
#  battle, menus, or other things. This could cause issues depending on how
#  you're handling your items.
#--------------------------------------------------------------------------
    $archipelago_gamename = "Five Nights at Fuckboy's"
    $archipelago_items_handling = Archipelago::ItemsHandlingFlags::REMOTE_ALL
    $load_autoconnect = true
    $receive_items_outside_map = false
#--------------------------------------------------------------------------
# * Progressive Methods
#  This hash contains calls you want to make for progressive items.
#  Each key/value pair should be a symbol and an array of methods in
#  string form. Then, you invoke the method progressive(key) in the
#  receiveditems_methods hash below. Whenever that progressive(key) method
#  is called, it calls the next function in the array. Make sure your keys
#  in receiveditems_methods are escaped!
#  Example:
#   progressive_methods = {
#       sword: [
#           "$game_party.gain_item($data_items[1], 1)",
#           "$game_party.gain_item($data_items[2], 1)",
#           "$game_party.gain_item($data_items[3], 1)"
#       ],
#       wand_upgrade: [
#           "$game_party.gain_item($data_items[(4..6), 1])"
#       ]
#   }
#   receiveditem_methods = {
#       80001 => "progressive(:sword)"
#       80002 => "progressive(:wand_upgrade)"
#   }
#     * When ID 80001 is first received, trigger the first method in the
#     array, in this case granting 1 of Game Item ID 1.
#     * When ID 80001 is received again, the second method in the array
#     triggers, granting 1 of Game Item ID 2.
#     * When ID 80001 is received again again, trigger the third method
#     in the array, granting 1 of Game Item ID 3.
#     * Ranges within brackets (like in the section below) work too!
#     * Like with ID 80002, with Game Item IDs 4 through 6 when called
#     one, two and three times respectively.
#
#  Note: If you ever call a progressive method more times than there are
#  entries in its array, nothing will happen, so don't worry about it.
#  MAKE SURE YOU CALL THE PROGRESSIVE METHOD IN THE ReceivedItem Methods
#  SECTION!
#--------------------------------------------------------------------------
    progressive_methods = {
        # Put your methods here. See the above comment for expected format.
        # Make sure to put a comma after every entry, except the last!
    }
#--------------------------------------------------------------------------
# * ReceivedItem Methods
#  This hash contains the methods you want to call when this
#  client gets a ReceivedItem of a specific ID. This doesn't have to be
#  restricted to only game items! Here's some examples:
#  22111 => "$game_party.gain_item($data_items[11], 22)",
#   * Gives 22 of Item ID 11.
#  100..110 => "$game_party.gain_item($data_items[1], 2)",
#   * 100, 101, etc, 110 each give 2 of Item ID 1.
#  10001..10010 => "$game_party.gain_item($data_items[(1..10)], 1)",
#   * 10001 gives 1 of Item ID 1, 10002 gives 1 of Item ID 2, etc, until 10
#   * Ranges made this way must be in brackets () and both have the same size!
#   * You can include more than one range in the value string, in which case
#   * all ranges must be the same size.
#  33333 => "$game_party.add_actor(1)"
#   * Adds Actor ID 1 to your party.
#  42069 => "$game_variables[1] += 5"
#   * Adds 5 to the 1st game variable.
#  69420 => "SceneManager.goto(Scene_Gameover)"
#   * Triggers a game over.
#  100000..100003 => "progressive(:revolver)"
#   * Triggers the next method in the "revolver" progressive array.
#--------------------------------------------------------------------------
    receiveditem_methods = {
        # Characters
        756782999 => "$game_temp.reserve_common_event(33)", # Freddy
        756783000 => "$game_temp.reserve_common_event(34)", # Bonnie
        756783001 => "$game_temp.reserve_common_event(35)", # Chica
        756783002 => "$game_temp.reserve_common_event(36)", # Foxy
        
        # Weapons
        756783003 => "$game_temp.reserve_common_event(37)", # Progressive Mic
        756783004 => "$game_temp.reserve_common_event(38)", # Progressive Guitar
        756783005 => "$game_temp.reserve_common_event(39)", # Progressive Cupcake
        756783006 => "$game_temp.reserve_common_event(40)", # Progressive Hook
        756783007 => "$game_temp.reserve_common_event(41)", # Dragon Dildo
        
        # Freddy Skills
        756783008 => "$game_temp.reserve_common_event(42)", # Tophat Toss
        756783009 => "$game_temp.reserve_common_event(43)", # Lead Stinger
        756783010 => "$game_temp.reserve_common_event(44)", # Toreador March
        
        # Bonnie Skills
        756783011 => "$game_temp.reserve_common_event(45)", # Bunny Hop
        756783012 => "$game_temp.reserve_common_event(46)", # Backup Bash
        756783013 => "$game_temp.reserve_common_event(47)", # Guitar Riff
        
        # Chica Skills
        756783014 => "$game_temp.reserve_common_event(48)", # Fearless Flight
        756783015 => "$game_temp.reserve_common_event(49)", # Pizza Pass
        756783016 => "$game_temp.reserve_common_event(50)", # Caffeine Revival
        
        # Foxy Skills
        756783017 => "$game_temp.reserve_common_event(51)", # Plank Walk
        756783018 => "$game_temp.reserve_common_event(52)", # Speed Share
        756783019 => "$game_temp.reserve_common_event(53)", # Rushdown
        
        # Combos
        756783020 => "$game_temp.reserve_common_event(54)", # Fazbear Combo
        756783021 => "$game_temp.reserve_common_event(55)", # Flighty Combo
        756783022 => "$game_temp.reserve_common_event(56)", # Bonbon Combo
        756783023 => "$game_temp.reserve_common_event(57)", # Pirate Combo
        
        # Armors
        756783024 => "$game_temp.reserve_common_event(58)", # Body Endoskeletons
        756783025 => "$game_temp.reserve_common_event(59)", # Head Endoskeletons
        756783026 => "$game_temp.reserve_common_event(60)", # Pizza Shields
        756783027 => "$game_temp.reserve_common_event(61)", # Caffeine Sodas
        756783028 => "$game_temp.reserve_common_event(62)", # Lucky Soda
        756783029 => "$game_temp.reserve_common_event(63)", # Double Pizza
        756783030 => "$game_temp.reserve_common_event(64)", # Ice Water
        756783031 => "$game_temp.reserve_common_event(65)", # Sneaky Juice
        756783032 => "$game_temp.reserve_common_event(66)", # Stealth Preserve
        756783033 => "$game_temp.reserve_common_event(67)", # Heist Cream
        756783034 => "$game_temp.reserve_common_event(68)", # Lunate Wine
        756783035 => "$game_temp.reserve_common_event(69)", # Thrifty Pretzels
        
        # Quest Items
        756783036 => "$game_temp.reserve_common_event(70)", # Lighter
        756783037 => "$game_temp.reserve_common_event(71)", # Bonnie's Head Voucher
        756783038 => "$game_temp.reserve_common_event(72)", # Bonnie's Head
        756783039 => "$game_temp.reserve_common_event(73)", # Kitchen Key
        756783040 => "$game_temp.reserve_common_event(74)", # Reveal Interior Walls
        756783041 => "$game_temp.reserve_common_event(75)", # Office Key Piece
        756783042 => "$game_temp.reserve_common_event(76)", # Backroom BB
        756783043 => "$game_temp.reserve_common_event(77)", # Restrooms BB
        756783044 => "$game_temp.reserve_common_event(78)", # Supply Closet BB
        756783045 => "$game_temp.reserve_common_event(79)", # East Hall Corner BB
        
        # Filler
        756783046 => "$game_temp.reserve_common_event(80)", # Small Pizza
        756783047 => "$game_temp.reserve_common_event(81)", # Medium Pizza
        756783048 => "$game_temp.reserve_common_event(82)", # Large Pizza
        756783049 => "$game_temp.reserve_common_event(83)", # Small Soda
        756783050 => "$game_temp.reserve_common_event(84)", # Medium Soda
        756783051 => "$game_temp.reserve_common_event(85)", # Large Soda
        756783052 => "$game_temp.reserve_common_event(86)", # Pizza Slice
        756783053 => "$game_temp.reserve_common_event(87)", # Cake
        756783054 => "$game_temp.reserve_common_event(88)", # Birthday Present
        756783055 => "$game_temp.reserve_common_event(89)", # X-Large Pizza
        756783056 => "$game_temp.reserve_common_event(90)", # X-Large Soda
        756783057 => "$game_temp.reserve_common_event(91)", # HP Boost
        756783058 => "$game_temp.reserve_common_event(92)", # MP Boost
        756783059 => "$game_temp.reserve_common_event(93)", # Attack Boost
        756783060 => "$game_temp.reserve_common_event(94)", # Defense Boost
        756783061 => "$game_temp.reserve_common_event(95)", # Interior Walls Key
        756783062 => "$game_temp.reserve_common_event(96)", # 100 Tokens
        756783063 => "$game_temp.reserve_common_event(97)", # 500 Tokens
        756783064 => "$game_party.gain_item($data_items[44], 1)",# Puppet's Strings
        756783065 => "$game_temp.reserve_common_event(98)", # Funky Scrungip Token
        
        # Extra Game Content
        780000001 => "$game_temp.reserve_common_event(99)",  # 1-Up Mushroom
        780000002 => "$game_temp.reserve_common_event(100)", # Hylian Shield
        780000003 => "$game_temp.reserve_common_event(101)", # Chaos Emerald
        780000004 => "$game_temp.reserve_common_event(32)",  # Dreamer's Crown
        780000005 => "$game_temp.reserve_common_event(102)", # Blade
        780000006 => "$game_temp.reserve_common_event(103)", # The Big Red Button
        780000007 => "$game_temp.reserve_common_event(104)", # Varia Suit
        780000008 => "$game_temp.reserve_common_event(105)", # Warp Star
        780000009 => "$game_temp.reserve_common_event(106)", # Dream Nail
        780000010 => "$game_temp.reserve_common_event(107)", # Moon Pearl
        780000011 => "$game_temp.reserve_common_event(108)", # Mega Buster
        780000012 => "$game_temp.reserve_common_event(109)", # Roc's Feather
        780000013 => "$game_temp.reserve_common_event(110)", # Lawbot Disguise
        780000014 => "$game_temp.reserve_common_event(111)", # Hookshot Badge
        780000015 => "$game_temp.reserve_common_event(112)", # Reflect Element
        780000016 => "$game_temp.reserve_common_event(113)", # HM04 Strength
        780000017 => "$game_temp.reserve_common_event(114)", # Toy Freddy
        780000018 => "$game_temp.reserve_common_event(115)", # 1 Puzzle Piece
        780000019 => "$game_temp.reserve_common_event(116)", # P
        780000020 => "$game_temp.reserve_common_event(117)", # Star Fox Credits Theme
        780000021 => "$game_temp.reserve_common_event(118)", # Scooby Snack
        780000022 => "$game_temp.reserve_common_event(119)", # Anime catboy transformaation potion
        780000023 => "$game_temp.reserve_common_event(120)", # Lava Badge
        780000024 => "$game_temp.reserve_common_event(121)"  # The Fog is Coming
    }
#==============================================================================
# ** ADVANCED
#------------------------------------------------------------------------------
#  For more complicated games - or more advanced users - additional options
#  are provided here to further customize how this integration works.
#==============================================================================
#--------------------------------------------------------------------------
# * RingLink
#  RingLink is a protocol that essentially links all players' currencies
#  together. Enable it by setting the value to true. You can change the
#  conversion rate to any int/float.
#    * DEFAULT: ringlink_enabled = false, ringlink_conversion_rate = 1
#--------------------------------------------------------------------------
    ringlink_enabled = false
    $ringlink_conversion_rate = 1
#==============================================================================
# ** CODE
#------------------------------------------------------------------------------
#  The feeble should not proceed past this point. Here be dragons.
#==============================================================================
#--------------------------------------------------------------------------
# * Method: Get ranges from string
#--------------------------------------------------------------------------
    def get_rng_from_str(string)
        range_regex = /\((\d+)(\.{2,3})(\d+)\)/
                ranges = []

        string.scan(range_regex) do |match|
            start_value = match[0].to_i
            end_value = match[2].to_i
            inclusive = match[1] == '..'
            ranges << (inclusive ? (start_value..end_value) : (start_value...end_value))
        end

        ranges.empty? ? false : ranges
    end
#--------------------------------------------------------------------------
# * Method: Replace all ranges in string with placeholder
#--------------------------------------------------------------------------
    def replace_rng_with_pl(string)
        range_regex = /\((\d+)(\.{2,3})(\d+)\)/

                ranges = string.scan(range_regex)
        string = string.gsub(range_regex, "\uFFFC") if ranges.any?

        return string
    end
#--------------------------------------------------------------------------
# * Method: Replace all placeholders in string with integers
#--------------------------------------------------------------------------
    def replace_pl_with_int(string, ints)
        i = -1

        modified_string = string.gsub(/\uFFFC/) do |match|
            i += 1
            ints[i]
        end

        return modified_string
    end
#--------------------------------------------------------------------------
# * Method: Expand Progressive methods into new hash (with arrays)
#--------------------------------------------------------------------------
    def expand_progressive_methods(progressive_methods)
        expanded_progressive_methods = {}

        progressive_methods.each do |key, value|
            iterate_to = 0
            pro_method_array = []
            value.each do |pro_method|
                ranges = get_rng_from_str(pro_method)
                if ranges
                    modding_string = replace_rng_with_pl(pro_method)
                    ranges.each do |range|
                        iterate_to = range.to_a.length if (iterate_to == 0) || (range.to_a.length < iterate_to)
                    end
                    iterate_to.times do |i|
                        ints_to_add = []
                        ranges.each do |range|
                            ints_to_add << (range.to_a[i])
                        end
                        modded_string = replace_pl_with_int(modding_string, ints_to_add)
                        pro_method_array << modded_string
                    end
                else
                    pro_method_array << pro_method
                end
            end
            expanded_progressive_methods[key] = pro_method_array
        end

        return expanded_progressive_methods
    end
#--------------------------------------------------------------------------
# * Method: Expand ReceivedItem methods into new hash
#--------------------------------------------------------------------------
    def expand_receiveditem_methods(receiveditem_methods)
        expanded_receiveditem_methods = {}

        receiveditem_methods.each do |key, value|
            if key.is_a?(Range)
                ranges = get_rng_from_str(value)
                if ranges
                    modding_string = replace_rng_with_pl(value)
                    key.each_with_index do |v, i|
                        ints_to_add = []
                        ranges.each do |range|
                            ints_to_add << (range.to_a[i])
                        end
                        modded_string = replace_pl_with_int(modding_string, ints_to_add)
                        expanded_receiveditem_methods[v] = modded_string
                    end
                else
                    key.each do |v|
                        expanded_receiveditem_methods[v] = value
                    end
                end
            else
                expanded_receiveditem_methods[key] = value
            end
        end

        return expanded_receiveditem_methods
    end
#--------------------------------------------------------------------------
# * Expand method hashes into new hashes
#--------------------------------------------------------------------------
    $expanded_progressive_methods = expand_progressive_methods(progressive_methods)
    $expanded_receiveditem_methods = expand_receiveditem_methods(receiveditem_methods)
#--------------------------------------------------------------------------
# * Method: Eval progressive methods
#--------------------------------------------------------------------------
    $progressive_counts = {}
    def progressive(key)
        if $expanded_progressive_methods.include?(key)
            $progressive_counts[key] = 0 unless $progressive_counts.include?(key)
            eval_target = $expanded_progressive_methods[key].fetch($progressive_counts[key], "puts \"[Archipelago_RGSS3] No defined method for index #{$progressive_counts[key]} in key #{key} in progressive_methods!\"")
            eval(eval_target)
            $progressive_counts[key] += 1
        else
            puts "[Archipelago_RGSS3] Key \"#{key}\" not found in progressive_methods!"
        end
    end
#--------------------------------------------------------------------------
# * Method: Use Text Input for details
#--------------------------------------------------------------------------
    def text_input(prompt)
        Input.update
        Graphics.update

        # A buffer to store the text in
        text = ""

        # Turn on text input
        Input.text_input = true

        # Wait until Enter gets pressed
        until Input.triggerex?(:RETURN)

            # Check for Ctrl+C and Ctrl+V!
            if Input.pressex?(:LCTRL) || Input.pressex?(:RCTRL)
                Input.clipboard = text if Input.triggerex?(:C)
                # << is faster than +=
                text << Input.clipboard if Input.triggerex?(:V)
            elsif Input.triggerex?(:BACKSPACE) or Input.timeex?(:BACKSPACE) >= 0.75
                text = text.chop
            else
                text << Input.gets
            end

            # Next frame
            Input.update
            Graphics.update
            $stdout.clear_screen
            puts "#{prompt} #{text}"
        end
        Input.text_input = false
        $stdout.clear_screen
        return text
    end
#--------------------------------------------------------------------------
# * Method: Use Keyboard Input to get connect details
#--------------------------------------------------------------------------
    def get_connect_details
        hostname = text_input("Hostname (will default to archipelago.gg if left blank):")
        port = text_input("Port:")
        name = text_input("Seat name:")
        password = text_input("Password (can be blank):")
        ringlink = text_input("Enable RingLink? (type \"true\" or \"false\"):")

        $archipelago.connect_info["hostname"] = hostname.empty? ? "archipelago.gg" : hostname
        $archipelago.connect_info["port"] = port.to_i
        $archipelago.connect_info["name"] = name
        $archipelago.connect_info["password"] = password unless password.empty?
        if ringlink == "true"
            $ringlink_enabled = true
        else
            $ringlink_enabled = false
        end
    end
#--------------------------------------------------------------------------
# * Create a new TextInput Scene
#--------------------------------------------------------------------------
    class Scene_APConnectInput < Scene_Base
        def start
            super
            draw_image
        end
        def post_start
            super
            begin_text_input
            return_scene
        end
        def draw_image
            @pic = Sprite.new
            @pic.bitmap=Cache.custom("Pictures/text_input")
        end
        def begin_text_input
            get_connect_details
            $archipelago.connect
        end
        def update
            super
        end
    end
#--------------------------------------------------------------------------
# * Add get_connect method to Archipelago module
#--------------------------------------------------------------------------
    module Archipelago
        class Client
            def get_connect
                SceneManager.call(Scene_APConnectInput) unless @client_connect_status == Archipelago::ConnectStatus::CONNECTED
            end
        end
    end
#--------------------------------------------------------------------------
# * Method: Set up common Archipelago startup details
#--------------------------------------------------------------------------
    
    def restart_archipelago
        
        $ap_tags = []
        $ap_tags.append("RingLink") if $ringlink_enabled

        $archipelago = Archipelago::Client.new
        $archipelago.connect_info["game"] = $archipelago_gamename
        $archipelago.connect_info["items_handling"] = $archipelago_items_handling
        $archipelago.connect_info["tags"] = $ap_tags
    #----------------------------------------------------------------------
    # * On Connected: Begin ItemHandling thread
    #----------------------------------------------------------------------
        # This is extremely bad and I wish I did not have to do this
        unhandled_items = Queue.new
        $archipelago.add_listener("Connected") do |msg|
            Thread.new do
                loop do
                    if $receive_items_outside_map
                        item = unhandled_items.pop(true) rescue nil
                        if item
                            eval_target = $expanded_receiveditem_methods.fetch(item, "puts \"[Archipelago_RGSS3] No defined method for ReceivedItem ID #{item}!\"")
                            eval(eval_target)
                            sleep 0.1
                        else
                            sleep 0.1
                        end
                    else
                        # This ensures that items are not received until the game is in a valid scene
                        if SceneManager.scene_is?(Scene_Map)
                            item = unhandled_items.pop(true) rescue nil
                            if item
                                eval_target = $expanded_receiveditem_methods.fetch(item, "puts \"[Archipelago_RGSS3] No defined method for ReceivedItem ID #{item}!\"")
                                eval(eval_target)
                                sleep 0.1
                            else
                                sleep 0.1
                            end
                        else
                            sleep 0.5
                        end
                    end
                    break if $archipelago.client_connect_status == Archipelago::ConnectStatus::DISCONNECTED
                end
            end
        end

    #----------------------------------------------------------------------
    # * On ReceivedItems: Process Index, push item to handler
    #----------------------------------------------------------------------

        $receiveditems_index = 0
        $archipelago.add_listener("ReceivedItems") do |msg|
            item_counter = msg["index"]

            msg["items"].each do |item|
                if $receiveditems_index <= item_counter
                    unhandled_items.push(item["item"])
                    $receiveditems_index += 1
                end
                item_counter += 1
            end
        end

        # For future me, here's the old code but commented out
        #$receiveditems_index = 0
        #$archipelago.add_listener("ReceivedItems") do |msg|
        #    item_counter = msg["index"]
        #
        #    msg["items"].each do |item|
        #        if $receiveditems_index == item_counter
        #            eval_target = $expanded_receiveditem_methods.fetch(item, "puts \"[Archipelago_RGSS3] No defined method for ReceivedItem ID #{item}!\"")
        #            eval(eval_target)
        #            $receiveditems_index += 1
        #        end
        #        item_counter += 1
        #    end
        #end

    #----------------------------------------------------------------------
    # * On Bounced, RingLink: Change currency
    #----------------------------------------------------------------------

        $archipelago.add_listener("Bounced") do |msg|
            if msg["tags"].include?("RingLink") and $ringlink_uuid != msg["data"]["source"]
                $game_party.gain_gold_ringlink((msg["data"]["amount"] * $ringlink_conversion_rate).to_i)
            end
        end
    end
#--------------------------------------------------------------------------
# * Override Cache to load Custom icons
#--------------------------------------------------------------------------
    module Cache
        def self.custom(filename)
            load_bitmap("Custom/Graphics/", filename)
        end
    end
#--------------------------------------------------------------------------
# * Override DataManager save/load methods
#--------------------------------------------------------------------------
    module DataManager
        def self.make_save_contents
            contents = {}
            contents[:system]        = $game_system
            contents[:timer]         = $game_timer
            contents[:message]       = $game_message
            contents[:switches]      = $game_switches
            contents[:variables]     = $game_variables
            contents[:self_switches] = $game_self_switches
            contents[:actors]        = $game_actors
            contents[:party]         = $game_party
            contents[:troop]         = $game_troop
            contents[:map]           = $game_map
            contents[:player]        = $game_player
            contents[:AP_connect_info] = $archipelago.connect_info if $load_autoconnect
            contents[:AP_receiveditems_index] = $receiveditems_index
            contents[:AP_progressive_counts] = $progressive_counts
            contents[:AP_ringlink_enabled] = $ringlink_enabled
            contents[:AP_ringlink_conversion_rate] = $ringlink_conversion_rate
            contents
        end

        def self.extract_save_contents(contents)
            $game_system        = contents[:system]
            $game_timer         = contents[:timer]
            $game_message       = contents[:message]
            $game_switches      = contents[:switches]
            $game_variables     = contents[:variables]
            $game_self_switches = contents[:self_switches]
            $game_actors        = contents[:actors]
            $game_party         = contents[:party]
            $game_troop         = contents[:troop]
            $game_map           = contents[:map]
            $game_player        = contents[:player]
            $archipelago.connect_info = contents[:AP_connect_info] if $load_autoconnect
            $receiveditems_index = contents[:AP_receiveditems_index]
            $progressive_counts = contents[:AP_progressive_counts]
            $ringlink_enabled = contents[:AP_ringlink_enabled]
            $ringlink_conversion_rate = contents[:AP_ringlink_conversion_rate]
        end

        def self.load_game(index)
            load_game_without_rescue(index)
            $archipelago.connect if $load_autoconnect
        rescue
            false
        end
    end
#--------------------------------------------------------------------------
# * Prepend Scene_Title.start to kill Archipelago connection
#--------------------------------------------------------------------------
    module Scene_Title_Disconnect
        def start
            $archipelago.disconnect if $archipelago
            restart_archipelago
            super
        end
    end

    Scene_Title.prepend(Scene_Title_Disconnect)

#--------------------------------------------------------------------------
# * RingLink: Setup RingLink by adding new methods
#--------------------------------------------------------------------------

    if $ringlink_enabled
        $ringlink_uuid = rand(0..1000000)
        module RingLink_Methods
            def gain_gold(amount)
                ringlink_packet = [{cmd: "Bounce", tags: ["RingLink"], data: {time: Time.now.to_i, source: $ringlink_uuid, amount: amount * $ringlink_conversion_rate}}].to_json
                $archipelago.client_socket.send(ringlink_packet)
                super(amount)
            end

            def gain_gold_ringlink(amount)
                @gold = [[@gold + amount, 0].max, max_gold].min
            end
        end

        Game_Party.prepend(RingLink_Methods)
    end


