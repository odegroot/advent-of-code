(function () {
"use strict";

class Parser {
  /**
   * @param {string} stream
   */
  constructor(stream) {
    this.stream = stream;
    this.position = 0;
    this.parse_tree = this.parse_group();
    if (this.position !== this.stream.length) {
      throw new Error('Did not consume all input.');
    }
  }

  parse_group() {
    if (this.current_character() !== '{') {
      throw new Error(`Unexpected character '${this.current_character()}' at position ${this.position}.`)
    }
    this.position += 1;
    let parse_tree = [];
    while (this.current_character() !== '}') {
      if (this.current_character() === '{') {
        parse_tree.push(this.parse_group());
      } else if (this.current_character() === '<') {
        parse_tree.push(this.parse_garbage());
      } else if (this.current_character() === ',') {
        this.position += 1;
        // Note, this accepts things like {,,<>,,}, which it shouldn't, but we don't have to reject it either.
      }
    }
    this.position += 1;
    return parse_tree;
  }

  parse_garbage() {
    const substring = this.stream.slice(this.position);
    const garbage = substring.match(/^<(?:!.|[^>!])*>/)[0];
    this.position += garbage.length;
    return garbage;
  }

  current_character() {
    return this.stream[this.position];
  }

  static count_groups(parse_tree) {
    let count;
    if (Array.isArray(parse_tree)) {
      count = 1;
      for (let group_element of parse_tree) {
        count += count_groups(group_element);
      }
    } else if (typeof parse_tree === 'string') {
      count = 0;
    } else {
      throw new Error('WOAH');
    }
    return count;
  }

  static total_score(parse_tree, level) {
    let score;
    if (Array.isArray(parse_tree)) {
      score = level;
      for (let group_element of parse_tree) {
        score += total_score(group_element, level + 1);
      }
    } else if (typeof parse_tree === 'string') {
      score = 0;
    } else {
      throw new Error('WOAH');
    }
    return score;
  }

  /**
   * @param {string} garbage
   */
  static count_garbage_characters(garbage) {
    return garbage.replace(/!./g, '').length - 2;
  }

  static total_garbage(parse_tree) {
    if (Array.isArray(parse_tree)) {
      let count = 0;
      for (let group_element of parse_tree) {
        count += this.total_garbage(group_element);
      }
      return count;
    } else if (typeof parse_tree === 'string') {
      return this.count_garbage_characters(parse_tree);
    } else {
      throw new Error('WOAH');
    }
  }

  static test_garbage() {
    const garbage_tests = {
      '<>': true,
      '<a>': true,
      '<random characters>': true,
      '<<<<>': true,
      '<{!>}>': true,
      '<!!>': true,
      '<!!!>>': true,
      '<{o"i!a,<{i<a>': true,
      '<ia!!!!!>"!>},<!!u!!!!!>,<a!<!!!>>': true,
      '<>a': false,
      '<>>': false,
      '<': false,
      '<!>': false,
      '{<>': false,
    };
    for (let stream in garbage_tests) {
      if (/^<(?:!.|[^>!])*>$/.test(stream) === garbage_tests[stream]) {
        console.info('✓');
      } else {
        console.error(`garbage.parse('${stream}').kind should be ${garbage_tests[stream]}.`);
      }
    }
  }

  static test_parsing() {
    const tests = {
      '{}': [],
      '{{{}}}': [[[]]],
      '{{},{}}': [[],[]],
      '{{{},{},{{}}}}': [[[],[],[[]]]],
      '{<{},{},{{}}>}': ['<{},{},{{}}>'],
      '{<a>,<a>,<a>,<a>}': ['<a>','<a>','<a>','<a>'],
      '{{<a>},{<a>},{<a>},{<a>}}': [['<a>'],['<a>'],['<a>'],['<a>']],
      '{{<!>},{<!>},{<!>},{<a>}}': [['<!>},{<!>},{<!>},{<a>']],
      '{{},<>}': [[], '<>'],
      '{<ia!!!!!>"!>},<!!u!!!!!>,<a!<!!!>>,{}}': ['<ia!!!!!>"!>},<!!u!!!!!>,<a!<!!!>>', []],
    };
    for (let stream in tests) {
      let expected = tests[stream];
      let actual = new Parser(stream).parse_tree;
      if (JSON.stringify(actual) === JSON.stringify(expected)) {
        console.info('✓');
      } else {
        console.error(actual, expected);
        throw new Error('parsing failed');
      }
    }
  }

  static test_group_count() {
    const tests = {
      '{}': 1,
      '{{{}}}': 3,
      '{{},{}}': 3,
      '{{{},{},{{}}}}': 6,
      '{<{},{},{{}}>}': 1,
      '{<a>,<a>,<a>,<a>}': 1,
      '{{<a>},{<a>},{<a>},{<a>}}': 5,
      '{{<!>},{<!>},{<!>},{<a>}}': 2,
      '{{},<>}': 2,
    };
    for (let stream in tests) {
      let expected = tests[stream];
      let parse_tree = new Parser(stream).parse_tree;
      let actual = Parser.count_groups(parse_tree);
      if (actual === expected) {
        console.info('✓');
      } else {
        console.error(`${stream}: expected ${expected}, actual ${actual}.`);
        throw new Error('Group count failed.');
      }
    }
  }

  static test_total_score() {
    const tests = {
      '{}': 1,
      '{{{}}}': 6,
      '{{},{}}': 5,
      '{{{},{},{{}}}}': 16,
      '{<a>,<a>,<a>,<a>}': 1,
      '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
      '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
      '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
    };
    for (let stream in tests) {
      let expected = tests[stream];
      let parse_tree = new Parser(stream).parse_tree;
      let actual = Parser.total_score(parse_tree, 1);
      if (actual === tests[stream]) {
        console.info('✓');
      } else {
        console.error(`${stream}: expected ${expected}, actual ${actual}.`);
        console.info(reply.value);
      }
    }
  }

  static test_garbage_count() {
    const tests = {
      '<>': 0,
      '<random characters>': 17,
      '<<<<>': 3,
      '<{!>}>': 2,
      '<!!>': 0,
      '<!!!>>': 0,
      '<{o"i!a,<{i<a>': 10,
    };
    for (let garbage in tests) {
      let expected = tests[garbage];
      let actual = Parser.count_garbage_characters(garbage);
      if (actual === expected) {
        console.info('✓');
      } else {
        console.error(`${garbage}: expected ${expected}, actual ${actual}.`);
        throw new Error('Test failed.');
      }
    }
  }
}

// Parser.test_garbage();
// Parser.test_parsing();
// Parser.test_group_count();
// Parser.test_total_score();
// Parser.test_garbage_count();

const input = document.body.innerText.trim();
const parse_tree = new Parser(input).parse_tree;
console.log(Parser.total_garbage(parse_tree));

})();
