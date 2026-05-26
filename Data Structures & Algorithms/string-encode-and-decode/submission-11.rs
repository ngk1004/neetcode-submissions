impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut encoded = String::new();

        for s in strs {
            encoded.push_str(&s.len().to_string());
            encoded.push('#');
            encoded.push_str(&s);
        }

        encoded
    }

    pub fn decode(s: String) -> Vec<String> {
        let chars: Vec<char> = s.chars().collect();
        let mut res = Vec::new();
        let mut i = 0;

        while i < chars.len() {
            let mut j = i;

            // Find the delimiter '#'
            while chars[j] != '#' {
                j += 1;
            }

            // Parse the length
            let length: usize = chars[i..j].iter().collect::<String>().parse().unwrap();

            // Extract the string using the length
            let start = j + 1;
            let end = start + length;
            res.push(chars[start..end].iter().collect());

            i = end;
        }

        res
    }
}