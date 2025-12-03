window.onload = function () {
    // div holding the page
    const container = document.getElementById("showpage");

    // If item is hovered highlight it.
    container.addEventListener("mouseover", (e) => {
        document.querySelectorAll('#showpage .highlight').forEach(el => {
            el.classList.remove('highlight');
        });

        // only the elem hovered
        if (e.target !== container) {
            e.target.classList.add('highlight');
        }
    });

    // Remove the highlight
    container.addEventListener("mouseout", (e) => {
        e.target.classList.remove('highlight');
    });

    container.addEventListener("click",(e)=>{
        // adding item to watch list



    })
};