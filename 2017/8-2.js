(function () {
"use strict";

const registers = {};

function parse(input) {
  const instructions = [];
  const lines = input.split("\n");
  for (let line of lines) {
    let result = line.match(/^(\w+) (inc|dec) ([-\d]+) if (\w+) ([<>!=]+) ([-\d]+)$/);
    let instruction = {
      to_modify: result[1],
      inc_dec: result[2],
      amount: Number(result[3]),
      compare_reg: result[4],
      comparison_operator: result[5],
      compare_num: Number(result[6]),
    }
    registers[instruction.to_modify] = 0;
    // console.log(line, result, instruction);
    instructions.push(instruction);
  }
  return instructions;
}

function process(instructions) {
  let highest_seen = 0;
  for (let instruction of instructions) {
    // Evaluate the condition.
    let condition_is_true;
    let reg_value = registers[instruction.compare_reg];
    if (instruction.comparison_operator === '>') {
      condition_is_true = reg_value > instruction.compare_num;
    } else if (instruction.comparison_operator === '<') {
      condition_is_true = reg_value < instruction.compare_num;
    } else if (instruction.comparison_operator === '>=') {
      condition_is_true = reg_value >= instruction.compare_num;
    } else if (instruction.comparison_operator === '<=') {
      condition_is_true = reg_value <= instruction.compare_num;
    } else if (instruction.comparison_operator === '==') {
      condition_is_true = reg_value === instruction.compare_num;
    } else if (instruction.comparison_operator === '!=') {
      condition_is_true = reg_value !== instruction.compare_num;
    } else {
      throw `Operator ${instruction.comparison_operator} is not supported.`
    }

    if (condition_is_true) {
      if (instruction.inc_dec === 'inc') {
        registers[instruction.to_modify] += instruction.amount;
      } else if (instruction.inc_dec === 'dec') {
        registers[instruction.to_modify] -= instruction.amount;
      } else {
        throw 'WOAH';
      }
      if (registers[instruction.to_modify] > highest_seen) {
        highest_seen = registers[instruction.to_modify];
      }
      // console.log(registers);
    } else {
      // console.info(`Skipping ${instruction.to_modify} ${instruction.inc_dec} ${instruction.amount}.`);
    }
  }
  return highest_seen;
}

let input = `
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
`.trim();
input = document.body.innerText.trim();

const instructions = parse(input);
console.log(process(instructions));

})();
