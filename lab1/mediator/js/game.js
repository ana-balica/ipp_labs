var Player = function(name, key) {
    this.name = name;    
    this.key = key;
    this.points = 0;
}

Player.prototype.play = function() {
    this.points += 1;
    Mediator.played();
};

var Scoreboard = {

    update: function(score) {
        c(score);
    }
};

var Mediator = {
    players: [],

    registerPlayer: function(player) {
        this.players.push(player);
    },

    played: function() {
        var score = {};
        var players = Mediator.players;
        for (var i = 0; i < players.length; i++) {
            score[players[i].name] = players[i].points;
        }
        Scoreboard.update(score);
    },

    play: function(e) {
        var players = Mediator.players;
        for (var i = 0; i < players.length; i++) {
            if (e.keyCode === players[i].key) {
                players[i].play();
                return;
            }
        }
    }
};


$(document).ready(function () {
    var player1 = new Player("Player1", 49);
    var player2 = new Player("Player2", 48);

    Mediator.registerPlayer(player1);
    Mediator.registerPlayer(player2);
    c(Mediator.players);

    window.onkeypress = Mediator.play;

    setTimeout(function () {
        window.onkeypress = null;
        c('Game over!');
    }, 30000);
});


function c(msg) {
    console.log(msg);
}