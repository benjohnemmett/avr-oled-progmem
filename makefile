
F_CPU=8000000
CC=avr-g++

OBJS = SSD1306-AVR/I2C.o SSD1306-AVR/SSD1306.o SSD1306-AVR/Framebuffer.o 

.PHONY: all
all: oled.hex

flash:
	avrdude -p m328p -c usbasp -U flash:w:oled.hex:i

oled.hex: oled.cpp $(OBJS)
	$(CC) -Os -mmcu=atmega328p -c oled.cpp -o oled.o
	$(CC) -mmcu=atmega328p $(OBJS) oled.o -o oled.elf
	avr-objcopy -j .text  -j .data  -O ihex oled.elf oled.hex

SSD1306-AVR/%.o: SSD1306-AVR/%.cpp
	$(CC) -mmcu=atmega328p -c $< -o $@ -DF_CPU=$(F_CPU)

.PHONY: clean
clean:
	rm -f *.elf *.o *.obj  *.hex
	rm -f ./SSD1306-AVR/*.o
