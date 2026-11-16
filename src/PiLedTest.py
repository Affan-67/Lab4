import time
from hal import hal_led as led
from hal import hal_input_switch as switch

LEFT = 1
RIGHT = 0

def main():
    led.init()
    switch.init()

    previous = LEFT
    start_time = 0

    try:
        while True:
            current = switch.read_slide_switch()

            if current == LEFT:
                # Left: blink at 5 Hz
                led.set_output(0, 1)
                time.sleep(0.1)
                led.set_output(0, 0)
                time.sleep(0.1)
            else:
                # Switch was just moved to the right: start the 5 second timer
                if previous == LEFT:
                    start_time = time.time()

                if time.time() - start_time < 5:
                    # Right: blink at 10 Hz for 5 seconds
                    led.set_output(0, 1)
                    time.sleep(0.05)
                    led.set_output(0, 0)
                    time.sleep(0.05)
                else:
                    # After 5 seconds: LED OFF
                    led.set_output(0, 0)
                    time.sleep(0.05)

            previous = current

    except KeyboardInterrupt:
        led.set_output(0, 0)

if __name__ == "__main__":
    main()