#!/usr/bin/env python
# -*- coding: utf-8 -*-

import af

from optparse import OptionParser

Parser = OptionParser(
    usage="%prog render1 render2 ... command\ntype \"%prog -h\" for "
    "help", version="%prog 1.  0"
)
Parser.add_option('-n', '--jobname', dest='jobname', type='string',       default=None,      help='Job name')
Parser.add_option('-s', '--service', dest='service', type='string',       default='generic', help='Service type')
Parser.add_option('-p', '--parser',  dest='parser',  type='string',       default='generic', help='Parser type')
Parser.add_option('-V', '--verbose', dest='verbose', action='store_true', default=False,     help='Verbose mode')
Parser.add_option('-D', '--debug',   dest='debug',   action='store_true', default=False,     help='Debug mode (verbose mode, no commands execution)')
(Options, Args) = Parser.parse_args()

if len(Args) < 2:
	Parser.error('Not enough arguments provided.')

if Options.debug: Options.verbose = True

Renders = Args[:-1]
Command = Args[-1]
JobName = Options.jobname
if JobName is None:
    JobName = Command.split(' ')[0]

if Options.verbose:
    print('JobName: %s' % JobName)
    print('Renders: %s' % (','.join(Renders)))
    print('Command: %s' % Command)

job = af.Job( JobName)
job.setMaintenance()

block = af.Block('Maintenance', Options.service)
block.setParser( Options.parser)
block.setCommand( Command)

for render in Renders:
    task = af.Task( render)
    block.tasks.append( task)

job.blocks.append( block)

if Options.verbose:
    job.output()

if not Options.debug:
    job.send()

