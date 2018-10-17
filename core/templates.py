indexTemp = """
<!DOCTYPE html>
<html>

<head>
    <title>Welcome!</title>
    <style type="text/css">
    * {
        font-family: Helvetica Neue, sans-serif;
        color: #0f0f0f;
    }

    html,
    body {
        margin: 0;
    }

    div.flex {
        display: flex;
        width: 100vw;
        height: 100vh;
        align-items: center;
        justify-content: center;
    }

    div.box {
        display: block;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 10px;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    p {
        margin: 0;
    }

    h1.title {
        text-align: center;
        margin-bottom: 10px;
    }

    hr {
        height: 1px;
        background: #ddd;
        border: none;
    }
    </style>
</head>

<body>
    <div class="flex">
        <div class="box">
            <h1 class="title">Welcome to my Website!</h1>
            <hr>
            <p>This is a brand new spanking website ran by a Python Web Server!</p>
            <hr>
            <p><a href="https://github.com/reinspect/amok">Amok</a></p>
        </div>
    </div>
</body>

</html>
"""

errorTemp = """
<!DOCTYPE html>
<html>

<head>
    <title>Page not found!</title>
    <style type="text/css">
    * {
        font-family: Helvetica Neue, sans-serif;
        color: #0f0f0f;
    }

    html,
    body {
        margin: 0;
    }

    div.flex {
        display: flex;
        width: 100vw;
        height: 100vh;
        align-items: center;
        justify-content: center;
    }

    div.box {
        display: block;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 10px;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    p {
        margin: 0;
    }

    h1.title {
        text-align: center;
        margin-bottom: 10px;
    }

    hr {
        height: 1px;
        background: #ddd;
        border: none;
    }
    </style>
</head>

<body>
    <div class="flex">
        <div class="box">
            <h1 class="title">404</h1>
            <hr>
            <p>Page is not found!</p>
            <hr>
            <p><a href="https://github.com/reinspect/amok">Amok</a></p>
        </div>
    </div>
</body>

</html>
"""