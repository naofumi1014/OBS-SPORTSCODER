window.addEventListener("DOMContentLoaded", () => {
    const websocket = new WebSocket("ws://localhost:2222/");
    const websocket_timer = new WebSocket("ws://localhost:1234/");

    // pythonサーバー側からメッセージを受け取った場合に発火する

    //現在要素があったら削除して表示する機能

    websocket.onmessage = ({ data }) => {
        let obj = JSON.parse(data);


        //HOME チーム　既存の要素の削除 
        const remove_element_hometeam = document.querySelector('div.HOMETEAM');
        if (remove_element_hometeam !== null) {

            remove_element_hometeam.remove();
        }

        const messages_hometeam = document.createElement("div");
        messages_hometeam.className = 'HOMETEAM';
        document.body.appendChild(messages_hometeam);

        //div内の要素 の記入
        const content_hometeam = document.createTextNode(obj.HOME.team);
        messages_hometeam.appendChild(content_hometeam);


        //HOME 得点　既存の要素の削除 
        const remove_element_homepoint = document.querySelector('div.HOMETEAM_POINT');
        if (remove_element_homepoint !== null) {

            remove_element_homepoint.remove();
        }

        const messages_homepoint = document.createElement("div");
        messages_homepoint.className = 'HOMETEAM_POINT';
        document.body.appendChild(messages_homepoint);

        //div内の要素 の記入
        const content_homepoint = document.createTextNode(obj.HOME.point);
        messages_homepoint.appendChild(content_homepoint);


        //VISITOR チーム　既存の要素の削除 
        const remove_element_visitorteam = document.querySelector('div.VISITORTEAM');
        if (remove_element_visitorteam !== null) {

            remove_element_visitorteam.remove();
        }

        const messages_visitorteam = document.createElement("div");
        messages_visitorteam.className = 'VISITORTEAM';
        document.body.appendChild(messages_visitorteam);

        //div内の要素 の記入
        const content_visitorteam = document.createTextNode(obj.VISITOR.team);
        messages_visitorteam.appendChild(content_visitorteam);



        //VISITOR 得点　既存の要素の削除 
        const remove_element_visitorpoint = document.querySelector('div.VISITORTEAM_POINT');
        if (remove_element_visitorpoint !== null) {

            remove_element_visitorpoint.remove();
        }

        const messages_visitorpoint = document.createElement("div");
        messages_visitorpoint.className = 'VISITORTEAM_POINT';
        document.body.appendChild(messages_visitorpoint);

        //div内の要素 の記入
        const content_visitorpoint = document.createTextNode(obj.VISITOR.point);
        messages_visitorpoint.appendChild(content_visitorpoint);





        //ピリオド　既存の要素の削除
        const remove_element_period = document.querySelector('div.PERIOD');
        if (remove_element_period !== null) {
            remove_element_period.remove();
        }

        //<div class='position'> の作成
        const messages_period = document.createElement("div");
        messages_period.className = 'PERIOD';
        document.body.appendChild(messages_period);

        //div内の要素 の記入
        const content_period = document.createTextNode(obj.PERIOD);
        messages_period.appendChild(content_period);



    };

    websocket_timer.onmessage = ({ data }) => {


        //要素のみを削除する機能
        if (JSON.parse(data)[0] == 'False') {

            console.log('めいん削除')
                //要素の削除 main
            const remove_element_main = document.querySelector('.position_main');
            if (remove_element_main !== null) {
                remove_element_main.parentNode.removeChild(remove_element_main);
            }

            //behind
            const remove_element_behind = document.querySelector('.position_behind');
            if (remove_element_behind !== null) {
                remove_element_behind.parentNode.removeChild(remove_element_behind);
            }

        }

        if (JSON.parse(data)[0] == 'main') {

            //既存の要素の削除
            const remove_element = document.querySelector('div.position_main');
            if (remove_element !== null) {
                console.log('reload element')
                remove_element.remove();
            }

            //<div class='position'> の作成
            const messages = document.createElement("div");
            messages.className = 'position_main';
            document.body.appendChild(messages);

            //div内の要素 の記入
            const content = document.createTextNode(JSON.parse(data)[1]);
            messages.appendChild(content);

            console.log(data);
            console.log(content);
        }

        if (JSON.parse(data)[0] == 'behind') {
            //ビハインドタイマーのみの削除
            if (JSON.parse(data)[1] == 'False') {
                const remove_element = document.querySelector('div.position_behind');
                if (remove_element !== null) {
                    console.log('remove behind element')
                    remove_element.remove();
                }
            } else {

                //既存の要素の削除
                const remove_element = document.querySelector('div.position_behind');
                if (remove_element !== null) {
                    console.log('reload element')
                    remove_element.remove();
                }

                //<div class='position'> の作成
                const messages = document.createElement("div");
                messages.className = 'position_behind';
                document.body.appendChild(messages);

                //div内の要素 の記入
                const content = document.createTextNode(JSON.parse(data)[1]);
                messages.appendChild(content);

                console.log(data);
                console.log(content);
            }
        }
    };


});