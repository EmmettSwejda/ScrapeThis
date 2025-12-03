window.onload = function () {
    const container = document.getElementById("showpage");

    container.addEventListener("mouseover", (e) => {
        // remove highlight from anything previously highlighted
        document.querySelectorAll('#showpage .highlight').forEach(el => {
            el.classList.remove('highlight');
        });

        // highlight ONLY the actual element under the cursor
        if (e.target !== container) {
            e.target.classList.add('highlight');
        }
    });

    container.addEventListener("mouseout", (e) => {
        e.target.classList.remove('highlight');
    });
};