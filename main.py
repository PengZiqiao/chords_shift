from itertools import cycle, islice

notes = []
for x in 'CDEFGAB':
    notes.append(x)
    if not x in 'EB':
        notes.append(f'{x}#')

notes_cycle = cycle(notes)


def gen_map(i):
    target = islice(notes_cycle, i, 12 + i)
    return dict(zip(notes, target))


def get_chords():
    chords = input('请输入谱，和弦之间用空格分隔\n').split()
    res = []
    for chord in chords:
        if '#' in chord:
            res.append((chord[:2], chord[2:]))
        else:
            res.append((chord[:1], chord[1:]))
    return res


def get_shift():
    orient, step = input('请输入变调参数，如“# 1”或“b 2”\n').split()
    return 12 - int(step) if orient == 'b' else int(step)


def cal_result(chords, shift):
    chords_map = gen_map(shift)
    targets = [f'{chords_map[x[0]]}{x[1]}' for x in chords]
    return ' '.join(targets)



if __name__ == '__main__':
    chords = get_chords()
    shift = get_shift()
    print(cal_result(chords, shift))
