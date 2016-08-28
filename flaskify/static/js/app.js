let React = require('react');
let ReactDOM = require('react-dom');
let axios = require('axios');


let Albums = React.createClass({

    getInitialState: function() {
        return {
            albums: []
        }
    },

    componentDidMount: function() {
        this.serverRequest = axios.get('/albums').then(function(result) {
            this.setState({
                albums: result.data.album
            });
        }.bind(this));
    },

    componentWillUnmount: function() {
        this.serverRequest.abort();
    },

    render: function(){
        var albums = this.state.albums.map(function(album, idx){
            return (<div className='col-xs-2 album' key={idx}>{album.name}</div>);
        })
        return (
            <div>{albums}</div>
        );
    }
});


let App = React.createClass({
    render: function(){
        return (
            <div>
                <h1>Flasify FTW!</h1>
                <Albums />
            </div>
        );
    }
});


ReactDOM.render(
    <App />,
    document.getElementById('app')
);
