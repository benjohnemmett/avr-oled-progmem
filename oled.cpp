#define F_CPU 8000000UL

#include <avr/io.h>
#include <util/delay.h>
#include "SSD1306-AVR/Framebuffer.h"

uint8_t _x1 = 6;
uint8_t _y1 = 6;

int main(void) {
  Framebuffer fb;

  fb.drawRectangle(2,2,125,61);
  
  DDRB |= (1 << PB5);

  while (1) {
    PORTB |= (1 << PB5);
    _delay_ms(200);
    PORTB &= ~(1 << PB5);
    _delay_ms(200);

    _x1 += 2;
    _y1 += 1;

    fb.drawRectangle(_x1, _y1, _x1+6, _y1+6, 1);
    fb.show();
    fb.invert(_y1 % 2);
  }

  return 0;
}