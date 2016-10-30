var app = angular.module('pokemonApp', []);

app.controller('MainController', function($q, $http) {
    
    var ctrl = this;

    var mode = 'generate';
    ctrl.isModeGenerate = function() {
        return mode === 'generate';
    };

    ctrl.selectMode = function(newMode) {
        mode = newMode === 'decrypt' ? 'decrypt' : 'generate';
    };

    ctrl.decrypt = function() {
        var storyJson = document.querySelector('#txt-encrypted').value;
        return $http({
            method: "post",
            url: '/api/text',
            data: storyJson,
            responseType: "arraybuffer"
        }).then(function(resp) {
            var arrayBufferView = new Uint8Array( resp.data );
            var img = document.querySelector( "#img-plain" );
            img.src = 'data:image/png;base64,' + encode(arrayBufferView);
        });
    };

    ctrl.generateStory = function() {
        var txtPlain = document.querySelector('#txt-plain');
        return fetchStory(txtPlain.value).then(function(story) {
            ctrl.activeStory = story;
        });
    };

    var showRawStory = false;
    ctrl.toggleRawStory = function() {
        showRawStory = !showRawStory;
    }
    ctrl.isShowingRawStory = function() {
        return showRawStory;
    };

    function hexToBase64(str) {
        return btoa(String.fromCharCode.apply(null, str.replace(/\r|\n/g, "").replace(/([\da-fA-F]{2}) ?/g, "0x$1 ").replace(/ +$/, "").split(" ")));
    }

    function fetchStory(text) {
        //return $q.resolve([{"trainer": "Red", "message": "Red challenges Ash to battle!"}, {"trainer": "Red", "message": "Red: Oddish, Charmeleon, I choose you!"}, {"trainer": "Ash", "message": "Ash: Hitmonchan, Dewgong, I choose you!"}, {"trainer": "Red", "message": "Oddish uses Round on Hitmonchan"}, {"trainer": "Red", "message": "Charmeleon uses Flamethrower on Dewgong"}, {"trainer": "Ash", "message": "Hitmonchan uses Venoshock on Oddish"}, {"trainer": "Ash", "message": "Dewgong uses Substitute on Charmeleon"}, {"trainer": "Red", "message": "Oddish uses Thunder on Hitmonchan"}, {"trainer": "Red", "message": "Charmeleon uses Earthquake on Dewgong"}, {"trainer": "Ash", "message": "Hitmonchan uses Toxic on Oddish"}, {"trainer": "Ash", "message": "Dewgong uses Flash on Charmeleon"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Flash Cannon on Hitmonchan"}, {"trainer": "Red", "message": "Charmeleon fainted!"}, {"trainer": "Red", "message": "Red: Onix, I choose you!"}, {"trainer": "Ash", "message": "Hitmonchan uses Psych Up on Oddish"}, {"trainer": "Ash", "message": "Dewgong fainted!"}, {"trainer": "Ash", "message": "Ash: Ditto, I choose you!"}, {"trainer": "Red", "message": "Oddish uses Torment on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Embargo on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Thunderbolt on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Swords Dance on Onix"}, {"trainer": "Red", "message": "Oddish uses Aerial Ace on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Smack Down on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Double Team on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Volt Switch on Onix"}, {"trainer": "Red", "message": "Oddish uses Thunder Wave on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Hail on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Psyshock on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Flame Charge on Onix"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Flash Cannon on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Retaliate on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Low Sweep on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Venoshock on Onix"}, {"trainer": "Red", "message": "Oddish uses Hail on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Dark Pulse on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Return on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Low Sweep on Onix"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Roost on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Snarl on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Dream Eater on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Dazzling Gleam on Onix"}, {"trainer": "Red", "message": "Oddish uses Snarl on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Roost on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Frustration on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Brick Break on Onix"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Hail on Hitmonchan"}, {"trainer": "Red", "message": "Onix fainted!"}, {"trainer": "Red", "message": "Red: Golduck, I choose you!"}, {"trainer": "Ash", "message": "Hitmonchan uses Retaliate on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Payback on Golduck"}, {"trainer": "Red", "message": "Oddish uses Nature Power on Hitmonchan"}, {"trainer": "Red", "message": "Golduck uses Flamethrower on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Taunt on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Swords Dance on Golduck"}, {"trainer": "Red", "message": "Oddish uses Protect on Hitmonchan"}, {"trainer": "Red", "message": "Golduck uses Will-O-Wisp on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses False Swipe on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Low Sweep on Golduck"}, {"trainer": "Red", "message": "Oddish uses Sunny Day on Hitmonchan"}, {"trainer": "Red", "message": "Golduck uses Thunderbolt on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Wild Charge on Oddish"}, {"trainer": "Ash", "message": "Ditto fainted!"}, {"trainer": "Ash", "message": "Ash: Drowzee, I choose you!"}, {"trainer": "Red", "message": "Red is angry!"}, {"trainer": null, "message": "Match ended in a DRAW"}]);

        return $http({
            method: "post",
            url: '/api/story',
            data: text
        }).then(function(resp) {
            return resp.data;
        });

        return $q.resolve([{"trainer": "Red", "message": "Red challenges Ash to battle!"}, {"trainer": "Red", "message": "Red: Oddish, Charmeleon, I choose you!"}, {"trainer": "Ash", "message": "Ash: Hitmonchan, Dewgong, I choose you!"}, {"trainer": "Red", "message": "Oddish uses Round on Hitmonchan"}, {"trainer": "Red", "message": "Charmeleon uses Flamethrower on Dewgong"}, {"trainer": "Ash", "message": "Hitmonchan uses Venoshock on Oddish"}, {"trainer": "Ash", "message": "Dewgong uses Substitute on Charmeleon"}, {"trainer": "Red", "message": "Oddish uses Thunder on Hitmonchan"}, {"trainer": "Red", "message": "Charmeleon uses Earthquake on Dewgong"}, {"trainer": "Ash", "message": "Hitmonchan uses Toxic on Oddish"}, {"trainer": "Ash", "message": "Dewgong uses Flash on Charmeleon"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Flash Cannon on Hitmonchan"}, {"trainer": "Red", "message": "Charmeleon fainted!"}, {"trainer": "Red", "message": "Red: Onix, I choose you!"}, {"trainer": "Ash", "message": "Hitmonchan uses Psych Up on Oddish"}, {"trainer": "Ash", "message": "Dewgong fainted!"}, {"trainer": "Ash", "message": "Ash: Ditto, I choose you!"}, {"trainer": "Red", "message": "Oddish uses Torment on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Embargo on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Thunderbolt on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Swords Dance on Onix"}, {"trainer": "Red", "message": "Oddish uses Aerial Ace on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Smack Down on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Double Team on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Volt Switch on Onix"}, {"trainer": "Red", "message": "Oddish uses Thunder Wave on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Hail on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Psyshock on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Flame Charge on Onix"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Flash Cannon on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Retaliate on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Low Sweep on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Venoshock on Onix"}, {"trainer": "Red", "message": "Oddish uses Hail on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Dark Pulse on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Return on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Low Sweep on Onix"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Roost on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Snarl on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Dream Eater on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Dazzling Gleam on Onix"}, {"trainer": "Red", "message": "Oddish uses Snarl on Hitmonchan"}, {"trainer": "Red", "message": "Onix uses Roost on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Frustration on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Brick Break on Onix"}, {"trainer": "Red", "message": "Red is STRONG"}, {"trainer": "Red", "message": "Oddish uses Hail on Hitmonchan"}, {"trainer": "Red", "message": "Onix fainted!"}, {"trainer": "Red", "message": "Red: Golduck, I choose you!"}, {"trainer": "Ash", "message": "Hitmonchan uses Retaliate on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Payback on Golduck"}, {"trainer": "Red", "message": "Oddish uses Nature Power on Hitmonchan"}, {"trainer": "Red", "message": "Golduck uses Flamethrower on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Taunt on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Swords Dance on Golduck"}, {"trainer": "Red", "message": "Oddish uses Protect on Hitmonchan"}, {"trainer": "Red", "message": "Golduck uses Will-O-Wisp on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses False Swipe on Oddish"}, {"trainer": "Ash", "message": "Ditto uses Low Sweep on Golduck"}, {"trainer": "Red", "message": "Oddish uses Sunny Day on Hitmonchan"}, {"trainer": "Red", "message": "Golduck uses Thunderbolt on Ditto"}, {"trainer": "Ash", "message": "Hitmonchan uses Wild Charge on Oddish"}, {"trainer": "Ash", "message": "Ditto fainted!"}, {"trainer": "Ash", "message": "Ash: Drowzee, I choose you!"}, {"trainer": "Red", "message": "Red is angry!"}, {"trainer": null, "message": "Match ended in a DRAW"}]);
    }

    // public method for encoding an Uint8Array to base64
    function encode (input) {
        var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;

        while (i < input.length) {
            chr1 = input[i++];
            chr2 = i < input.length ? input[i++] : Number.NaN; // Not sure if the index 
            chr3 = i < input.length ? input[i++] : Number.NaN; // checks are needed here

            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;

            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }
            output += keyStr.charAt(enc1) + keyStr.charAt(enc2) +
                      keyStr.charAt(enc3) + keyStr.charAt(enc4);
        }
        return output;
    }
});