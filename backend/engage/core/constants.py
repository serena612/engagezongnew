from common.mixins import LabelChoices


class WinAction(LabelChoices):
    PLAY_GAME = 'play_game', 'Play one game'
    JOIN_TOURNAMENT = 'join_tournament', 'Participate in a tournament'
    WATCH_VIDEO = 'watch_video', 'Watch a video'
    INVITE_FRIEND = 'invite_friend', 'Invite a friend to Engage'
    CHALLENGE_FRIEND = 'challenge_friend', 'Challenge a friend to any game'
    PLAY_WITH_FRIEND = 'play_with_friend', 'Play any game with a friend'
    WATCH_2_VIDEOS = 'watch_2_videos', 'Watch two videos'
    PLAY_2_GAMES = 'play_2_games', 'Play any two games'
    WIN_TOURNAMENT = 'win_tournament', 'Win a tournament'


class SupportedGame(LabelChoices):
    DOTA2 = 'dota2', 'Dota 2',
    CLASH_ROYALE = 'clash_royale', 'Clash Royale'
    PUBG = 'pubg', 'PUGB'
    COD = 'cod', 'Call Of Duty'
    FIFA = 'fifa', 'Fifa'


class EventType(LabelChoices):
    SHOW = 'show', 'SHOWS'
    AFFILIATE = 'affiliate', 'AFFILIATES'
    EVENT = 'event', 'EVENTS'


class HTML5GameType(LabelChoices):
    FREE = 'free', 'Free Game'
    PREMIUM = 'premium', 'Premium Game'
    EXCLUSIVE = 'exclusive', 'Exclusive Game'


class HTML5GameOption(LabelChoices):    
    ADVENTURE_QUIZ = 'adventure_quiz', 'Adventure Quiz'
    ANGRY_ZOMBIES = 'angry_zombies', 'Angry Zombies'
    ALIEN_VS_MATH = 'alien_vs_math', 'Alien vs Math'
    ANIMALS_MEMORY = 'animals_memory', 'Animals Memory'
    CANNON_BALL = 'cannon_ball', 'Cannon Ball'
    CAT_JUMP = 'cat_jump', 'Cat Jump'
    CAT_VS_DOG = 'cat_vs_dog', 'Cat Vs Dog'
    CONQUER_YOUR_LOVE = 'conquer_your_love', 'Conquer your love'
    GALAXY_DOMINATION = 'galaxy_domination', 'Galaxy Domination'
    MAD_SHARK = 'mad_shark', 'Mad Shark'
    MEMORY_ANIMAL_GAME = 'memory_animal_game', 'Memory Animal Game'
    PREHISTORIC_WARFARE = 'prehistoric_warfare', 'Prehistoric Warfare'
    SLICE_FRUIT = 'slice_fruit', 'Slice Fruit'
    SOCCER_HEROES = 'soccer_heroes', 'Soccer Heroes'
    SPOT_THE_DIFFERENCE = 'spot_the_difference', 'Spot the Difference'
    SUPER_QUIZ_XML = 'super_quiz_xml', 'Super Quiz XML'
    SWEET_MEMORY = 'sweet_memory', 'Sweet Memory'
    SAVE_ROCKET = 'save_rocket','Save Rocket'
    RISKY_WAY = 'risky_way','Risky Way'
    EXIT = 'exit','Exit'
    DOTS_PUZZLE = 'dots_puzzle','Dots Puzzle'
    HOLE = 'hole','Hole'
    RED_JUMPER = 'red_jumper','Red Jumper'
    TURKEY_ADVENTURE = 'turkey_adventure','Turkey Adventure'
    STICKY_BALLS = 'sticky_balls','Sticky Balls'
    PASSAGE = 'passage','Passage'
    SPIRAL_PAINT = 'spiral_paint','Spiral Paint'
    FALLING_NUMBERS = 'falling_numbers','Falling Numbers'
    MERGE_NUMBERS = 'merge_numbers','Merge Numbers'
    SNACK_CIRCLE = 'snack_circle','Snack and Circle'
    TRIANGLE_WAY = 'triangle_way','Triangle Way'
    NEON_BLOCK = 'neon_block','Neon Block'
    MATCH3_MANIA = 'match3_mania','Match3 Mania'
    PLAIT_PUZZLE = 'plait_puzzle','Plait Puzzle'
    NETWORK = 'network','Network'
    DOTSANDLINES = 'dots_and_lines','Dots And Lines'
    CHANGER_JAM = 'changer_jam','Changer Jam'
    PROTON_VS_ELECTRON = 'proton_vs_electron','Proton Vs Electron'
    COLOR_BOUNCER = 'color_bouncer','Color Bouncer'
    TETRA_BLOCK_PUZZLE = 'tetra_block_puzzle','Tetra Block Puzzle'
    GARBAGE = 'garbage','Garbage'
    COLOR_LINES = 'color_lines','Color Lines'
    CATCH_NUMBERS = 'catch_numbers','Catch the numbers'
    DRAW_THE_PATH = 'draw_the_path','Draw The Path'
    TIGHTNESS = 'tightness','Tightness'
    MIRRORS = 'mirrors','Mirrors'
    COLOR_BLOCKS = 'color_blocks','Color Blocks'
    WORLD_CARGO = 'world_cargo','World Cargo'
    BOOKS_TOWER = 'books_tower','Books Tower'
    BRIGHT_BALL = 'bright_ball','Bright Ball'
    DOTS_ATTACK = 'dots_attack','Dots Attack'
    FLAYING_TRIANGLE = 'flaying_triangle','Flaying Triangle'
    POCKET_JUMP = 'pocket_jump','Pocket Jump'
    GO_TO_DOT = 'go_to_dot','Go To Dot'
    JUMP_BOX_HERO = 'jump_box_hero','Jump Box Hero'
    JUMP_RED_SQUARE = 'jump_red_square','Jump Red Square'
    RACING_GAME_CHALLENGE = 'racing_game_challenge','Racing Game Challenge'
    FALLING_DOTS = 'falling_dots','Falling Dots'
    AMAZING_CUBE = 'amazing_cube','Amazing Cube'
    RETRO_SPEED2 = 'retro_speed2','Retro Speed2'
    COLOR_TOWER = 'color_tower','Color Tower'
    COLOR_CIRCLE = 'color_circle','Color Circle'
    CIRCLE_FLIP = 'circle_flip','Circle Flip'
    KNIVES = 'knives','Knives'
    SHTO_PONG = 'shot_pong','Shot Pong'
    SNAKE_AND_CIRCLE = 'snake_and_circle','Snake and Circle'


class NotificationAction(LabelChoices):
    IMAGE = 'image', 'Image'
    VIDEO = 'video', 'Video'
    TEXT = 'text', 'Text'


class NotificationTemplate(LabelChoices):
    INSTANT = 'instant', 'Instant One Time'
    EVENT = 'event', 'Event'

    SEND_COINS = 'send_coins', 'Send Coins'

    DAILY = 'daily', 'Daily'
    EVERY_14_DAYS = 'every_14_days', 'Every 14 Days'
    ONCE_A_MONTH = 'once_a_month', 'Once A Month'

    HOME = 'home', 'When User Reach Home Dashboard'
    LOGIN = 'login', 'After User Login'

    HOW_TO_USE = 'how_to_use', 'How To Use Engage'
    LEVEL_UP_5 = 'level_up_5', 'Level Up 5'  # TODO
    LEVEL_UP_10 = 'level_up_10', 'Level Up 10'  # TODO

    DAY1_JOINING = 'day_1_joining', 'Day 1 of Joining'
    DAY2_JOINING = 'day_2_joining', 'Day 2 of Joining'

    BEFORE_MATCH_INFORMATIVE = 'before_match_informative', 'Before Match Informative'
    WIN_MATCH_INFORMATIVE = 'win_match_informative', 'Win Match Informative'

    ACTIVE_5_DAYS = 'active_5_days', '5 Active Days After Joining'
    ACTIVE_10_DAYS = 'active_10_days', '10 Active Days After Joining'
    ACTIVE_30_DAYS = 'active_30_days', '30 Active Days After Joining'

    DORMANT_3_DAYS = 'dormant_3_days', 'Dormant 3 Days'
    DORMANT_5_DAYS = 'dormant_5_days', 'Dormant 5 Days'

    USER_REGISTER_FOR_TOURNAMENT = 'user_register_for_tournament', 'User Registers For A Tournament'
    USER_FIRST_TOURNAMENT = 'user_first_tournament', 'User Who Is First In Any Tournament'
    USER_SECOND_THIRD_TOURNAMENT = 'user_second_third_tournament', 'Users Who Win A Prize (2nd and more)'
    USER_OUTSIDE_THE_WINNING_POSITIONS = 'user_outside_the_winning_positions', 'User Outside The Winning Positions'

    HAPPY_BIRTHDAY = 'happy_birthday', 'Happy Birthday'

    FRIEND_ADDED = 'friend_added', 'Friend Added'
    FRIEND_REMOVE = 'friend_remove', 'Friend Remove'
    FRIEND_REQUEST = 'friend_request', 'Friend Request'

    VIDEO_ADDED = 'video_added', 'New Video Added'
    USER_WATCH_VIDEO = 'user_watch_video', 'If User Watches Any Video'

    MISSION_COMPLETED = 'mission_completed', 'Mission Completed'  # TODO
    COMPLETE_PROFILE = 'complete_profile', 'Complete Profile'
    ONWARDANDUPWARD = 'onward_upward', 'Onwards and Upwards'
    


UserProfileStates = [
    'Abia', 'Adamawa', 'Akwa_Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue',
    'Borno', 'Cross_River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu','FCT', 'Gombe',
    'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara',
    'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau',
    'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
]


class GameMode(LabelChoices):
    TOP_SCORER = 'top_scorer', 'Top Scorer'
    BATTLE_ROYALE = 'battle_royale', 'Battle Royale'
    TEAM_BASED = 'team_based', 'Team-Based'


class Platform(LabelChoices):
    PC = 'pc', 'PC'
    MOBILE = 'mobile', 'Mobile'


