const solution = (pyString) => {
  return (
    pyString.toUpperCase().split("P").length ===
    pyString.toUpperCase().split("Y").length
  );
};

["pPoooyY", "Pyy"].forEach((s) => {
  const result = solution(s);
  console.log(result);
});
