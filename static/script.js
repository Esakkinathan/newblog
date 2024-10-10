function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

function toggleMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
  }

  window.onclick = function(event) {
    if (!event.target.matches('.menu-button')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  function closeToast() {
    const container = document.getElementById('toast-container');
    container.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', (event) => {
    const container = document.getElementById('toast-container');
    const toasts = document.querySelectorAll('.toast');

    toasts.forEach(toast => {
        const closeBtn = toast.querySelector('.close-btn');
        closeBtn.addEventListener('click', () => {
            toast.style.display = 'none';
            container.style.display = 'none';
        });

        setTimeout(() => {
            if (toast.style.display !== 'none') {
                toast.style.display = 'none';
                container.style.display = 'none';
            }
        }, 5000);
    });
});
