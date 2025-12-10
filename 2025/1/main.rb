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

puts password("input.txt", 50)
