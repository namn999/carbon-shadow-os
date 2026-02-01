async function optimize() {
  const runtime = document.getElementById("runtime").value;
  const deadline = document.getElementById("deadline").value;

  const res = await fetch(
    `http://127.0.0.1:8000/optimize?runtime=${runtime}&deadline=${deadline}`,
    { method: "POST" }
  );

  const data = await res.json();
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}
