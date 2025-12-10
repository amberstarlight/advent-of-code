# frozen_string_literal: true

# Day 1: Secret Entrance

def password(input, start_position)
  password = 0
  position = start_position
  File.open(File.join(File.dirname(__FILE__), input)) do |file|
    lines = file.readlines
    lines.each do |n|
      val = n.sub(/^L/, '-').sub(/^R/, '').to_i
      position = (position + val) % 100
      password += 1 if position.zero?
    end
  end
  password
end

def method_b(input, start_position)
  password = 0
  position = start_position
  File.open(File.join(File.dirname(__FILE__), input)) do |file|
    lines = file.readlines
    lines.each do |n|
      val = n.sub(/^L/, '-').sub(/^R/, '').to_i
      range = val.abs

      range.times do |_i|
        position = (
          if val.negative?
            (position += 1) % 100
          else
            (position -= 1) % 100
          end
        )
        password += 1 if position.zero?
      end
    end
  end
  password
end

puts password('input.txt', 50)
puts method_b('input.txt', 50)
