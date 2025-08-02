document.addEventListener('DOMContentLoaded', function ()  {
    const categoryMap = window.categoryMapData;

    const categorySelect = document.querySelector('#id_category');
    const titleInput = document.querySelector('#id_title');
    const suggestionsBox = document.querySelector('.suggestions-box');  // ✅ FIXED

    if (!categorySelect || !titleInput || !suggestionsBox) return;

    categorySelect.addEventListener('change', function () {
        const selectedCategory = this.value;
        const suggestions = categoryMap[selectedCategory] || [];

        suggestionsBox.innerHTML = ''; // clear previous
        suggestionsBox.style.display = suggestions.length > 0 ? 'block' : 'none';

        suggestions.forEach(item => {
            const div = document.createElement('div');
            div.textContent = item;
            div.style.cursor = 'pointer';
            div.style.border = '1px solid #ccc';
            div.style.padding = '5px';
            div.style.marginBottom = '2px';
            div.style.backgroundColor = '#f8f8f8';
            div.addEventListener('click', () => {
                titleInput.value = item;
                suggestionsBox.style.display = 'none';
            });
            suggestionsBox.appendChild(div);
        });
    });
});
