function search(){
    var channel = document.getElementById('query').value;
    document.write('loading...')
    window.location.href = 'https://gif-invasion.herokuapp.com//search/' + channel;
}