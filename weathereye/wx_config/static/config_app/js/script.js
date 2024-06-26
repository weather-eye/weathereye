// redirect to the SURFACE config page based on users choice
document.addEventListener('DOMContentLoaded', function() {
    const installSurfaceForm = document.getElementById('installTypeForm');
    const installSurfaceRadios = installSurfaceForm.querySelectorAll('input[type="radio"]');

    installSurfaceRadios.forEach(radio => {
        radio.addEventListener('click', function() {
            installSurfaceForm.submit();
        });
    });
});