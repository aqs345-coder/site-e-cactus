document.addEventListener("DOMContentLoaded", () => {
  // 1. OTIMIZAÇÃO: Aborta o script em telas de toque ou dispositivos sem mouse
  if (window.matchMedia("(pointer: coarse)").matches) {
    return;
  }

  const cursor = document.createElement("div");
  cursor.classList.add("cursor");
  cursor.innerHTML =
    '<div class="cursor__dot"></div><div class="cursor__ring"></div>';
  document.body.appendChild(cursor);

  const dot = cursor.querySelector(".cursor__dot");
  const ring = cursor.querySelector(".cursor__ring");

  let mouseX = 0;
  let mouseY = 0;
  let ringX = 0;
  let ringY = 0;

  // 2. OTIMIZAÇÃO: O evento apenas atualiza variáveis na memória (Custo zero de CPU)
  document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  // 3. OTIMIZAÇÃO: O render visual sincronizado a 60fps para ambos os elementos
  function renderCursor() {
    // Ponto segue instantaneamente, mas usa translate3d para aceleração de GPU
    dot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;

    // Anel segue com atraso (lerp)
    ringX += (mouseX - ringX) * 0.25;
    ringY += (mouseY - ringY) * 0.25;
    ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0) translate(-50%, -50%)`;

    requestAnimationFrame(renderCursor);
  }

  // Inicia o loop
  renderCursor();

  // Delegação de eventos mantida (sua lógica estava ótima aqui)
  const hoverTargets =
    'a, button, .btn, input, textarea, select, [role="button"], .card, .spec-card, .team__member';
  const textTargets = "input, textarea, [contenteditable]";

  document.addEventListener("mouseover", (e) => {
    if (e.target.closest(hoverTargets)) cursor.classList.add("cursor--hover");
    if (e.target.closest(textTargets)) cursor.classList.add("cursor--text");
  });

  document.addEventListener("mouseout", (e) => {
    if (e.target.closest(hoverTargets))
      cursor.classList.remove("cursor--hover");
    if (e.target.closest(textTargets)) cursor.classList.remove("cursor--text");
  });

  document.addEventListener("mousedown", () =>
    cursor.classList.add("cursor--click"),
  );
  document.addEventListener("mouseup", () =>
    cursor.classList.remove("cursor--click"),
  );
});
