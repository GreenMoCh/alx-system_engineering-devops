#!/usr/bin/env ruby

if ARGV.empty?
  exit (1)
end

input_str = ARGV[0]
pattern = /hb?tn/
matches = input_str.scan(pattern)
puts matches.join
