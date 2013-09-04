var casper = require('casper').create({
    viewportSize : {width : 800, height : 600},
    verbose: true,
    logLevel: "debug",
});

casper.start("http://localhost:8000/polls/", function userInterface() {
    this.capture("no-polls-available.png");
});

casper.thenOpen('http://localhost:8000/admin/', function loginAdmin() {
        this.capture("login.png");
        this.fill(
            'form[action="/admin/"]',
            { username: 'admin', password: 'password' },
            true
            );
        this.waitForSelector("#site-name");
        });

casper.then(function() {
    this.capture("logged-in-admin.png");
    this.click('a[href="/admin/polls/poll/"]');
    this.waitForSelector("#changelist");
});

casper.then(function() {
    this.capture("polls-admin.png");
    this.click(".addlink");
    this.waitForSelector("#poll_form");
});

/// "add-new-poll"
casper.then(function addNewPoll() {
    this.capture("add-new-poll.png");
    this.fill(
        '#poll_form',
        {
            question: 'What is your favorite color?',
        'choice_set-0-choice_text' : "Blue. No, green!",
        'choice_set-1-choice_text' : "Yellow",
        'choice_set-2-choice_text' : "Red"
        },
        false
        );
    this.click(".datetimeshortcuts a[href*=handleCalendar]");
    this.click(".datetimeshortcuts a[href*=handleClock]");
    this.capture("add-new-poll-filled-in.png");
    this.click("input[name=_save]");
    this.waitForSelector("li.info")
});
/// @end

casper.then(function() {
    this.capture("poll-added.png");
});

casper.thenOpen("http://localhost:8000/polls/", function() {
    this.capture("index.png");
    this.click("a");
    this.waitForSelector("form");
});

function randomVote(capture) {
    casper.then(function() {
        var options = this.getElementsAttribute('input[name="choice"]', 'id');
        var index = Math.floor(Math.random() * options.length);
        var option = options[index];
        this.click("#" + option);
        if (capture) {
            this.capture("voting.png");
        }
        this.click("input[type=submit]");
        this.waitForSelector("ul");
    });
};

function voteAgain() {
    casper.then(function() {
        this.click("a");
    });
};

casper.then(function() {
    this.capture("detail.png");
    console.log("about to call randomVote");
    randomVote(true);
});

casper.then(function() {
    this.capture("voted.png");
});

casper.then(function() {
    for (var i = 0; i < 10; i++) {
        randomVote(false);
        voteAgain();
    }
})

casper.then(function() {
    randomVote(false);
    casper.then(function() {
        this.capture("many-votes.png");
    });
});

casper.run();
