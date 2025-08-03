// static/js/category_Suggestions.js

document.addEventListener('DOMContentLoaded', () => {
    const categorySelect = document.querySelector('select[name="category"]');
    const titleInput = document.querySelector('input[name="thing_name"]') || document.querySelector('input[name="title"]');
    const suggestionsBox = document.querySelector('.suggestions-box');

    if (!categorySelect || !titleInput || !suggestionsBox) return;

    categorySelect.addEventListener('change', () => {
        const selectedCategory = categorySelect.value;
        const suggestions = window.categoryMapData[selectedCategory] || [];

        suggestionsBox.innerHTML = '';
        suggestionsBox.style.display = suggestions.length ? 'block' : 'none';

        suggestions.forEach(suggestion => {
            const div = document.createElement('div');
            div.textContent = suggestion;
            div.classList.add('suggestion-item');
            div.style.cursor = 'pointer';
            div.onclick = () => {
                titleInput.value = suggestion;
                suggestionsBox.innerHTML = '';
                suggestionsBox.style.display = 'none';
            };
            suggestionsBox.appendChild(div);
        });
    });
});
