o = out/lixo.$1
f = $1/.f
d = $(call f,$(@D))

EXTS := pdf png svg
OUTS := $(foreach e,$(EXTS),$(call o,$e))
SVG := $(filter %.svg,$(OUTS))

.PHONY: all clean
all: $(OUTS)

.SECONDEXPANSION:

$(call o,%): $(SVG) $$d ; @cairosvg -f $* -d 300 -o $@ $<
$(SVG): lixo.py $$d ; @python3 $< 20cm > $@

clean: ; @rm -f $(OUTS)

$(call f,%):
	@mkdir -p $(@D)
	@touch $@
