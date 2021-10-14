jQuery(document).ready(function() {

    var winnerSquarePlayer1 = 16;

    // Winners file path
    var player1Plays = [];

    var squaresMap = [];

    squaresMap.push("1-10-10");
    squaresMap.push("2-80-10");
    squaresMap.push("3-150-10");
    squaresMap.push("4-220-10");
    squaresMap.push("5-10-80");
    squaresMap.push("6-80-80");
    squaresMap.push("7-150-80");
    squaresMap.push("8-220-80");
    squaresMap.push("9-10-150");
    squaresMap.push("10-80-150");
    squaresMap.push("11-150-150");
    squaresMap.push("12-220-150");
    squaresMap.push("13-10-220");
    squaresMap.push("14-80-220");
    squaresMap.push("15-150-220");
    squaresMap.push("16-220-220");

    jQuery("#plays_input textarea").val("");

    jQuery("#play").click(function() {
        var plays = jQuery("#plays_input textarea").val();

        if (plays != undefined && plays.length > 0) {
            jQuery(".piece1").delay(10).animate({ left: "10px", top: "60px" }, 500).delay(500);
            jQuery("#winner_strings").empty();

            jQuery(".player1wins").fadeOut("fast", function() {});

            var rows = plays.split("\n");
            var numberOfRows = rows.length;
            var numberOfSimulations = 0;
            for(var i=0; i<numberOfRows; ++i){
                 if (numberOfSimulations < 2){
                    var randInt = Math.floor(Math.random() * numberOfRows);
                    jQuery("#winner_strings").append("<p><b>Jugada ganadora "+(i+1)+":</b> "+rows[randInt]+"</p>");
                    playGame(rows[randInt]);
                    jQuery(".piece1").delay(1000).animate({ left: "10px", top: "60px" }, 500).delay(500);
                    ++numberOfSimulations;
                    jQuery(".player1wins").delay(5000).fadeOut("slow", function() {});
                 }
            }
        }
    });


    function playGame(play1) {
        play1 = play1.split(",");
        var notWinner = true;
        var contPlay1 = 0;
        var contMoves = 0;
        while(notWinner){
          ++contMoves;
          actualSquare = movePiece1(play1[++contPlay1], contMoves);
          if (actualSquare == winnerSquarePlayer1) {
              notWinner = false;
              jQuery(".player1wins").delay(5000).fadeIn("slow", function() {});
          }
        }

    }

    function movePiece1(square, moves) {
        var coords = squaresMap[square - 1].split("-");
        var left = coords[1] + "px";
        var top = parseInt(coords[2]) + 50;
        top = top + "px";
        if (moves == 2) {
            jQuery(".piece1").delay(500).animate({ left: left, top: top }, 500).delay(500);
        } else {
            jQuery(".piece1").animate({ left: left, top: top }, 500).delay(500);
        }
        return square;
    }



});