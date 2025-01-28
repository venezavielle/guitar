from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # Initializes window
    stdkeys.create_window()

    # Define a set of valid keys
    keys = "q2we4r5ty7u8i9op-[=]"
    strings = set()

    n_iters = 0
    while True:
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            string_tracker = key
            # First condition which will only be true if key pressed returns a value
            if len(string_tracker) > 0:
                # Second condition to check if key pressed is valid
                if key in keys:
                    k = GuitarString(float(440.0 * (1.059463 ** (keys.index(key) - 12))))
                    k.pluck()
                    strings.add(k)
                    string_tracker = ""
        sample = 0
        expired_strings = set()

        for p in strings:
            sample += p.sample()
            p.tick()
            if p.time() > 44100*1.5:
                expired_strings.add(p)

        # Remove expired strings from the main set
        for e in expired_strings:
            strings.remove(e)

        play_sample(sample)