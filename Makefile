prefix=/usr

all:

clean:
	find . -name *.pyc | xargs rm -f

install:
	install -d -m 0755 "$(DESTDIR)/$(prefix)/sbin"
	install -m 0755 conduit-daemon "$(DESTDIR)/$(prefix)/sbin"
	# install -d -m 0755 "$(DESTDIR)/$(prefix)/bin"
	# install -m 0755 conduit "$(DESTDIR)/$(prefix)/bin"

	install -d -m 0755 "$(DESTDIR)/$(prefix)/lib64/conduit-daemon"
	cp -r lib/* "$(DESTDIR)/$(prefix)/lib64/conduit-daemon"
	find "$(DESTDIR)/$(prefix)/lib64/conduit-daemon" -type f | xargs chmod 644
	find "$(DESTDIR)/$(prefix)/lib64/conduit-daemon" -type d | xargs chmod 755

	install -d -m 0755 "$(DESTDIR)/$(prefix)/lib/systemd/system"
	install -m 0644 systemd/conduit-daemon.service "$(DESTDIR)/$(prefix)/lib/systemd/system"

uninstall:
	rm -f "$(DESTDIR)/$(prefix)/sbin/conduit-daemon"
	rm -Rf "$(DESTDIR)/$(prefix)/lib64/conduit-daemon"
	rm -f "$(DESTDIR)/$(prefix)/lib/systemd/system/conduit-daemon.service"

.PHONY: all clean install uninstall
