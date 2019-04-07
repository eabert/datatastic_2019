from pprint import pprint
import statistics
import numpy as np

# GameID	Half	PlayerID	FrameID 	Time	GameClock	Speed	AccelImpulse	AccelLoad	AccelX	AccelY	AccelZ	Longitude	Latitude


def main():
    with open('datafest-osu-2019\\data\\gps.csv') as f:
        raw_gps = f.readlines()

    distance = np.zeros((21, 38))
    playtime = np.zeros((21, 38))
    for line in raw_gps[1:]:
        s = line.split(',')
        distance[int(s[2]) - 1][int(s[0]) - 1] += float(s[6]) * 0.1
        playtime[int(s[2]) - 1][int(s[0]) - 1] += 0.1

    np.savetxt('./distance', distance, delimiter=',')
    np.savetxt('./playtime.csv', playtime, delimiter=',')

if __name__ == '__main__':
    main()
