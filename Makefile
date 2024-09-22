OUT := out
NAME := lixo

SVG := $(OUT)/$(NAME).svg
PDF := $(OUT)/$(NAME).pdf

f = $1/.f
d = $(call f,$(@D))

.PHONY: all clean
all: $(PDF) $(SVG)

.SECONDEXPANSION:

$(PDF): $(SVG) $$d  ; @cairosvg -o $@ $<
$(SVG): lixo.py $$d ; @python3 $< > $@

clean: ; @rm -f $(SVG) $(PDF)

$(call f,%):
	@mkdir -p $(@D)
	@touch $@
