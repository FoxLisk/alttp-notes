from pathlib import Path
import yaml

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

def run_comparison(comparison_path):
    with open(comparison_path) as fp:
        comparison = yaml.safe_load(fp)
    print(f"{comparison['title']}")
    times = []
    for route, screens in comparison['routes'].items():
        seconds, frames = sum_route(screens)
        times.append((route, seconds, frames))
    for route, seconds, frames in sorted(times, key=lambda t: t[1:]):
        print(f"    {route}: {seconds}'{frames:02}")

def _looks_like_yaml(filename):
    return not filename.startswith('.') and filename.endswith('.yaml')

def main():
    dot = Path('.')
    for f in dot.iterdir():
        if _looks_like_yaml(f.name):
            run_comparison(f)
            print("")

if __name__ == '__main__':
    main()
