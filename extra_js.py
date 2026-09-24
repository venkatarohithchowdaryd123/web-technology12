"""Additional JavaScript programs (imported by generate.py)."""
import json
from extra_css import svg

js_extra = []

def add(slug, title, desc, body, js=""):
    js_extra.append(dict(slug=slug, title=title, desc=desc, body=body, js=js))

def tool(slug, title, desc, fields, code, button="Run"):
    """Build a small form-based program. `fields` = [(id, label, type, default)];
    type is number | text | list (numbers) | wlist (words). `code` is a JS function body that
    can use each id as a variable and must return the text to display."""
    inputs, decls = [], []
    for fid, label, typ, default in fields:
        itype = "number" if typ == "number" else "text"
        inputs.append(f'  <label>{label}<input id="{fid}" type="{itype}" value="{default}"></label>')
        el = f"document.getElementById('{fid}').value"
        if typ == "number":
            decls.append(f"  const {fid} = Number({el});")
        elif typ == "list":
            decls.append(f"  const {fid} = {el}.split(',').map(x => x.trim()).filter(x => x !== '').map(Number);")
        elif typ == "wlist":
            decls.append(f"  const {fid} = {el}.split(',').map(x => x.trim()).filter(x => x !== '');")
        else:
            decls.append(f"  const {fid} = {el};")
    body = ('<form class="demo-form" onsubmit="run(); return false;">\n' + "\n".join(inputs) +
            f'\n  <button class="btn" type="submit">{button}</button>\n</form>\n<div class="output-box" id="out"></div>')
    js = ("// Reads the inputs, runs the program logic and prints the result.\nfunction run() {\n" + "\n".join(decls) +
          "\n  const result = (() => {\n" + code + "\n  })();\n  document.getElementById('out').textContent = result;\n}\nrun();")
    add(slug, title, desc, body, js)

# ---------------- Number programs ----------------
tool("even-odd", "Check Even or Odd", "Uses the % operator to decide whether a number is even or odd.",
     [("n", "Number", "number", 7)], "    return n + (n % 2 === 0 ? ' is an EVEN number.' : ' is an ODD number.');", "Check")
tool("positive-negative-zero", "Positive, Negative or Zero", "Checks the sign of a number with if / else if / else.",
     [("n", "Number", "number", -5)],
     "    if (n > 0) return n + ' is POSITIVE.';\n    if (n < 0) return n + ' is NEGATIVE.';\n    return 'The number is ZERO.';", "Check")
tool("reverse-number", "Reverse a Number", "Reverses digits using a while loop with % and Math.floor.",
     [("n", "Number", "number", 12345)],
     "    let num = Math.abs(n), rev = 0;\n    while (num > 0) { rev = rev * 10 + (num % 10); num = Math.floor(num / 10); }\n    return 'Reverse of ' + n + ' is ' + (n < 0 ? -rev : rev);", "Reverse")
tool("sum-of-digits", "Sum of Digits", "Adds every digit of a number.",
     [("n", "Number", "number", 4829)],
     "    let num = Math.abs(n), sum = 0;\n    while (num > 0) { sum += num % 10; num = Math.floor(num / 10); }\n    return 'Sum of digits of ' + n + ' = ' + sum;", "Calculate")
tool("swap-two-numbers", "Swap Two Numbers", "Swaps values using destructuring and using a temporary variable.",
     [("a", "A", "number", 10), ("b", "B", "number", 25)],
     "    let x = a, y = b;\n    [x, y] = [y, x];                       // destructuring swap\n    let m = a, n = b, temp = m;            // temporary-variable swap\n    m = n; n = temp;\n    return 'Before: a=' + a + ', b=' + b + '\\nAfter (destructuring): a=' + x + ', b=' + y + '\\nAfter (temp variable): a=' + m + ', b=' + n;", "Swap")
tool("gcd", "Greatest Common Divisor (GCD)", "Euclid's algorithm.",
     [("a", "Number A", "number", 48), ("b", "Number B", "number", 18)],
     "    let x = Math.abs(a), y = Math.abs(b);\n    while (y !== 0) { [x, y] = [y, x % y]; }\n    return 'GCD of ' + a + ' and ' + b + ' = ' + x;", "Find GCD")
tool("lcm", "Least Common Multiple (LCM)", "LCM = (a x b) / GCD(a, b).",
     [("a", "Number A", "number", 12), ("b", "Number B", "number", 18)],
     "    const gcd = (x, y) => y === 0 ? x : gcd(y, x % y);\n    const g = gcd(Math.abs(a), Math.abs(b));\n    return 'LCM of ' + a + ' and ' + b + ' = ' + (Math.abs(a * b) / g);", "Find LCM")
tool("armstrong-number", "Armstrong Number", "A number equal to the sum of its digits each raised to the number of digits.",
     [("n", "Number", "number", 153)],
     "    const digits = String(Math.abs(n)).split('');\n    const sum = digits.reduce((s, d) => s + Math.pow(Number(d), digits.length), 0);\n    return n + (sum === n ? ' is' : ' is NOT') + ' an Armstrong number (digit-power sum = ' + sum + ').';", "Check")
tool("perfect-number", "Perfect Number", "A number equal to the sum of its proper divisors.",
     [("n", "Number", "number", 28)],
     "    let sum = 0, divisors = [];\n    for (let i = 1; i <= n / 2; i++) if (n % i === 0) { sum += i; divisors.push(i); }\n    return 'Proper divisors: ' + divisors.join(', ') + '\\nSum = ' + sum + '\\n' + n + (sum === n && n > 0 ? ' is' : ' is NOT') + ' a perfect number.';", "Check")
tool("multiplication-table", "Multiplication Table", "Prints the table of a number up to a chosen limit.",
     [("n", "Number", "number", 7), ("limit", "Up to", "number", 10)],
     "    let lines = [];\n    for (let i = 1; i <= limit; i++) lines.push(n + ' x ' + i + ' = ' + (n * i));\n    return lines.join('\\n');", "Show table")
tool("power-of-number", "Power of a Number", "Calculates base raised to an exponent using a loop and Math.pow.",
     [("base", "Base", "number", 2), ("exp", "Exponent (whole number)", "number", 10)],
     "    let result = 1;\n    for (let i = 0; i < Math.abs(exp); i++) result *= base;\n    if (exp < 0) result = 1 / result;\n    return 'Loop result: ' + base + '^' + exp + ' = ' + result + '\\nMath.pow result: ' + Math.pow(base, exp);", "Calculate")
tool("count-digits", "Count Digits in a Number", "Counts how many digits a number has.",
     [("n", "Number", "number", 987654)],
     "    let num = Math.abs(Math.trunc(n)), count = 0;\n    do { count++; num = Math.floor(num / 10); } while (num > 0);\n    return n + ' has ' + count + ' digit(s).';", "Count")

# ---------------- Arrays ----------------
tool("sort-array", "Sort an Array", "Sorts numbers ascending and descending with sort().",
     [("arr", "Numbers (comma separated)", "list", "45, 3, 99, 12, 7, 60")],
     "    const asc = [...arr].sort((a, b) => a - b);\n    const desc = [...arr].sort((a, b) => b - a);\n    return 'Original:   ' + arr.join(', ') + '\\nAscending:  ' + asc.join(', ') + '\\nDescending: ' + desc.join(', ');", "Sort")
tool("second-largest", "Second-Largest Element", "Finds the second-largest distinct number in an array.",
     [("arr", "Numbers (comma separated)", "list", "12, 35, 1, 10, 34, 35")],
     "    const unique = [...new Set(arr)].sort((a, b) => b - a);\n    return unique.length < 2 ? 'Need at least two distinct numbers.' : 'Largest = ' + unique[0] + '\\nSecond largest = ' + unique[1];", "Find")
tool("remove-duplicates", "Remove Duplicate Elements", "Uses a Set to remove repeated values.",
     [("arr", "Items (comma separated)", "wlist", "apple, banana, apple, cherry, banana, mango")],
     "    const unique = [...new Set(arr)];\n    return 'Original: ' + arr.join(', ') + '\\nUnique:   ' + unique.join(', ') + '\\nRemoved ' + (arr.length - unique.length) + ' duplicate(s).';", "Remove")
tool("merge-arrays", "Merge Two Arrays", "Combines arrays using concat() and the spread operator.",
     [("a", "Array 1", "wlist", "1, 2, 3"), ("b", "Array 2", "wlist", "4, 5, 6")],
     "    return 'concat(): ' + a.concat(b).join(', ') + '\\nspread:   ' + [...a, ...b].join(', ');", "Merge")
tool("array-element-frequency", "Frequency of Each Array Element", "Counts how many times every element appears.",
     [("arr", "Items (comma separated)", "wlist", "a, b, a, c, b, a, d")],
     "    const freq = {};\n    arr.forEach(x => freq[x] = (freq[x] || 0) + 1);\n    return Object.entries(freq).map(([k, v]) => k + ' -> ' + v).join('\\n');", "Count")
tool("common-elements", "Common Elements in Two Arrays", "Finds the intersection using filter() and includes().",
     [("a", "Array 1", "wlist", "1, 2, 3, 4, 5"), ("b", "Array 2", "wlist", "4, 5, 6, 7, 2")],
     "    const common = [...new Set(a.filter(x => b.includes(x)))];\n    return common.length ? 'Common: ' + common.join(', ') : 'No common elements.';", "Find")

# ---------------- Strings ----------------
tool("reverse-string", "Reverse a String", "split(), reverse() and join().",
     [("s", "Text", "text", "JavaScript")], "    return 'Reversed: ' + s.split('').reverse().join('');", "Reverse")
tool("string-palindrome", "Palindrome String Check", "Ignores case, spaces and punctuation.",
     [("s", "Text", "text", "A man, a plan, a canal: Panama")],
     "    const clean = s.toLowerCase().replace(/[^a-z0-9]/g, '');\n    const isPal = clean === clean.split('').reverse().join('');\n    return '\"' + s + '\" ' + (isPal ? 'IS' : 'is NOT') + ' a palindrome.';", "Check")
tool("vowels-consonants", "Count Vowels and Consonants", "Counts letters in a string.",
     [("s", "Text", "text", "Hello World from JavaScript")],
     "    let v = 0, c = 0;\n    for (const ch of s.toLowerCase()) {\n      if ('aeiou'.includes(ch)) v++;\n      else if (ch >= 'a' && ch <= 'z') c++;\n    }\n    return 'Vowels: ' + v + '\\nConsonants: ' + c;", "Count")
tool("word-count", "Count Words in a String", "Splits on whitespace to count words.",
     [("s", "Text", "text", "The quick brown fox jumps over the lazy dog")],
     "    const words = s.trim().split(/\\s+/).filter(w => w.length);\n    return 'Words: ' + words.length + '\\nCharacters (with spaces): ' + s.length;", "Count")
tool("character-frequency", "Frequency of Characters in a String", "Counts every character (case-insensitive, spaces ignored).",
     [("s", "Text", "text", "programming")],
     "    const freq = {};\n    for (const ch of s.toLowerCase().replace(/\\s/g, '')) freq[ch] = (freq[ch] || 0) + 1;\n    return Object.entries(freq).map(([k, v]) => k + ': ' + v).join('\\n');", "Count")

add("regex-demo", "Regular Expressions Demo",
    "test(), match(), replace() and split() with several patterns.",
    '''<form class="demo-form" onsubmit="run(); return false;"><label>Text<input id="txt" value="Call 98765 43210 or email me@site.com on 2026-09-20"></label><button class="btn" type="submit">Run patterns</button></form><div class="output-box" id="out"></div>''',
    r"""
function run() {
  const t = document.getElementById('txt').value;
  const digits = t.match(/\d+/g);                       // all numbers
  const email  = t.match(/[\w.]+@[\w.]+\.\w+/);         // email
  const date   = /\d{4}-\d{2}-\d{2}/.test(t);           // ISO date present?
  const masked = t.replace(/\d/g, '#');                 // replace digits
  const words  = t.split(/\s+/);                        // split on spaces
  document.getElementById('out').textContent =
    'Numbers found: ' + (digits ? digits.join(', ') : 'none') +
    '\nEmail found: ' + (email ? email[0] : 'none') +
    '\nContains a date (YYYY-MM-DD): ' + date +
    '\nDigits masked: ' + masked +
    '\nWord count: ' + words.length;
}
run();""")

# ---------------- Language features ----------------
add("functions-demo", "JavaScript Functions",
    "Declaration, expression, default parameters, return values and recursion.",
    '<button class="btn" onclick="run()">Run</button><div class="output-box" id="out"></div>',
    r"""
function greet(name = 'Student') { return 'Hello, ' + name + '!'; }           // declaration + default parameter
const square = function (n) { return n * n; };                                // function expression
function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }             // variable arguments
function factorial(n) { return n <= 1 ? 1 : n * factorial(n - 1); }           // recursion
function counter() { let c = 0; return () => ++c; }                            // closure
function run() {
  const next = counter();
  document.getElementById('out').textContent =
    greet() + '\n' + greet('Asha') + '\nsquare(9) = ' + square(9) +
    '\nsum(1,2,3,4) = ' + sum(1, 2, 3, 4) + '\nfactorial(5) = ' + factorial(5) +
    '\nclosure counter: ' + next() + ', ' + next() + ', ' + next();
}
run();""")

add("arrow-functions", "Arrow Functions",
    "Short function syntax with implicit return, plus map / filter / reduce.",
    '<button class="btn" onclick="run()">Run</button><div class="output-box" id="out"></div>',
    r"""
const add = (a, b) => a + b;             // implicit return
const double = n => n * 2;               // single parameter
const info = (name, age) => {            // block body
  const group = age >= 18 ? 'adult' : 'minor';
  return `${name} is an ${group}`;
};
function run() {
  const nums = [1, 2, 3, 4, 5, 6];
  document.getElementById('out').textContent =
    'add(3, 4) = ' + add(3, 4) + '\ndouble(8) = ' + double(8) + '\n' + info('Ravi', 20) +
    '\nmap x2: ' + nums.map(double).join(', ') + '\nfilter even: ' + nums.filter(n => n % 2 === 0).join(', ') +
    '\nreduce sum: ' + nums.reduce((a, b) => a + b, 0);
}
run();""")

add("arrays-methods", "Arrays and Array Methods",
    "Add, remove, search and transform items in an array.",
    '<div class="output-box" id="out"></div><button class="btn" onclick="run()">Run again</button>',
    r"""
function run() {
  const log = [];
  const fruits = ['apple', 'banana'];
  fruits.push('cherry');           log.push('push -> ' + fruits);
  fruits.unshift('mango');         log.push('unshift -> ' + fruits);
  fruits.pop();                    log.push('pop -> ' + fruits);
  fruits.shift();                  log.push('shift -> ' + fruits);
  fruits.splice(1, 0, 'kiwi');     log.push('splice(1,0,"kiwi") -> ' + fruits);
  log.push('slice(0,2) -> ' + fruits.slice(0, 2));
  log.push('indexOf("kiwi") -> ' + fruits.indexOf('kiwi'));
  log.push('includes("apple") -> ' + fruits.includes('apple'));
  log.push('join(" | ") -> ' + fruits.join(' | '));
  log.push('reverse -> ' + [...fruits].reverse());
  log.push('map(upper) -> ' + fruits.map(f => f.toUpperCase()));
  log.push('find(len>4) -> ' + fruits.find(f => f.length > 4));
  document.getElementById('out').textContent = log.join('\n');
}
run();""")

add("objects-demo", "Objects in JavaScript",
    "Create an object, read and change properties, add methods and loop over keys.",
    '<button class="btn" onclick="run()">Run</button><div class="output-box" id="out"></div>',
    r"""
const student = {
  name: 'Meena', age: 20, course: 'BCA',
  marks: { html: 88, css: 82, js: 91 },
  average() { const m = Object.values(this.marks); return (m.reduce((a, b) => a + b) / m.length).toFixed(1); }
};
function run() {
  student.city = 'Chennai';           // add property
  student.age = 21;                   // update property
  delete student.course;              // delete property
  const keys = Object.keys(student).join(', ');
  document.getElementById('out').textContent =
    'Name: ' + student.name + ', Age: ' + student.age + '\nKeys: ' + keys +
    '\nAverage marks: ' + student.average() + '\nJSON: ' + JSON.stringify(student);
}
run();""")

add("date-object", "Date Object", "Shows the current date, time and date parts using the Date object.",
    '<button class="btn" onclick="run()">Refresh</button><div class="output-box" id="out"></div>',
    r"""
function run() {
  const d = new Date();
  const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  const future = new Date(d.getTime() + 30 * 24 * 60 * 60 * 1000);
  document.getElementById('out').textContent =
    'Date: ' + d.getDate() + '/' + (d.getMonth() + 1) + '/' + d.getFullYear() + ' (' + days[d.getDay()] + ')' +
    '\nTime: ' + d.toLocaleTimeString() + '\nISO: ' + d.toISOString() +
    '\nTimestamp (ms): ' + d.getTime() + '\nDate after 30 days: ' + future.toDateString() +
    '\nNew Year 2027 is in ' + Math.ceil((new Date(2027, 0, 1) - d) / 86400000) + ' day(s)';
}
run();""")

add("math-object", "Math Object", "Uses common Math methods and constants.",
    '<form class="demo-form" onsubmit="run(); return false;"><label>Number<input id="n" type="number" value="16.7"></label><button class="btn" type="submit">Calculate</button></form><div class="output-box" id="out"></div>',
    r"""
function run() {
  const n = Number(document.getElementById('n').value);
  document.getElementById('out').textContent =
    'Math.PI = ' + Math.PI.toFixed(5) + '\nMath.round(' + n + ') = ' + Math.round(n) + '\nMath.floor = ' + Math.floor(n) + '   Math.ceil = ' + Math.ceil(n) +
    '\nMath.sqrt = ' + Math.sqrt(n).toFixed(3) + '\nMath.pow(' + n + ', 2) = ' + Math.pow(n, 2).toFixed(2) + '\nMath.abs(-' + n + ') = ' + Math.abs(-n) +
    '\nMath.max(3, 9, ' + n + ') = ' + Math.max(3, 9, n) + '   Math.min = ' + Math.min(3, 9, n) +
    '\nRandom 1-100: ' + (Math.floor(Math.random() * 100) + 1);
}
run();""")

add("spread-rest-operators", "Spread and Rest Operators",
    "Spread expands values; rest gathers them.",
    '<button class="btn" onclick="run()">Run</button><div class="output-box" id="out"></div>',
    r"""
function total(first, ...others) { return first + others.reduce((a, b) => a + b, 0); }   // rest parameters
function run() {
  const a = [1, 2, 3], b = [4, 5];
  const merged = [...a, ...b];                      // spread in arrays
  const p = { name: 'Ali', age: 22 };
  const q = { ...p, city: 'Madurai', age: 23 };     // spread in objects
  const [head, ...tail] = merged;                   // rest in destructuring
  document.getElementById('out').textContent =
    'merged = [' + merged + ']\nobject copy = ' + JSON.stringify(q) +
    '\nMath.max(...merged) = ' + Math.max(...merged) + '\nhead = ' + head + ', tail = [' + tail + ']' +
    '\ntotal(1,2,3,4) = ' + total(1, 2, 3, 4);
}
run();""")

# ---------------- DOM / events ----------------
add("button-click-event", "Button Click Event", "Handles click, double-click and mouseover events.",
    '''<button class="btn" id="b1" onclick="clicked()">Click me</button>
<button class="btn" id="b2">Double-click me</button>
<button class="btn" id="b3">Hover over me</button>
<div class="output-box" id="out">Waiting for an event...</div>''',
    r"""
let clicks = 0;
const out = document.getElementById('out');
function clicked() { clicks++; out.textContent = 'onclick: button clicked ' + clicks + ' time(s).'; }        // inline handler
document.getElementById('b2').addEventListener('dblclick', () => out.textContent = 'dblclick event fired!');   // addEventListener
document.getElementById('b3').addEventListener('mouseover', () => out.textContent = 'mouseover event fired!');""")

_imgs = [svg("#e74c3c", "#f39c12", "Image 1", 400, 220), svg("#16a085", "#3498db", "Image 2", 400, 220), svg("#8e44ad", "#e84393", "Image 3", 400, 220)]
add("change-image-on-click", "Change Image on Button Click", "Cycles through images by changing the src attribute.",
    '<img id="pic" alt="demo" style="max-width:100%;border-radius:10px;display:block;margin-bottom:12px"><button class="btn" onclick="next()">Next Image</button> <button class="btn" onclick="pick(0)">Image 1</button>',
    "const images = " + json.dumps(_imgs) + ";\nlet index = 0;\nconst pic = document.getElementById('pic');\n"
    "function show() { pic.src = images[index]; }\nfunction next() { index = (index + 1) % images.length; show(); }\nfunction pick(i) { index = i; show(); }\nshow();")

add("display-api-data", "Display API Data Dynamically",
    "Fetches users from a public API and builds cards in the DOM (falls back to sample data when offline).",
    '<button class="btn" onclick="load()">Load Users</button><div id="list" class="ulist"></div><div class="output-box" id="out">Click the button.</div>',
    r"""
const sample = [
  { name: 'Leanne Graham', email: 'leanne@example.com', company: { name: 'Romaguera-Crona' } },
  { name: 'Ervin Howell', email: 'ervin@example.com', company: { name: 'Deckow-Crist' } },
  { name: 'Clementine Bauch', email: 'clem@example.com', company: { name: 'Romaguera-Jacobson' } }
];
function render(users) {
  const list = document.getElementById('list');
  list.innerHTML = '';
  users.slice(0, 6).forEach(u => {
    const div = document.createElement('div');
    div.className = 'ucard';
    div.innerHTML = `<b>${u.name}</b><br>${u.email}<br><small>${u.company.name}</small>`;
    list.appendChild(div);
  });
}
async function load() {
  const out = document.getElementById('out');
  out.textContent = 'Loading...';
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!res.ok) throw new Error('HTTP ' + res.status);
    render(await res.json());
    out.textContent = 'Loaded from the live API.';
  } catch (err) {
    render(sample);
    out.textContent = 'API not reachable (' + err.message + '). Showing sample data instead.';
  }
}""")
js_extra[-1]["css"] = ".ulist{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin:14px 0}.ucard{background:#fff;padding:10px;border-radius:8px;border-left:5px solid #c0392b;color:#4a1010}"

add("login-form-validation", "Responsive Login Form with JavaScript Validation",
    "Validates email and password and shows friendly error messages.",
    '''<form class="demo-form lf" id="f" novalidate>
  <label>Email<input id="email" type="email" placeholder="you@example.com"></label><small class="err" id="e1"></small>
  <label>Password<input id="pw" type="password" placeholder="min 8 chars, letter + number"></label><small class="err" id="e2"></small>
  <label style="display:flex;gap:6px;align-items:center"><input type="checkbox" id="show" style="width:auto"> Show password</label>
  <button class="btn" type="submit">Login</button>
</form><div class="output-box" id="out"></div>''',
    r"""
const f = document.getElementById('f'), pw = document.getElementById('pw');
document.getElementById('show').addEventListener('change', e => pw.type = e.target.checked ? 'text' : 'password');
f.addEventListener('submit', e => {
  e.preventDefault();
  const email = document.getElementById('email').value.trim();
  let ok = true;
  const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  document.getElementById('e1').textContent = emailOk ? '' : 'Enter a valid email address.';
  const pwOk = pw.value.length >= 8 && /[A-Za-z]/.test(pw.value) && /\d/.test(pw.value);
  document.getElementById('e2').textContent = pwOk ? '' : 'Password needs 8+ characters with a letter and a number.';
  document.getElementById('out').textContent = emailOk && pwOk ? 'Login successful (demo). Welcome, ' + email + '!' : 'Please fix the errors above.';
});""")
js_extra[-1]["css"] = ".lf{max-width:380px}.err{color:#c0392b;display:block;min-height:1em}"

add("complete-interactive-webpage", "Complete Interactive Webpage (HTML + CSS + JS)",
    "A mini web page with a theme toggle, tabs, a live search filter, a like counter and a message form.",
    '''<div class="ia" id="page">
  <div class="bar"><b>My Interactive Page</b><button class="btn" id="theme">Toggle theme</button></div>
  <div class="tabs"><button class="tab active" data-t="t1">Courses</button><button class="tab" data-t="t2">Like</button><button class="tab" data-t="t3">Message</button></div>
  <section id="t1" class="pane show"><input id="q" placeholder="Search courses..."><ul id="courses"></ul></section>
  <section id="t2" class="pane"><p>Do you like this page?</p><button class="btn" id="like">&#128077; Like</button> <b id="lc">0</b> likes</section>
  <section id="t3" class="pane"><input id="nm" placeholder="Your name"><textarea id="ms" placeholder="Write a message..." rows="3"></textarea><button class="btn" id="send">Send</button><p id="res"></p></section>
</div>''',
    r"""
const courses = ['HTML Basics', 'CSS Layouts', 'JavaScript Fundamentals', 'DOM Manipulation', 'Responsive Design', 'Web Storage'];
const ul = document.getElementById('courses');
function showCourses(filter = '') {
  ul.innerHTML = '';
  courses.filter(c => c.toLowerCase().includes(filter.toLowerCase())).forEach(c => ul.innerHTML += '<li>' + c + '</li>');
  if (!ul.children.length) ul.innerHTML = '<li>No results</li>';
}
document.getElementById('q').addEventListener('input', e => showCourses(e.target.value));
showCourses();

document.querySelectorAll('.tab').forEach(tab => tab.addEventListener('click', () => {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.pane').forEach(p => p.classList.remove('show'));
  tab.classList.add('active');
  document.getElementById(tab.dataset.t).classList.add('show');
}));

let likes = Number(localStorage.getItem('likes') || 0);
const lc = document.getElementById('lc'); lc.textContent = likes;
document.getElementById('like').addEventListener('click', () => { likes++; lc.textContent = likes; localStorage.setItem('likes', likes); });

document.getElementById('theme').addEventListener('click', () => document.getElementById('page').classList.toggle('dark'));
document.getElementById('send').addEventListener('click', () => {
  const n = document.getElementById('nm').value.trim(), m = document.getElementById('ms').value.trim();
  document.getElementById('res').textContent = n && m ? 'Thanks ' + n + ', your message was received!' : 'Please fill in both fields.';
});""")
js_extra[-1]["css"] = """.ia{background:#fff;color:#4a1010;border-radius:12px;overflow:hidden;transition:.3s}.ia.dark{background:#1b2838;color:#eee}
.bar{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;background:#c0392b;color:#fff}.tabs{display:flex}
.tab{flex:1;padding:10px;border:0;background:#ffe3e3;cursor:pointer;font:inherit}.tab.active{background:#ff6b6b;color:#fff}
.pane{display:none;padding:16px}.pane.show{display:block}.pane input,.pane textarea{width:100%;padding:8px;margin-bottom:8px;border:1px solid #ffb3b3;border-radius:6px;font:inherit}"""

# =====================================================================
# Split pages: each assignment question now has its own program page.
# `js_overrides` narrows four existing combined pages to ONE question each
# (applied in generate.py); the matching second question is added below.
# =====================================================================
js_overrides = {
    "array-stats": dict(
        title="Largest and Smallest Element in an Array",
        desc="Finds the largest and smallest numbers in a comma-separated list.",
        js=r"""
function stats() {
  const nums = document.getElementById('arr').value.split(',').map(Number);
  document.getElementById('out').textContent =
    `Array: [${nums.join(', ')}]\nLargest: ${Math.max(...nums)}\nSmallest: ${Math.min(...nums)}`;
}
stats();"""),
    "change-text-bg-color": dict(
        title="Change Text Using JavaScript",
        desc="DOM manipulation: change the text of an element with textContent and innerHTML.",
        body='''<div class="demo-area" id="target">Click a button below to change me!</div>
<div style="margin-top:12px;">
  <button class="btn" onclick="document.getElementById('target').textContent='Text changed by JavaScript!'">Change Text</button>
  <button class="btn" onclick="document.getElementById('target').innerHTML='<b>Bold</b> and <i>italic</i> via innerHTML'">Change HTML</button>
  <button class="btn" onclick="document.getElementById('target').textContent='Click a button below to change me!'">Reset</button>
</div>'''),
    "classes-inheritance": dict(
        title="Classes and Objects",
        desc="Defines an ES6 class with a constructor, properties and methods, then creates objects from it.",
        js=r"""
class Student {
  constructor(name, course) { this.name = name; this.course = course; }
  introduce() { return `${this.name} studies ${this.course}.`; }
}
function run() {
  const s1 = new Student('Asha', 'BCA');
  const s2 = new Student('Ravi', 'B.Sc CS');
  document.getElementById('out').textContent =
    s1.introduce() + '\n' + s2.introduce() + '\ns1 instanceof Student: ' + (s1 instanceof Student);
}"""),
    "form-validation": dict(
        title="Form Validation",
        desc="Validates required fields, age range, matching passwords and a checkbox, with a message under each field.",
        body='''<form class="demo-form fv" id="fv" novalidate>
  <label>Full name *<input id="n"></label><small class="err" id="en"></small>
  <label>Age (18-60) *<input id="age" type="number"></label><small class="err" id="ea"></small>
  <label>Password *<input id="p1" type="password"></label><small class="err" id="e1"></small>
  <label>Confirm password *<input id="p2" type="password"></label><small class="err" id="e2"></small>
  <label style="display:flex;gap:6px;align-items:center"><input id="tc" type="checkbox" style="width:auto"> I accept the terms *</label><small class="err" id="et"></small>
  <button class="btn" type="submit">Register</button>
</form><div class="output-box" id="out"></div>''',
        css=".fv{max-width:400px}.err{display:block;color:#c0392b;min-height:1em}",
        js=r"""
document.getElementById('fv').addEventListener('submit', e => {
  e.preventDefault();
  const v = id => document.getElementById(id).value.trim();
  const set = (id, msg) => { document.getElementById(id).textContent = msg; return msg === ''; };
  const age = Number(v('age'));
  const ok = [
    set('en', v('n') ? '' : 'Name is required.'),
    set('ea', age >= 18 && age <= 60 ? '' : 'Age must be between 18 and 60.'),
    set('e1', v('p1').length >= 6 ? '' : 'Password needs at least 6 characters.'),
    set('e2', v('p2') === v('p1') && v('p2') ? '' : 'Passwords do not match.'),
    set('et', document.getElementById('tc').checked ? '' : 'You must accept the terms.')
  ].every(Boolean);
  document.getElementById('out').textContent = ok ? 'Form is valid. Registration successful (demo).' : 'Please correct the highlighted errors.';
});"""),
}

add("array-sum-average", "Sum and Average of Array Elements", "Calculates the sum and average using reduce().",
    '<form class="demo-form" onsubmit="run(); return false;"><label>Numbers (comma separated)<input id="arr" value="4, 9, 1, 7, 15, 3"></label><button class="btn" type="submit">Calculate</button></form><div class="output-box" id="out"></div>',
    r"""
function run() {
  const nums = document.getElementById('arr').value.split(',').map(x => Number(x.trim())).filter(x => !isNaN(x));
  const sum = nums.reduce((total, n) => total + n, 0);
  document.getElementById('out').textContent =
    `Array: [${nums.join(', ')}]\nCount: ${nums.length}\nSum: ${sum}\nAverage: ${(sum / nums.length).toFixed(2)}`;
}
run();""")

add("change-background-color", "Change Background Colour Using JavaScript",
    "Changes the page-box background with buttons, a colour picker and a random colour.",
    '''<div class="demo-area" id="target" style="min-height:120px;display:flex;align-items:center;justify-content:center;transition:.3s">Background colour demo</div>
<div style="margin-top:12px;">
  <button class="btn" onclick="setBg('#35d0ba')">Teal</button>
  <button class="btn" onclick="setBg('#ff7676')">Red</button>
  <button class="btn" onclick="setBg('#f1c40f')">Yellow</button>
  <button class="btn" onclick="randomBg()">Random</button>
  <label style="margin-left:8px">Pick: <input type="color" id="pick" value="#ff6b6b" oninput="setBg(this.value)"></label>
</div>
<div class="output-box" id="out"></div>''',
    r"""
const target = document.getElementById('target');
function setBg(color) {
  target.style.background = color;
  document.getElementById('out').textContent = 'Background colour set to ' + color;
}
function randomBg() {
  const color = '#' + Math.floor(Math.random() * 0xffffff).toString(16).padStart(6, '0');
  setBg(color);
}""")

add("inheritance", "Inheritance in JavaScript",
    "Subclasses with extends, super() and method overriding across two levels.",
    '<button class="btn" onclick="run()">Run Demo</button><div class="output-box" id="out"></div>',
    r"""
class Person {
  constructor(name) { this.name = name; }
  describe() { return `${this.name} is a person.`; }
}
class Student extends Person {                     // level 1 subclass
  constructor(name, course) { super(name); this.course = course; }
  describe() { return super.describe() + ` Studies ${this.course}.`; }   // overriding + super
}
class Intern extends Student {                     // level 2 subclass
  constructor(name, course, company) { super(name, course); this.company = company; }
  describe() { return super.describe() + ` Interns at ${this.company}.`; }
}
function run() {
  const p = new Person('Asha'), s = new Student('Ravi', 'BCA'), i = new Intern('Meena', 'B.Sc CS', 'TechCorp');
  document.getElementById('out').textContent =
    p.describe() + '\n' + s.describe() + '\n' + i.describe() +
    '\n\ni instanceof Intern: ' + (i instanceof Intern) + '\ni instanceof Student: ' + (i instanceof Student) + '\ni instanceof Person: ' + (i instanceof Person);
}""")

add("validate-name-email-phone-password", "Validate Name, Email, Phone Number and Password",
    "Checks four fields with regular expressions and lists every error found.",
    '''<form class="demo-form" id="valForm" onsubmit="return validate();">
  <label>Name (letters only)<input id="fname" type="text"></label>
  <label>Email<input id="femail" type="text"></label>
  <label>Phone (10 digits)<input id="fphone" type="text"></label>
  <label>Password (min 8, upper + lower + digit)<input id="fpass" type="password"></label>
  <button class="btn" type="submit">Submit</button>
</form><div class="output-box" id="out"></div>''',
    r"""
function validate() {
  const name = document.getElementById('fname').value.trim();
  const email = document.getElementById('femail').value.trim();
  const phone = document.getElementById('fphone').value.trim();
  const pass = document.getElementById('fpass').value;
  const errors = [];
  if (!/^[A-Za-z][A-Za-z ]{1,}$/.test(name)) errors.push('Name must contain only letters (min 2).');
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errors.push('Enter a valid email address.');
  if (!/^[6-9]\d{9}$/.test(phone)) errors.push('Phone must be 10 digits starting with 6-9.');
  if (!/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(pass)) errors.push('Password: 8+ chars with upper, lower and a digit.');
  document.getElementById('out').textContent = errors.length ? errors.join('\n') : 'All fields are valid! Form would now submit.';
  return false;
}""")
