document.addEventListener('DOMContentLoaded', function() {

    var videoLinks = document.querySelectorAll('.video-link');
    var videoPlayer = document.querySelector("#player");

    videoLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {

            e.preventDefault();
            var videoUrl = this.getAttribute('data_video');

            videoPlayer.querySelector('source').setAttribute('src', "/static/" + videoUrl);
            
            videoPlayer.load();
        });
    });

});