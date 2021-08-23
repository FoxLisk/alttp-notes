from ruamel.yaml import YAML

def parse_time(time):
    seconds, frames = time.split("'")
    return int(seconds), int(frames)

def sum_route(screens):
    seconds, frames = 0, 0
    for room, time in screens.items():
        screen_seconds, screen_frames = parse_time(time)
        seconds += screen_seconds
        frames += screen_frames
        # print(f"{room}:   {screen_seconds}'{screen_frames}")

    seconds += frames // 60
    frames = frames % 60

    return seconds, frames

if __name__ == '__main__':
    with open('abnoeg_ir_hookpush.yaml') as f:
        yaml = YAML(typ="safe")
        routes = yaml.load(f)
        for route, screens in routes.items():
            seconds, frames = sum_route(screens)
            print(f"{route}: {seconds}'{frames:02}")
