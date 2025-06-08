document.addEventListener('DOMContentLoaded', function() {
    // Обработка теста
    const testForm = document.getElementById('english-test');
    if (testForm) {
        testForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Получаем все ответы
            const answers = [];
            const questions = document.querySelectorAll('.question');
            
            questions.forEach((question, index) => {
                const selectedOption = question.querySelector('input[type="radio"]:checked');
                if (selectedOption) {
                    answers.push(parseInt(selectedOption.value));
                } else {
                    answers.push(null);
                }
            });
            
            // Проверяем ответы
            let correctAnswers = 0;
            const testData = JSON.parse(document.getElementById('test-data').textContent);
            
            answers.forEach((answer, index) => {
                if (answer === testData.questions[index].answer) {
                    correctAnswers++;
                }
            });
            
            // Показываем результат
            const resultDiv = document.getElementById('result');
            const resultText = document.getElementById('result-text');
            
            // Определяем уровень по количеству правильных ответов
            let level = '';
            if (correctAnswers <= 1) level = testData.results['0-1'];
            else if (correctAnswers === 2) level = testData.results['2'];
            else if (correctAnswers === 3) level = testData.results['3'];
            else if (correctAnswers === 4) level = testData.results['4'];
            else level = testData.results['5'];
            
            resultText.textContent = `Вы ответили правильно на ${correctAnswers} из ${questions.length} вопросов. ${level}`;
            resultDiv.classList.remove('hidden');
            
            // Прокручиваем к результату
            resultDiv.scrollIntoView({ behavior: 'smooth' });
        });
    }
    
    // Обработка формы обратной связи
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Здесь можно добавить AJAX-отправку формы
            alert('Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.');
            contactForm.reset();
        });
    }
});
