=begin
#===============================================================================
 Title: Common Event Queue
 Author: Hime
 Date: Aug 1, 2013
--------------------------------------------------------------------------------
 ** Change log
 Aug 1, 2013
   - Initial release
--------------------------------------------------------------------------------   
 ** Terms of Use
 * Free to use in non-commercial projects
 * Contact me for commercial use
 * No real support. The script is provided as-is
 * Will do bug fixes, but no compatibility patches
 * Features may be requested but no guarantees, especially if it is non-trivial
 * Credits to Hime Works in your project
 * Preserve this header
--------------------------------------------------------------------------------
 ** Description
 
 This script changes the common event system to allow you to reserve multiple
 common events. They are stored in a queue, and are retrieved in a first-in
 first-out order.
 
--------------------------------------------------------------------------------
 ** Installation
 
 Place this script below Materials and above Main
 
--------------------------------------------------------------------------------
 ** Usage

 For developers.
 
 $game_temp.common_event_id returns first ID in the queue. It does not remove
 it from the queue.
 
 $game_temp.reserve_common_event adds a common event ID to the queue.
 
 $game_temp.reserved_common_event returns the first ID in the queue and removes
 it from the queue.
 
#===============================================================================
=end
$imported = {} if $imported.nil?
$imported["TH_CommonEventQueue"] = true
#===============================================================================
# ** Rest of Script
#=============================================================================== 
class Game_Temp
  
  alias :th_common_event_queue_initialize :initialize
  def initialize
    th_common_event_queue_initialize
    @common_event_queue = []
  end
  
  #--------------------------------------------------------------------------
  # Overwrite. Basically look at the first element
  #--------------------------------------------------------------------------
  def common_event_id
    @common_event_queue[0]
  end
  
  #--------------------------------------------------------------------------
  # Overwrite. Enqueue it
  #--------------------------------------------------------------------------
  def reserve_common_event(common_event_id)
    @common_event_queue.push(common_event_id)
  end

  #--------------------------------------------------------------------------
  # Overwrite.
  #--------------------------------------------------------------------------
  def common_event_reserved?
    @common_event_queue.size > 0
  end
  
  #--------------------------------------------------------------------------
  # Overwrite. Dequeue the common event FIFO order.
  #--------------------------------------------------------------------------
  def reserved_common_event
    $data_common_events[@common_event_queue.shift]
  end
end