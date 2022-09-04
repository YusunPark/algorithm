const solution = (participants, completions) => {
  participants.sort();
  completions.sort();

  while (participants.length) {
    const participant = participants.pop();
    const completion = completions.pop();
    if (participant !== completion) {
      return participant;
    }
  }
};
