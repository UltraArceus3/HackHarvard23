document.addEventListener('DOMContentLoaded', function() {

    var videoLinks = document.querySelectorAll('.video-link');
    var videoPlayer = document.querySelector("#player");

    var transcript = document.querySelector(".transcription");

    videoLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {

            e.preventDefault();
            var videoUrl = this.getAttribute('data_video');
            var summary = this.getAttribute('transcript');

            videoPlayer.querySelector('source').setAttribute('src', "/static/" + videoUrl);
            
            transcript.querySelector('p').innerHTML = summary;

            videoPlayer.load();
        });
    });

});