document.addEventListener('DOMContentLoaded', function() {
    const scenarios = document.querySelectorAll('.scenario');
    const submitButton = document.getElementById('submit');
    let ansCounter = 0;
    const questionCount = scenarios.length;

    scenarios.forEach((scenario, index) => {
        const buttons = scenario.querySelectorAll('.options');
        const answerInput = document.getElementById(`answer${index + 1}`);

        buttons.forEach(button => {
            button.addEventListener('click', function() {
                buttons.forEach(btn => {
                    if (btn !== button) {
                        btn.disabled = true;
                        btn.style.backgroundColor = '';
                    } else {
                        btn.style.backgroundColor = 'lightblue';

                        answerInput.value = button.value;

                        if (!scenario.classList.contains('answered')) {
                            ansCounter++;
                            scenario.classList.add('answered');
                        }
                    }
                });

                if (ansCounter === questionCount) {
                    submitButton.classList.remove('hidden');
                    submitButton.classList.add('show'); 
                }
            });
        });
    });
});
