"""
This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
This will be done by using python’s flask library."""


def score_server():
    """This function will serve the score. It will read the score from the scores file and return html"""
    score = ''
    try:
        with open('scores.txt', 'r') as file:
            score = file.read()
            html = f"""
                    <html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>The score is:</h1>
                            <div id="score">{score}</div>
                        </body>
                    </html>
                    """
            return html
    except Exception as ERROR:
        print(f'Error: {ERROR}')
        html = f"""
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>ERROR:</h1>
                        <div id="score"> style="color:red">{ERROR}</div>
                    </body>
                </html>
                """
        return html


