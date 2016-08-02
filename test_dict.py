#!/usr/bin/env python

net_device = {
    'key1': 'value1',
    'key2': 'value2',
}

print net_device['key1']
try:
    print net_device['model']
except KeyError:
    print "Handled Key Error"
except IndexError:
    print "Handled Index Error"
except Exception:
    print "Handled exception"
except (KeyError, IndexError):
    print "Handled either Key or Index error"

# Use KeyError instead of Exception to test specifically for missing Keys in Dict

print "hello world"

