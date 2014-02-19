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
        for (sc in score) {
            $('#' + sc).text(score[sc]);
        }
    },

    clear: function(players) {
        for (var i = 0; i < players.length; i++) {
            $('#' + players[i].name).text('0');
        }
    },

    show_winner: function(players) {
        var score = [];
        for (var i = 0; i < players.length; i++) {
            score.push([players[i].name ,$('#' + players[i].name).text()]);
        }
        score.sort(function(a, b) { return b[1] - a[1]; });
        $('#winner').text('Last winner - ' + score[0][0]);
        $('#winner').show();
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
    },

    game_over: function(e) {
        Scoreboard.show_winner(Mediator.players);
        Scoreboard.clear(Mediator.players);
    }
};


$(document).ready(function () {
    var player1 = new Player("Player1", 49);
    var player2 = new Player("Player2", 48);

    Mediator.registerPlayer(player1);
    Mediator.registerPlayer(player2);

    window.onkeypress = Mediator.play;
    $('#winner').hide();

    $('button').on('click', function() {
        var button = $(this);
        $(button).attr('disabled','disabled');
        window.onkeypress = Mediator.play;
        setTimeout(function () {
            window.onkeypress = null;
            $(button).removeAttr('disabled');
            Mediator.game_over();
        }, 30000);
    }) 
});


// helper function
function c(msg) {
    console.log(msg);
}