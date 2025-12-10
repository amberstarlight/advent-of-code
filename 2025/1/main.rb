# Day 1: Secret Entrance

def password(input, start_position)
  password = 0
  position = start_position
  File.open(File.join(File.dirname(__FILE__), input)) do |file|
    lines = file.readlines
    lines.each { |n|
      val = n.sub(/^L/, "-").sub(/^R/, "").to_i
      position = (position + val) % 100

      if position == 0
        password += 1
      end
    }
  end
  password
end

def method_0x434C49434B(input, start_position)
  password = 0
  position = start_position
  File.open(File.join(File.dirname(__FILE__), input)) do |file|
    lines = file.readlines
    lines.each { |n|
      val = n.sub(/^L/, "-").sub(/^R/, "").to_i
      range = val.abs

      range.times do |i|
        position = (
          if val < 0
            (position += 1) % 100
          else
            (position -= 1) % 100
          end
        )
        if position == 0
          password += 1
        end
      end
    }
  end
  password
end

puts password("input.txt", 50)
puts method_0x434C49434B("input.txt", 50)
