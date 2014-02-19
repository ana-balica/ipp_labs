var Player = function(name, key) {
    this.name = name;    
    this.key = key;
    this.points = 0;
}

Player.prototype.play = function(i) {
    this.points += 1;
    Observable.notifyObservers('scoreChange', this);
    return;
};

var Scoreboard = {

    update: function(player) {
        $('li#' + player.name).text(player.name + ' - ' + player.points.toString());
    },

    clear: function(players) {
        for (var i = 0; i < players.length; i++) {
            $('li#' + players[i].name).text(players[i].name + ' - 0');
            players[i].points = 0;
        }
        return players;
    },

    show_winner: function(players) {
        var score = [];
        for (var i = 0; i < players.length; i++) {
            score.push([players[i].name, players[i].points]);
        }
        score.sort(function(a, b) { return b[1] - a[1]; });
        $('#winner').text('Last winner - ' + score[0][0]);
        $('#winner').show();
    }
};


var Observable = {
    observers: [], 

    addObserver: function(topic, observer) {
        this.observers[topic] || (this.observers[topic] = []);
        this.observers[topic].push(observer);
    }, 

    removeObserver: function(topic, observer) {
        if (!this.observers[topic])
            return;

        var index = this.observers[topic].indexOf(observer)
        if (~index) {
            this.observers[topic].splice(index, 1);
        }
    }, 

    notifyObservers: function(topic, message) {
        if (!this.observers[topic])
            return;

        for (var i = this.observers[topic].length - 1; i >= 0; i--) {
            this.observers[topic][i](message);
        }
    }
};

$(document).ready(function () {
    var player1 = new Player("Player1", 48);
    var player2 = new Player("Player2", 49);
    var player3 = new Player("Player3", 50);
    var player4 = new Player("Player4", 51);
    var players = [player1, player2, player3, player4];

    for (var i = 0; i < players.length; i++) {
        $('ul').append("<li id='" + players[i].name + "'>" + players[i].name + " - 0</li>");
    }

    Observable.addObserver('scoreChange', Scoreboard.update);

    $('#winner').hide();

    $('button').on('click', function() {
        var button = $(this);
        $(button).attr('disabled','disabled');
        $(document).on('keyup', function(e) {
            for (var i = 0; i < players.length; i++) {
                if (e.keyCode === players[i].key) {
                    players[i].play();
                }
            }
        });
        setTimeout(function () {
            $(document).off('keyup');
            $(button).removeAttr('disabled');
            Scoreboard.show_winner(players);
            players = Scoreboard.clear(players);
        }, 30000);
    }) 
});


// helper function
function c(msg) {
    console.log(msg);
}