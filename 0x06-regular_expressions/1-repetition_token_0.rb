#!/usr/bin/env ruby

if ARGV.empty?
  exit (1)
end

input_str = ARGV[0]
pattern = /hbt{2,5}n/
matches = input_str.scan(pattern)
puts matches.join
