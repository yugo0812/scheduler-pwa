async function fetchReviews() {
    const history = JSON.parse(localStorage.getItem("studyHistory") || "[]");
    const res = await fetch("/api/review", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(history),
    });
    const { due_items } = await res.json();
    renderReviewList(due_items);
}
